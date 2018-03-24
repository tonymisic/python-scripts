import os, re, shutil

inFile = open('input.txt')
outFile = open('output.txt', 'w')
data = inFile.read()
outFile.write(data)
inFile.close()
outFile.close()

