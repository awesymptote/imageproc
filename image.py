#!/usr/bin/env python
import argparse
import csv
import os

def main():

	# Set up parser 
	parser = argparse.ArgumentParser()
	parser.add_argument("file1",help="first file to compare") # <-- required arg
	parser.add_argument("file2",help="second file to compare") # <-- required arg
	parser.add_argument("-d","--dbg",help="gives detailed csv output",action="store_true") # <-- optional arg
	args = parser.parse_args()

	# If files aren't there, abort gracefully with extra kind message
	if not os.path.exists(args.file1) or not os.path.exists(args.file2):
		print "One or more of the files does not exist, please check that the file names were entered correctly."
		exit()
	
	# Open csv files
	with open(args.file1,"rb") as file1, open(args.file2,"rb") as file2:	
		read1 = csv.reader(file1, delimiter=' ',quotechar='|')
		read2 = csv.reader(file2, delimiter=' ',quotechar='|')

		# Print contents of csv file for debug
		if args.dbg:

		#this iteration assumes that the first row is a header of some sort, might need to change that 
			print "csv file 1 contents here" 
			rownumber = 0
			for row in read1:
				if rownumber == 0:
					header = row
				else:
					colnumber = 0
					for colnumber in row:
						print '%-8s: %s' % (header[colnumber],col)
						colnumber += 1
						rownumber += 1

			print "csv file 2 contents here"
			rownumber = 0
			for row in read2:
				if rownumber == 0:
					header = row
				else:
					colnumber = 0
					for colnumber in row:
						print '%-8s: %s' %(header[colnumber],col)
						colnumber += 1
						rownumber += 1
			





if __name__ == '__main__':
	main()

