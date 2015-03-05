# coding=UTF-8
import sys
file = open(sys.argv[1], 'r')
while True:
	line = file.readline()
	if not line: break
	print line
file.close()
