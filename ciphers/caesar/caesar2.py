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
	crypt.add_argument("-d", "--decrypt", action="store_true", default=True, help="decryption - shift letters <<< by X characters (DEFAULT)")
	crypt.add_argument("-e", "--encrypt", action="store_true", default=False, help="encryption - shift letters >>> by X characters")
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
	parser.add_argument("MESSAGE", help="specify message or file from which text/cipher will be read")

	# pass arguments
	args = parser.parse_args()
	

	# return list filled with numbers according to specified range:
	shift_range = shiftRange(args.shift)


	# check if encrypt flag was set:
	decrypt = 1
	if args.encrypt:
		decrypt = 0

	# check if file flag was set and return list full of outputs to "output":
	if args.file:
		output = processFile(decrypt, shift_range, args.MESSAGE)
	else:
		output = processMessage(decrypt, shift_range, args.MESSAGE)


	# loop through output list:
	i = 0
	while i < len(shift_range):
		if args.quiet:
			print(f"{output[i]}\n")
		else:
			if decrypt:
				print(f"[*] DECRYPTED (using {shift_range[i]} shifts):")
			else:
				print(f"[*] ENCRYPTED (using {shift_range[i]} shifts):")
			print(f"{output[i]}\n")
		i += 1


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
		# Only numbers and '-', ',' are acceptable:
		else:
			print(f"[!] ERROR! Unknown character detected in '{shiftRange}'!", file=sys.stderr)
			sys.exit(1)
		i += 1

	# len(delim_list) must always equal to (len(num_list) - 1)!
	if len(delim_list) >= len(num_list):
		print(f"[!] ERROR! Cannot determine range for '{shiftRange}'!")
		sys.exit(2)

	# translate delimeters to number ranges in variable "new_num_list":
	i = 0
	new_num_list = [num_list[i]] # add first number to list, as delimeter does not affect first number
	while i < len(delim_list):
		# if delimeter is simple ',' then add next number to list, as current is already in the list:
		if delim_list[i] == ',':
			if num_list[i+1] not in new_num_list:
				new_num_list.append(num_list[i+1])
			else:
				print(f"[!] ERROR! Number '{num_list[i+1]}' is specified multiple times!", file=sys.stderr)
				sys.exit(3)
		# if delimeter is '-' (X-Y) then set X as current and keep appending until Y is reached:
		else:
			x = num_list[i]
			y = num_list[i+1]
			# check if X is < than Y:
			if x >= y:
				print(f"[!] ERROR! Number '{x}' must be smaller than '{y}!", file=sys.stderr)
				sys.exit(4)
			# while X < Y:
			while x < y:
				new_num_list.append(x+1) # x+1 because current number X is already in a list
				x += 1
		i += 1

	# A = 0, Z = 25 -> cannot be higher than 25:
	i = 0
	while i < len(new_num_list):
		while new_num_list[i] > 25:
			new_num_list[i] -= 26
		i += 1

	# previous lowering numbers bigger than 25 can create duplicates:
	num_list = [] # this variable was no longer needed, so recycling
	i = 0
	while i < len(new_num_list):
		if new_num_list[i] not in num_list:
			num_list.append(new_num_list[i])
		i += 1
	# sort numbers from lowest to highest:
	num_list.sort()

	# return clean "num_list"
	return num_list


def processFile(decrypt, shift_range, input_file):
	# check if file "input_file" exists:
	if not os.path.exists(input_file):
		print(f"[!] ERROR! File '{input_file}' does not exists!", file=sys.stderr)
		sys.exit(5)
	else:
		# open file
		fo = open(input_file, "r+")

		# read whole file to variable "line"
		line = fo.read(-1)

		# close file
		fo.close()

	#process file content:
	return processMessage(decrypt, shift_range, line)


def processMessage(decrypt, shift_range, message):
	message_processed = ""

	# negative decryption is encryption:
	if decrypt == 0:
		i = 0 
		while i < len(shift_range):
			shift_range[i] *= -1
			i += 1

	output_list = [] # as multiple ranges can be decrypted, each answer will be an item in "output_list"
	output_index = 0 # first decryption 
	while output_index < len(shift_range): 
		shift_number = shift_range[output_index] # current shift which will be used for decryption from "shift_range"
		# decrypt/encrypt the message:
		i = 0 
		while i < len(message):
			if message[i] >= 'A' and message[i] <= 'Z':
				# convert chars to ints so math can be performed:
				if ord(message[i]) - shift_number < ord('A'):
					message_processed += chr(ord(message[i]) - shift_number + 26) 
				# negative decryption (encryption):
				elif ord(message[i]) - shift_number > ord('Z'):
					message_processed += chr(ord(message[i]) - shift_number - 26) 
				else:
					message_processed += chr(ord(message[i]) - shift_number)
			elif message[i] >= 'a' and message[i] <= 'z':
				# convert chars to ints so math can be performed:
				if ord(message[i]) - shift_number < ord('a'):
					message_processed += chr(ord(message[i]) - shift_number + 26) 
				# negative decryption (encryption):
				elif ord(message[i]) - shift_number > ord('z'):
					message_processed += chr(ord(message[i]) - shift_number - 26) 
				else:
					message_processed += chr(ord(message[i]) - shift_number)
			else:
				message_processed += message[i]
			i += 1
		output_list.append(message_processed)
		message_processed = ""
		output_index += 1

	return output_list


main()
