#!/usr/bin/env python
import argparse
import csv
import os

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file1",help="first file to compare")
	parser.add_argument("file2",help="second file to compare")
	parser.add_argument("-d","--dbg",help="gives detailed csv output",action="store_true")
	args = parser.parse_args()

	if not os.path.exists(args.file1) or not os.path.exists(args.file2):
		print "One or more of the files does not exist, please check that the file names were entered correctly."
		exit()
		
	
	file1 = open(args.file1,"rb")
	file2 = open(args.file2,"rb")




	if args.dbg:
		print "print csv file contents here"

if __name__ == '__main__':
	main()

