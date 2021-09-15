#!/usr/bin/env python3

###################################################
# Author: AISK11								  #
# This script encrypts and decrypts Caesar cipher #
###################################################

import sys
import os
import argparse # https://docs.python.org/3/library/argparse.html#module-argparse


def main():
	# create ArgumentParser object and add description of program:
	parser = argparse.ArgumentParser(description="Decrypts and encrypts Caesar cipher.")

	# mutually exclusive arguments:
	crypt = parser.add_mutually_exclusive_group()
	crypt.add_argument("-d", "--decrypt", action="store_true", default=True, help="decryption - shift letters up X characters (DEFAULT)")
	crypt.add_argument("-e", "--encrypt", action="store_true", default=False, help="encryption - shift letters down X characters")
	# shift argument:
	parser.add_argument("-s", "--shift", default="3", help="specify X, when X is a numerical value or range used to shift letters (DEFAULT 3)")
	# mutually exclusive arguments:
	verbosity = parser.add_mutually_exclusive_group()
	verbosity.add_argument("-v", "--verbose", action="store_true", default=True, help="print header (DEFAULT)")
	verbosity.add_argument("-q", "--quiet", action="store_true", default=False, help="print decrypted/encrypted output only")
	# mutually exclusice arguments:
	text = parser.add_mutually_exclusive_group()
	text.add_argument("-t", "--text", action="store_true", default=True, help="cipher should be read from stdin (DEFAULT)")
	text.add_argument("-f", "--file", action="store_true", default=False, help="cipher should be read from file")
	# positional argument: 
	parser.add_argument("CIPHER", help="specify cipher or file from which read cipher")

	# pass arguments
	args = parser.parse_args()
	
	
	
	num_list = shiftRange(args.shift)
	print(f"{num_list}")




	# exit program with return code 0:
	sys.exit(0)


# accepts range (string) and converts it to integer list
def shiftRange(shiftRange):
	num_list = []
	delim_list = []

	# loop through all characters and separate them (numbers to "num_list", delimeters to "delim_list"):
	num = ""	# temp variable, that separates 0-9 from delimeters ',' and '-'
	i = 0
	while i < len(shiftRange):
		# check if character is number, add to "num" (string):
		if shiftRange[i] >= "0" and shiftRange[i] <= "9":
			num += shiftRange[i]
			# if there is no more delimeter after number, then also add to "num_list":
			if i == len(shiftRange) - 1:
				if num != "":
					num_list.append(int(num))
		# check if character is delimeter, add int(num) to list and current char to "delim_list":
		elif shiftRange[i] == "-" or shiftRange[i] == ",":
			if num != "":
				num_list.append(int(num))
			delim_list.append(shiftRange[i])
			num = ""
		# wrong input:
		else:
			print(f"[!] ERROR! Unknown character detected in '{shiftRange}'!", file=sys.stderr)
			sys.exit(1)
		i += 1


	print(f"num_list: {num_list}")
	print(f"delim_list: {delim_list}")

	return num_list

main()
