from PIL import Image, ImageDraw
import random, datetime, os, json

def scale(coords, scaling_factor):
	new_coords = []
	for r in coords:
		x, y = r
		new_coords.append(tuple((x * scaling_factor, y * scaling_factor)))
	return new_coords

## Constants
right_cut_at = 0.5
right_cut_diamond = [(0, 1), (-1, 0), (0, -1), (right_cut_at, -right_cut_at), (right_cut_at, right_cut_at)]
left_cut_diamond = scale(right_cut_diamond, -1)
crosshairs_width = 1 / 50
crosshairs = [(-1, crosshairs_width), (-1, -crosshairs_width), (1, -crosshairs_width), (1, crosshairs_width), (-crosshairs_width, -1), (-crosshairs_width, 1), (crosshairs_width, 1), (crosshairs_width, -1)]

def translate(coords, translation_vector):
	dx, dy = translation_vector
	new_coords = []
	for r in coords:
		x, y = r
		new_coords.append(tuple((dx + x, dy + y)))
	return new_coords

def mkdir(name):
	if not os.path.isdir(name):
		os.makedirs(name)


def draw_diamond(draw_handle, scaling_factor, translation_vector, right_is_cut, color):
	diamond = right_cut_diamond if right_is_cut else left_cut_diamond
	diamond = scale(diamond, scaling_factor)
	diamond = translate(diamond, translation_vector)
	draw_handle.polygon(diamond, fill = color)

def draw_crosshairs(draw_handle, center, color, scaling_factor):
	coords = scale(crosshairs, scaling_factor / 4)
	coords = translate(coords, center)
	draw_handle.polygon(coords[4:], fill = color)
	draw_handle.polygon(coords[:4], fill = color)

def generate_frames(use_clutter):
	""" Returns all 72 possible frames with a 3x3 grid, 4 frame conditions (isolated or cluttered for green or red targets), and whether the target diamond is cut on the left or right.
	If 'use clutter?' is false, we will not use clutter and will thus generate 36 frames instead of 72.
	NOTE THAT the set of frames will be generated deterministicly, and are meant to be shuffled.
	If the frame is cluttered, the colors of the distractors will be randomly generated.
	Currently, the side the distractors are cut on is generated randomly for both isolated and cluttered frames. """
	frames = []
	for target_index in range(9):
		for clutter in ["isolated", "cluttered"] if SETTINGS["use clutter?"] else ["isolated"]:
			for target_color in ["red", "green"]:
				for target_is_cut_on in ["left", "right"]:
					# determine diamond colors
					if clutter == "cluttered":
						opposite_color = "green" if (target_color == "red") else "red"
						all_colors = [opposite_color for _ in range(9)]
						all_colors[target_index] = target_color
					else:
						all_colors = ["NA" for _ in range(9)]
						all_colors[target_index] = target_color
					# determine where diamonds are cut off
					all_cutoffs = [random.choice(["left", "right"]) for _ in range(9)]
					all_cutoffs[target_index] = target_is_cut_on
					frame_parameters = {
					"target index": target_index,
					"clutter condition": clutter,
					"target color": target_color,
					"target cut on": target_is_cut_on,
					"all colors": all_colors,
					"all cutoffs": all_cutoffs}
					frames.append(frame_parameters)
	return frames

def draw_frame(SETTINGS, frame_parameters, filename):
	im = Image.new("RGB", SETTINGS["frame size"], SETTINGS["background color"])
	draw_handle = ImageDraw.Draw(im)
	center = [x / 2 for x in SETTINGS["frame size"]]
	diamond_scale = min(center) * SETTINGS["diamond scale"]
	for n, color, cutoff in zip(range(9), frame_parameters["all colors"], frame_parameters["all cutoffs"]):
		coll = center[0] + (center[0] * SETTINGS["diamond spread"] * ((n % 3) - 1))
		row = center[1] + (center[0] * SETTINGS["diamond spread"] * (int(n / 3) - 1))
		if color == "red": raw_color = SETTINGS["color choices"][0]
		elif color == "green": raw_color = SETTINGS["color choices"][1]
		elif color == "NA": raw_color = SETTINGS["background color"]
		draw_diamond(draw_handle, diamond_scale, [coll, row], cutoff == "right", raw_color)
	im.save(filename, "PNG")

def draw_crosshair_frame(SETTINGS, filename):
	im = Image.new("RGB", SETTINGS["frame size"], SETTINGS["background color"])
	draw = ImageDraw.Draw(im)
	center = [x / 2 for x in SETTINGS["frame size"]]
	draw_crosshairs(draw, center, SETTINGS["crosshair color"], SETTINGS["crosshair scale"])
	im.save(filename, "PNG")

SETTINGS = {
	"background color": (0, 0, 0),
	"color choices": [(255, 0, 0), (0, 255, 0)],
	"crosshair color": (211, 211, 211),
	"frame size": [1280, 1280],
	"diamond scale": 0.05 * 4 / 3,
	"diamond spread": 0.5,
	"crosshair scale": 70,
	"use clutter?": True,
	"seed": 1, ## Seed is optional, though if you choose to provide one it will render frames deterministically (for reproducibility)
}

def make_study(SETTINGS):
	if not "seed" in SETTINGS:
		SETTINGS["seed"] = random.random() *random.seed(SETTINGS["seed"] * 1e8)
    
    	time=str(datetime.datetime.now())
	studies_folder = os.getcwd() + "/studies/"
	root_folder_name = studies_folder + "study " + time + "/"
	frames_folder_name = root_folder_name + "frames/"
	mkdir(studies_folder)
	mkdir(root_folder_name)
	mkdir(frames_folder_name)
	draw_crosshair_frame(SETTINGS, frames_folder_name + "crosshair.png")
	frames = generate_frames(SETTINGS)
	random.shuffle(frames)
	frame_rows = dict([[k, []] for k in frames[0].keys()])
	frame_rows["filepath"] = []
	for n, params in zip(range(len(frames)), frames):
		filename = frames_folder_name + "frame " + str(n) + ".png"
		frame_rows["filepath"].append(filename)
		for k in params.keys():
			frame_rows[k].append(params[k])
		draw_frame(SETTINGS, params, filename)
	with open(root_folder_name + "frames.json", "w") as json_file:
		json.dump(frame_rows, json_file, indent=4)
	return time

#print("Your json file is in\n" + make_study(SETTINGS))
