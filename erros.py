#!/usr/bin/env python3
import os
import sys

# LBYL - Look Before You Leap

if os.path.exists('names1.txt'):
	names = open('names1.txt').readlines()
else:
	print('[Error] File names.txt not exists')
	sys.exit(1)


if len(names) >= 3:
    print(names[2])
else:
    print('[Error]: Missing name in the list')
    sys.exit(1)
