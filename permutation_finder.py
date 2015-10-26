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

    print('Input file is '+inputfile)

    # Words related to the clue, "Cricket in India" or English
    # https://en.wikipedia.org/wiki/Most_common_words_in_English
    common_words = ["USE", "GOOD", "THE", "BE", "TO", "AND", "THAT", "HAVE",
                    "WITH", "ABOUT", "WHICH", "GET", "KNOW", "TAKE", "WANT",
                    "BECAUSE", "DAY", "MOST", "FIRST", "CRICKET", "SCORE",
                    "HE", "FROM", "WHEN", "OTHER", "THAN", "BECAUSE", "LOOK",
                    "ONLY", "NEW", "COULD"]

    current_best_fit = 0
    current_best_fit_value = 0
    with open(inputfile, "r") as fh:
        full_string = fh.read()
        factors_of_lenth = factors(len(full_string))
        print(factors_of_lenth)
        for i in factors_of_lenth:
            print('testing length '+str(i))
            num_substrings = len(full_string) / i
            j = 0
            current_count = 0
            while ((j + i) < full_string):
                row = full_string[j:(j+i)]
                for word in common_words:
                    word_in_string = True
                    for character in word:
                        if character not in row:
                            word_in_string = False
                    if word_in_string:
                        current_count = current_count + 1
                j = j + i
            print('.')
            if current_count > current_best_fit_value:
                current_best_fit_value = current_count
                current_best_fit = i

    print('Current best fit is a row of '+str(current_best_fit)+' characters, at '+str(current_best_fit_value)+' total matches')

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

if __name__ == "__main__":
    main(sys.argv[1:])
