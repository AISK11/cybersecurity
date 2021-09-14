#!/usr/bin/env python3

import sys
import os

def main():
	# get arguments to work with them further
	arguments = checkArguments()
	decrypt = arguments[0]
	shift_number = arguments[1]
	isText = arguments[2]
	message_position = arguments[3]

	# if input is a string from CLI
	if isText:
		output = processMessage(decrypt, shift_number, message_position)
	# else input is a file
	else:
		output = processFile(decrypt, shift_number, message_position)

	# nice formatting at the end, so user knows, if he encrypted or decrypted
	if decrypt:
		print("DECRYPTED:")
	else:
		print("ENCRYPTED:")
	print(f"{output}")
	return 0


def getHelp():
	print("HELP - ToDo")
	exit()


def checkArguments():
	# default argument values
	decrypt = 1; isText = 1; shift_number = 3; message_position = 0

	# check if user typed help argument
	if "-h" in sys.argv or "--help" in sys.argv:
		getHelp()

	# check passed arguments
	i = 1
	while i < len(sys.argv): 
		if sys.argv[i] == "-d" or sys.argv[i] == "--decrypt":
			decrypt = 1
		elif sys.argv[i] == "-e" or sys.argv[i] == "--encrypt":
			decrypt = 0
		elif sys.argv[i] == "-n" or sys.argv[i] == "--number":
			# check if argument after "-n" exists
			if i+1 > len(sys.argv)-1:
				print(f"ERROR! Expected argument after '{sys.argv[i]}'!", file=sys.stderr)
				exit()
			# check if argument after "-n" is number and overwrite default shift_number
			try:
				sys.argv[i+1] = int(sys.argv[i+1])
				shift_number = sys.argv[i+1]
				# next value should be int, so skip checking against conditions
				i += 1
			except:
				print(f"ERROR! Argument '{sys.argv[i+1]}' is not a number but is '{type(sys.argv[i+1]).__name__}'!", file=sys.stderr)
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
		elif sys.argv[i] == '-f' or sys.argv[i] == "--file":
			# check if argument after "-t" exists
			if i+1 > len(sys.argv)-1:
				print(f"ERROR! Expected argument after '{sys.argv[i]}'!", file=sys.stderr)
				exit()
			isText = 0
			# next value should be int, so skip checking against conditions
			message_position = i+1
			i += 1
		i += 1

	# A = 0, Z = 26 -> cannot be higher than 26
	while shift_number > 25:
		shift_number -= 26
	while shift_number < -25:
		shift_number += 26

	# check if message to decrypt was specified
	if message_position != 0:
		# Pass arguments back to main
		return [decrypt, shift_number, isText, sys.argv[message_position]]
	else:
		print(f"ERROR! No text to encrypt/decrypt!", file=sys.stderr)
		exit()

def processFile(decrypt, shift_number, input_file):
	# check if file input_file exists
	if not os.path.exists(input_file):
		print(f"ERROR! File '{input_file}' does not exists!", file=sys.stderr)
		exit()
	else:
		# open file
		fo = open(input_file, "r+")
		
		# read whole file
		line = fo.read(-1)
		print(f"{line}")
		
		# close file
		fo.close()

	# process file content
	return processMessage(decrypt, shift_number, line)


def processMessage(decrypt, shift_number, message):
	message_processed = ""
	
	# negative decryption is encryption
	if decrypt == 0:
		shift_number *= -1
	
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
			
	return message_processed	

main()
