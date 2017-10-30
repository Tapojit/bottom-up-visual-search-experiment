from PIL import Image, ImageDraw
import random, datetime, os, json

def scale(coords, scaling_factor):
	new_coords = []
	for r in coords:
		x, y = r
		new_coords.append(tuple((x * scaling_factor, y * scaling_factor)))
	return new_coords

## Constants

#right_cut_diamond = [(0, 1), (-1, 0), (0, -1), (0.5, -0.5), (0.5, 0.5)]
#left_cut_diamond = scale(right_cut_diamond, -1)
def rotate(point):
	x, y = point
	return [y, -x]

right_cut_diamond = [(-1, 0.2,), (-1, -0.2,), (1, -0.2,), (1, 0.2,)]
left_cut_diamond = [rotate(p) for p in right_cut_diamond]


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

def generate_frames():
	orientations = ["left", "right"]
	frames = []
	for target_index in range(9):
		for oi in [0,1]:
			for ci in [0,1]:
				all_visibility = [ci for _ in range(9)]
				all_visibility[target_index] = 1
				all_orientations = [orientations[(oi+1)%2] for _ in range(9)]
				all_orientations[target_index] = orientations[oi]
				frame_parameters = {
						"target index": target_index,
						"visible?": all_visibility,
						"target color": "red",
						"all colors": ["red" for _ in range(9)],
						"target cut on": orientations[oi],
						"all cutoffs": all_orientations}
				frames.append(frame_parameters)
	random.shuffle(frames)
	return [frames[:9], frames[9:]]

def draw_frame(SETTINGS, frame_parameters, filename):
	im = Image.new("RGB", SETTINGS["frame size"], SETTINGS["background color"])
	draw_handle = ImageDraw.Draw(im)
	center = [x / 2 for x in SETTINGS["frame size"]]
	diamond_scale = min(center) * SETTINGS["diamond scale"]
	for n, visible, color, cutoff in zip(range(9), frame_parameters["visible?"], frame_parameters["all colors"], frame_parameters["all cutoffs"]):
		coll = center[0] + (center[0] * SETTINGS["diamond spread"] * ((n % 3) - 1))
		row = center[1] + (center[1] * SETTINGS["diamond spread"] * (int(n / 3) - 1))
		color = SETTINGS["background color"] if (visible == 0) else SETTINGS["color choices"][0] if color == "red" else SETTINGS["color choices"][1]
		draw_diamond(draw_handle, diamond_scale, [coll, row], cutoff == "right", color)
	im.save(filename, "PNG")

def draw_crosshair_frame(SETTINGS, filename):
	im = Image.new("RGB", SETTINGS["frame size"], SETTINGS["background color"])
	draw = ImageDraw.Draw(im)
	center = [x / 2 for x in SETTINGS["frame size"]]
	draw_crosshairs(draw, center, SETTINGS["crosshair color"], SETTINGS["crosshair scale"])
	im.save(filename, "PNG")

SETTINGS = {
	"background color": (0, 0, 0),
	"color choices": [(255, 255, 255), (255, 255, 255)], #[(255, 0, 0), (0, 255, 0)],
	"crosshair color": (211, 211, 211),
	"frame size": [640, 640],
	"diamond scale": 0.05,
	"diamond spread": 0.5,
	"crosshair scale": 70,
	"seed": 1, ## Seed is optional, though if you choose to provide one it will render frames deterministically (for reproducibility)
}

def make_study(SETTINGS):
	if not "seed" in SETTINGS:
		SETTINGS["seed"] = random.random()
	random.seed(SETTINGS["seed"] * 1e8)

	time=str(datetime.datetime.now())
	studies_folder = os.getcwd() + "/studies/"
	
	root_folder_name = studies_folder + "study " + time + "/"
	frames_folder_name = root_folder_name + "frames/"
	mkdir(studies_folder)	
	mkdir(root_folder_name)
	mkdir(frames_folder_name)
	draw_crosshair_frame(SETTINGS, frames_folder_name + "crosshair.png")
	frame_combos = generate_frames()
	frames = []
	for i in range(2):
		a, b = frame_combos
		random.shuffle(a)
		random.shuffle(b)
		frames += a
		frames += b
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
