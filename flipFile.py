#!/bin/python

from sys import argv

script, filename, optionalCharacter = argv

# open the original file:
originalFile = open(filename, 'r')

# append "_flipped" to the output file:
flippedFile = open(filename+"_flipped", 'w')

# clear the *_flipped file, if it exists already:
flippedFile.truncate()

# optionalCharacter is what to fill if we want each line to have the same length
longestLine = 0
if 1 == len(optionalCharacter):
    for line in originalFile:
        if longestLine < len(line):
            longestLine = len(line)

originalFile.close()
originalFile = open(filename, 'r')

for line in originalFile:
    # remove newline character:
    line = line.strip(line[-1:])
    # if we want to fill the line with a character, do that:
    if 0 < longestLine:
        line = line + optionalCharacter*(longestLine - len(line))
    # reverse line
    # from http://stackoverflow.com/questions/931092/reverse-a-string-in-python
    flippedLine = line[::-1]

    # handle characters we want to flip:
    dummyCharacter = chr(9)

    string = flippedLine

    string = string.replace(")", dummyCharacter)
    string = string.replace("(", ")")
    string = string.replace(dummyCharacter, "(")

    string = string.replace("}", dummyCharacter)
    string = string.replace("{", "}")
    string = string.replace(dummyCharacter, "}")

    string = string.replace("]", dummyCharacter)
    string = string.replace("[", "]")
    string = string.replace(dummyCharacter, "[")

    string = string.replace("\\", dummyCharacter)
    string = string.replace("/", "\\")
    string = string.replace(dummyCharacter, "/")

    string = string.replace(">", dummyCharacter)
    string = string.replace("<", ">")
    string = string.replace(dummyCharacter, "<")

    flippedFile.write(string)
    # write the stripped newline character back:
    flippedFile.write("\n")

originalFile.close()	
flippedFile.close()

