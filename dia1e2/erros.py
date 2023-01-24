#!/usr/bin/env python3
import os
import sys
import time
import logging

log = logging.Logger("errors")

# def try_to_open_a_file(filepath, retry=1):
	# for attempt in range(1, retry + 1):
		# try:
			# return open(filepath).readlines()
		# except FileNotFoundError as e:
			# log.error("ERRO: %s", e)
			# time.sleep(1)
		# else:
			# print('Sucesso!!!')
		# finally:
			# print('Execute isso sempre!')
	# return []
	# 
# 
# for line in try_to_open_a_file("names1txt", retry=3):
	# print(line)


def try_to_open_a_file(filepath, retry=1):

	if retry > 999:
		raise ValueError("Retry cannot be above 999")

	try:
		return open(filepath).readlines()
	except FileNotFoundError as e:
		log.error("ERRO: %s", e)
		time.sleep(2)
		if retry > 1:
			return try_to_open_a_file(filepath, retry=retry-1)
	else:
		print('Sucesso!!!')
	finally:
		print('Execute isso sempre!')

	return []

for line in try_to_open_a_file("names1.txt", retry=500):
	print(line)
