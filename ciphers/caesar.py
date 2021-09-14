#!/usr/bin/env python3

###################################################
# Author: AISK11                                  #
# This script encrypts and decrypts Caesar cipher # 
###################################################

import sys
import os

def main():
	# get arguments to work with them further
	arguments = checkArguments()
	decrypt = arguments[0]
	isText = arguments[1]
	num_list = arguments[2]
	message_position = arguments[3]
	verbose = arguments[4]

	# input is a string from CLI
	if isText:
		output = processMessage(decrypt, num_list, message_position)
	# input is a file
	else:
		output = processFile(decrypt, num_list, message_position)

	# loop through output list
	i = 0
	while i < len(num_list):
		if verbose:
			if decrypt:
				print(f"DECRYPTED (using {num_list[i]} shift):")
			else:
				print(f"ENCRYPTED (using {num_list[i] * -1} shift):")
		print(f"{output[i]}\n")	
		i += 1

	return 0



# print help and exit
def getHelp():
	print("This script encrypts and decrypts Caesar cipher.\n")
	print(f"SYNTAX:\n{sys.argv[0]} [OPTIONS] <-t TEXT|-f FILE>\n")
	print("OPTIONS:")
	print("-h      | --help      \tPrint (this) help menu.")
	print("-d      | --decrypt   \tUse decryption - shift letters up X characters. (DEFAULT)")
	print("-e      | --encrypt   \tUse encryption - shift letters down X characters.")
	print("-s X    | --shift X   \tSpecify X, when X is a numerical value or range used to shift letters. (DEFAULT=3)")
	print("-t TEXT | --text TEXT \tSpecify, that stdin should be read.")
	print("-f FILE | --file FILE \tSPECIFY, that stdin should be read from a file.")
	print("-v      | --verbose   \tPrint header. (DEFAULT)")
	print("-q      | --quiet     \tPrint decrypted/encrypted output only.")
	print("\nEXAMPLES:")
	print("Decrypt string with default letter shift by 3:")
	print(f"    {sys.argv[0]} -t ENCRYPTED-TEXT")
	print(f"    {sys.argv[0]} -d -n 3 -t ENCRYPTED-TEXT")
	print("Decrypt specified file by 5 to 8 letter shift with quiet output:")
	print(f"    {sys.argv[0]} -d -n 5,8 -f ENCRYPTED-FILE -q")
	print("Encrypt specified file by 1, 3, 8 to 11 and 15 letter shift with quiet output:")
	print(f"    {sys.argv[0]} -e -n 1,3,8-11,15 -f DECRYPTED-FILE -q")
	exit()


def fillDelimeterWithNumbers(num_list, delimeter_list):
	i = 0
	
	# fill list with default 3 if list is empty
	if num_list == []:
		num_list.append(3)

	# add first number to list, as delimeter does not affect first number
	new_num_list = [num_list[i]]
	x = 0
	# iterate through delimeters
	while i < len(delimeter_list):
		# if delimeter is simple ',', then add next number to list, as current is already in the list, if is not already in		
		if delimeter_list[i] == ",":
			if not num_list[i+1] in new_num_list:
				new_num_list.append(num_list[i+1])
			else:
				print(f"ERROR! '{num_list[i+1]}' is specified multiple times!", file=sys.stderr)
		# if delimeter is '-' (X-Y) then set X as current and keep appending until Y is reached
		else:
			x = num_list[i]
			y = num_list[i+1]
			# check if X is < than Y
			if x >= y:
				print(f"ERROR! Number '{x}' must be smaller than '{y}'!")
				exit()
			# while X <= Y
			while x < y:
				new_num_list.append(x+1)
				x += 1
		i += 1

	# A = 0, Z = 25 -> cannot be higher than 25
	i = 0
	while i < len(new_num_list):
		while new_num_list[i] > 25:
			new_num_list[i] -= 26
		i += 1
	# sort numbers in list and omit duplicates
	clean_list = []
	i = 0
	while i < len(new_num_list):
		if not new_num_list[i] in clean_list:
			clean_list.append(new_num_list[i])
		i += 1
	return clean_list	


