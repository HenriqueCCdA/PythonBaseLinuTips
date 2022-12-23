#!/usr/bin/env python3
import os
import sys

# LBYL - Look Before You Leap

# if os.path.exists('names1.txt'):
	# names = open('names1.txt').readlines()
# else:
	# print('[Error] File names.txt not exists')
	# sys.exit(1)

# if len(names) >= 3:
    # print(names[2])
# else:
    # print('[Error]: Missing name in the list')
    # sys.exit(1)

# EAFP - Easy to Ask Forgiveness than permission

try:
	names = open('names.txt').readlines()
except FileNotFoundError as e:
	print(f'[Error] {str(e)}.')
	sys.exit(e.errno)
	# TODO: User retry
else:
	print('Sucesso!!!')
finally:
	print('Execute isso sempre!')
	
try:
    print(names[0])
except:
	print('[Error]: Missing name in the list')
	sys.exit(1)
