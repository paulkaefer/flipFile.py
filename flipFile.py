#!/bin/python

from sys import argv

script, filename = argv

file = open(filename, 'r')
flippedFile = open(filename+"_flipped", 'w')
flippedFile.truncate()# clear what exists already

for line in file:
    flippedLine = line[::-1]
    flippedFile.write(flippedLine)
    # We don't need to write a new line, since that will be written at the beginning of each line:
    #flippedFile.write("\n")

# write a new line, since the first line in the file will be blank, and it won't write a new line after the last line of the original file:
flippedFile.write("\n")

file.close()	
flippedFile.close()
