#!/usr/bin/python

import sys

str = sys.argv[1]

for i in range(0, len(str) - 1):
	print str[i],
print str[len(str) - 1]

for i in range(1, len(str) - 1):
	print str[i],
	for j in range(0, len(str) - 2):
		sys.stdout.write("   ")
	print str[len(str) - 1 - i]

for i in range(0, len(str) - 1):
	print str[len(str) - 1 - i],
sys.stdout.write(str[0])