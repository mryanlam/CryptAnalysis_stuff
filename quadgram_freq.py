#!/usr/bin/python

# Matthew Lam
# Cryptography
# Letter Frequency in python

import os
import sys
import getopt
import operator

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
        full_string = fh.read()
        for i in range(len(full_string) - 3):
            bigram = str(full_string[i]) + str(full_string[i+1] + str(full_string[i+2] + str(full_string[i+3]))
            if bigram in freq_dict.keys():
                freq_dict[bigram] += 1
            else:
                freq_dict[bigram] = 1

    # Sort by value
    with open(outputfile, "w") as fh:
        for key in sorted(freq_dict, key=freq_dict.get, reverse=True):
            fh.write(str(key)+","+str(freq_dict[key])+"\n")
        # for key in freq_dict.keys():
        #     fh.write("Key: "+str(key)+" -> "+str(freq_dict[key])+"\n")


if __name__ == "__main__":
    main(sys.argv[1:])