# check passed arguments and pass them to main
def checkArguments():
	# default argument values
	decrypt = 1; isText = 1; num_list = []; delimeter_list = []; message_position = 0; verbose = 1
	
	# check if user typed help argument
	if "-h" in sys.argv or "--help" in sys.argv:
		getHelp()

	# loop through passed arguments
	i = 1
	while i < len(sys.argv): 
		if sys.argv[i] == "-d" or sys.argv[i] == "--decrypt":
			decrypt = 1
		elif sys.argv[i] == "-e" or sys.argv[i] == "--encrypt":
			decrypt = 0
		
		#elif sys.argv[i] == "-n" or sys.argv[i] == "--number":
		#	# check if argument after "-n" exists
		#	if i+1 > len(sys.argv)-1:
		#		print(f"ERROR! Expected argument after '{sys.argv[i]}'!", file=sys.stderr)
		#		exit()
		#	# check if argument after "-n" is number and overwrite default shift_number
		#	try:
		#		sys.argv[i+1] = int(sys.argv[i+1])
		#		shift_number = sys.argv[i+1]
		#		# next value should be int, so skip checking against conditions
		#		i += 1
		#	except:
		#		print(f"ERROR! Argument '{sys.argv[i+1]}' is not a number but is '{type(sys.argv[i+1]).__name__}'!", file=sys.stderr)
		#		exit()
	
		elif sys.argv[i] == "-s" or sys.argv[i] == "--shift":
				# check if argument after "-n" exists
				if i+1 > len(sys.argv)-1:
					print(f"ERROR! Expected argument after '{sys.argv[i]}'!", file=sys.stderr)
					exit()

				number_range = sys.argv[i+1] # next argument e.g. "5-11,14,16,18-23"
				num_index = 0				 # iteration for while loop
				num	= ""					 # this variable will be delimiting numbers from ',' and '-'
				#delimeter_list = []		 # list full of delimeters (defined above), here for the comment
				#num_list = []				 # after number is found, it will be converted to int and appended to this list, defined above, here for the comment
				while num_index < len(number_range):
					# if character is number, add to "num" (string)
					if number_range[num_index] >= "0" and number_range[num_index] <= "9":
						num += number_range[num_index]
						# if there is no more delimeter at the end, then also add number to num_list
						if num_index == len(number_range) - 1:
							if num != "":
								num_list.append(int(num))
					# if character is delimeter, convert num to string, add to list and clear value
					# also add delimeter to delimeter list
					elif number_range[num_index] == "-":
						if num != "":
							num_list.append(int(num))
						delimeter_list.append("-")
						num = ""
					# 2nd type of delimeter	
					elif number_range[num_index] == ",":
						if num != "":
							num_list.append(int(num))
						delimeter_list.append(",")
						num = ""
					# wrong input was put
					else:
						print(f"ERROR! Wrong input was detected! '{number_range}' is in a wrong format!", file=sys.stderr)
						exit()
					num_index += 1
				# len(delimeter_list) must always equal len(num_list) - 1
				if len(delimeter_list) >= len(num_list):
					print(f"ERROR! Wrong input was detected! '{number_range}' is in a wrong format!", file=sys.stderr)
					exit()

		elif sys.argv[i] == "-t" or sys.argv[i] == "--text":
			# check if argument after "-t" exists
			if i+1 > len(sys.argv)-1:
				print(f"ERROR! Expected argument after '{sys.argv[i]}'!", file=sys.stderr)
				exit()		
			isText = 1
			message_position = i+1
			# next value should be int, so skip checking against conditions
			i += 1
		elif sys.argv[i] == "-f" or sys.argv[i] == "--file":
			# check if argument after "-t" exists
			if i+1 > len(sys.argv)-1:
				print(f"ERROR! Expected argument after '{sys.argv[i]}'!", file=sys.stderr)
				exit()
			isText = 0
			# next value should be int, so skip checking against conditions
			message_position = i+1
			i += 1
		elif sys.argv[i] == "-q" or sys.argv[i] == "--quiet":
			verbose = 0
		elif sys.argv[i] == "-v" or sys.argv[i] == "--verbose":
			verbose = 1
		i += 1

	# Get all specified numbers form a range
	num_list = fillDelimeterWithNumbers(num_list, delimeter_list)

	# check if message to decrypt was specified
	if message_position != 0:
		# Pass arguments back to main
		return [decrypt, isText, num_list, sys.argv[message_position], verbose]
	else:
		print(f"ERROR! No text to encrypt/decrypt!", file=sys.stderr)
		exit()

def processFile(decrypt, num_list, input_file):
	# check if file input_file exists
	if not os.path.exists(input_file):
		print(f"ERROR! File '{input_file}' does not exists!", file=sys.stderr)
		exit()
	else:
		# open file
		fo = open(input_file, "r+")
		
		# read whole file
		line = fo.read(-1)
		
		# close file
		fo.close()

	# process file content
	return processMessage(decrypt, num_list, line)


def processMessage(decrypt, num_list, message):
	message_processed = ""
	
	# negative decryption is encryption
	if decrypt == 0:
		i = 0
		while i < len(num_list):
			num_list[i] *= -1	
			i += 1

	output_list = []
	output_index = 0
	while output_index < len(num_list):
		shift_number = num_list[output_index]
		# process message and retrun message_processed
		i = 0
		while i < len(message):
			if message[i] >= 'A' and message[i] <= 'Z':
				# convert chars to ints so math can be performed
				if ord(message[i]) - shift_number < ord('A'):
					message_processed += chr(ord(message[i]) - shift_number + 26)
				# negative decryption (encryption)
				elif ord(message[i]) - shift_number > ord('Z'):
					message_processed += chr(ord(message[i]) - shift_number - 26)
				else:
					message_processed += chr(ord(message[i]) - shift_number)
			elif message[i] >= 'a' and message[i] <= 'z':
				# convert chars to ints so math can be performed
				if ord(message[i]) - shift_number < ord('a'):
					message_processed += chr(ord(message[i]) - shift_number + 26)
				# negative decryption (encryption)
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
