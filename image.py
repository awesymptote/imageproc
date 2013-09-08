#!/usr/bin/env python
import argparse
import csv
import os
import sys
import Image, ImageDraw

def main():
	# Dougs branch
	# Set up parser 
	parser = argparse.ArgumentParser()
	parser.add_argument("file1",help="first file to compare") # <-- required arg
	parser.add_argument("file2",help="second file to compare") # <-- required arg
	parser.add_argument("outfile",help="name of output file") # <-- required arg
	parser.add_argument("-d","--dbg",help="gives detailed csv output",action="store_true") # <-- optional arg

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
		maxDeltaIndices = []
		
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

			
			if maxDeltaVal != 0:
				for col in range(0,30):
					bigArray[row][col] = float(bigArray[row][col]/maxDeltaVal)
					print "Normalized diffs: %f" % bigArray[row][col]

		# Random code that just creates white image for now

		img = Image.new('RGB',(400,400),"white")
		draw = ImageDraw.Draw(img)
		draw.line((0,0) + img.size, fill=128)
		draw.line((0,img.size[1],img.size[0],0),fill=128)
		del draw
		img.save(args.outfile,"PNG")



if __name__ == '__main__':
	main()

