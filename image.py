#!/usr/bin/env python
import argparse
import csv
import os
import sys

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

		'''
		# Print contents of csv file for debug to stdout
		if args.dbg:

			read1 = csv.reader(file1)
			read2 = csv.reader(file2)

			print "csv file 1 contents here" 
			for row in read1:
		       		for col in row:
		       			sys.stdout.write('%s' % col)
				print "\n"


			print "csv file 2 contents here"
			for row in read2:
				for col in row:
		       			sys.stdout.write('%s' % col)
				print "\n"
		'''

		#Use python lists b/c we have two files?

		
		# theoretically should have the deltas for each row...
		bigArray = []
		for row in range(0,20):
			bigArray.append([])
			for col in range(0,30):
				bigArray[row].append(abs(float(list1[row][col])-(float(list2[row][col]))))
				
		


if __name__ == '__main__':
	main()

