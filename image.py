#!/usr/bin/env python
import argparse
import csv
import os
import sys
import Image, ImageDraw

def main():

	# Set up parser 
	parser = argparse.ArgumentParser()
	parser.add_argument("file1",help="first file to compare") # <-- required arg
	parser.add_argument("file2",help="second file to compare") # <-- required arg
	parser.add_argument("outfile",help="name of output file") # <-- required arg
	parser.add_argument("-d","--dbg",help="gives normalized delta output",action="store_true") # <-- optional arg

	args = parser.parse_args()

	# If files aren't there, abort gracefully with extra kind message
	if not os.path.exists(args.file1) or not os.path.exists(args.file2):
		print "One or more of the files does not exist, please check that the file names were entered correctly."
		exit()
	
	# Open csv files
	with open(args.file1,"rb") as file1, open(args.file2,"rb") as file2:	

		# Putting files into 2 dimensional lists
		list1 = list(csv.reader(file1))
		list2 = list(csv.reader(file2))

		
		# Here is the logic to build the array of delta arrays
		bigArray = []

		# Fill array with required values
		for row in range(0,20):
			bigArray.append([])
			i = 0
			maxDeltaVal = 0
			maxDeltaIndex = 0
			for col in range(0,30):
				deltaVal = abs((float(list1[row][col]))-(float(list2[row][col])))
				if deltaVal > maxDeltaVal:
					maxDeltaVal = deltaVal
				bigArray[row].append(deltaVal)

			# Normalize values
			if maxDeltaVal != 0:
				for col in range(0,30):
					bigArray[row][col] = float(bigArray[row][col]/maxDeltaVal)

					# If in debug mode:
					if args.dbg:
						print "Normalized deltas: %f" % bigArray[row][col]

		# Random code that just creates white image for now

		img = Image.new('RGB',(400,400),"white")
		draw = ImageDraw.Draw(img)
		
		# drawn delta width will be 10px
		linewidth = 10
		ystart = 10
		xstart = 10
		for r in range(0,20):
			xstart = 50
			for c in range(0,30):
				draw.line((xstart,ystart,xstart+linewidth,ystart), fill=(red(bigArray[r][c]),0,blue(bigArray[r][c])), width=5)
				xstart += linewidth

			ystart += 20
		del draw
		img.save(args.outfile+".png","PNG")

# Large deltas = more red
def red(delta):
	return int(delta*float(255))

# Small deltas = more blue
def blue(delta):
	return int((float(1)-delta)*float(255))


if __name__ == '__main__':
	main()

