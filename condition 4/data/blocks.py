import sys, tempfile, os, csv

def convert_blocks(filename):
	temp_file = tempfile.NamedTemporaryFile(mode="w", delete=False)
	block_number = 0
	csv_opened = open(filename, 'r')
	reader = csv.DictReader(csv_opened)
	last_color = False
	last_position = False
	for i, row in enumerate(reader):
		if (i == 0):
			if ("block number" in row.keys()):
				return "Already had 'block number'"
			else:
				writer = csv.DictWriter(temp_file, fieldnames=list(row.keys()) + ["block number", "same color as last?", "same position as last?"], lineterminator=",\n")
				writer.writeheader()
		if not row['corrAns']: # the absence of corrAns indicates a blank row, thus incrementing the block number
			block_number += 1
			last_color = False
			last_position = False
			continue
		row["block number"] = block_number
		row["same color as last?"] = (row["color"] == last_color)
		row["same position as last?"] = (row["position"] == last_position)
		last_color = row["color"]
		last_position = row["position"]
		writer.writerow(row)
	csv_opened.close()
	temp_file.close()
	os.rename(temp_file.name, os.path.abspath(filename))
	return "Success"


if __name__ == "__main__":
	filename = sys.argv[1]
	print(convert_blocks(filename))

