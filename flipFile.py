#!/bin/python

from sys import argv

script, filename = argv

# open the original file:
originalFile = open(filename, 'r')

# append "_flipped" to the output file:
flippedFile = open(filename+"_flipped", 'w')

# clear the *_flipped file, if it exists already:
flippedFile.truncate()

for line in file:
    # reverse line
    # from http://stackoverflow.com/questions/931092/reverse-a-string-in-python
    flippedLine = line[::-1]
    flippedFile.write(flippedLine)
    # We don't need to write a new line, since that will be written at the beginning of each line:
    #flippedFile.write("\n")

# write a new line, since the first line in the file will be blank, and it won't write a new line after the last line of the original file:
flippedFile.write("\n")

file.close()	
flippedFile.close()

