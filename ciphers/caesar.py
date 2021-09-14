#!/usr/bin/env python3

import sys
import os

def main():
	# Default values
	decrypt = 1; isText = 1; shift_number = 3
	message_position = 0

	# Check if user typed help argument
	if "-h" in sys.argv or "--help" in sys.argv:
		print(f"Script to encrypt/decrypt caesar cipher.")

	# Check passed arguments
	i = 1
	while i < len(sys.argv): 
		if sys.argv[i] == "-d" or sys.argv[i] == "--decrypt":
			decrypt = 1
		elif sys.argv[i] == "-e" or sys.argv[i] == "--encrypt":
			decrypt = 0
		elif sys.argv[i] == "-n" or sys.argv[i] == "--number":
			# Check if argument after "-n" is number
			try:
				sys.argv[i+1] = int(sys.argv[i+1])
				shift_number = sys.argv[i+1]
				# next value should be int, so skip checking against conditions
				i += 1
			except:
				print(f"Argument '{sys.argv[i+1]}' is not a number but is '{type(sys.argv[i+1]).__name__}'!", file=sys.stderr)
				return -1
		elif sys.argv[i] == "-t" or sys.argv[i] == "--text":
			isText = 1
			message_position = i+1
			# next value should be int, so skip checking against conditions
			i += 1
		elif sys.argv[i] == '-f' or sys.argv[i] == "--file":
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
	
	# Call encrypt or decrypt function
	if message_position != 0:
		decryptMessage(decrypt, isText, shift_number, sys.argv[message_position])
	
	return 0


def decryptMessage(decrypt, isText, shift_number, message):
	decrypted_message = ""
	
	if decrypt == 0:
		shift_number *= -1



	if isText:
		i = 0
		while i < len(message):
			if message[i] >= 'A' and message[i] <= 'Z':
				# convert chars to ints so math can be performed
				if ord(message[i]) - shift_number < ord('A'):
					decrypted_message += chr(ord(message[i]) - shift_number + 26)
				# negative decryption (encryption)
				elif ord(message[i]) - shift_number > ord('Z'):
					decrypted_message += chr(ord(message[i]) - shift_number - 26)
				else:
					decrypted_message += chr(ord(message[i]) - shift_number)
			elif message[i] >= 'a' and message[i] <= 'z':
				# convert chars to ints so math can be performed
				if ord(message[i]) - shift_number < ord('a'):
					decrypted_message += chr(ord(message[i]) - shift_number + 26)
				# negative decryption (encryption)
				elif ord(message[i]) - shift_number > ord('z'):
					decrypted_message += chr(ord(message[i]) - shift_number - 26)
				else:
					decrypted_message += chr(ord(message[i]) - shift_number)
			else:
				decrypted_message += message[i]
			i += 1
			

		if (decrypt):
			print(f"DECRYPTED: {decrypted_message}")
		else:
			print(f"ENCRYPTED: {decrypted_message}")

main()
