#!/usr/bin/python

# Matthew Lam
# Cryptography
# Letter Frequency in python

import os
import sys
import getopt

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('test.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	
	print('Input file is '+inputfile)
	print('Output file is '+outputfile)

	freq_dict = {}
	with open(inputfile, "r") as fh:
		for word in fh:
			for ch in word:
				if ch in freq_dict.keys():
					freq_dict[ch] += 1
				else:
					freq_dict[ch] = 1
	# Sort by Key
	with open(outputfile, "w") as fh:
		for key in sorted(freq_dict):
			fh.write(str(key)+","+str(freq_dict[key])+"\n")
		# for key in freq_dict.keys():
		# 	fh.write("Key: "+str(key)+" -> "+str(freq_dict[key])+"\n")


if __name__ == "__main__":
	main(sys.argv[1:])


