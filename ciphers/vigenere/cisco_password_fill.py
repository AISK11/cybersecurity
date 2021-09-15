#!/usr/bin/env python3


import os


def main():
	# Do password encryption:
	print("enable")
	print("conf t")
	print("service password-encryption")
	print("end\n\n")

	# (writable) characters to use to set a password, range: 0x20 = ' ', 0x7E = '~'
	# loop through all characters
	i = 32 # 32 = 0x20
	while i < 126: # 126 = 0x7E
		# append every command to the variable as an item in a list
		OUTPUT = []
		OUTPUT.append("enable")
		OUTPUT.append("conf t")
		OUTPUT.append("line console 0")
		OUTPUT.append(f"password {20 * chr(i)}")
		OUTPUT.append("end")
		OUTPUT.append("show run | i password 7")
		OUTPUT.append("!")
		OUTPUT.append("!")
		
		# this variable contains one big string properly formatted from list variable "OUTPUT"
		OUTPUT_CLEAN = ""
		output_i = 0
		while output_i < len(OUTPUT):
			OUTPUT_CLEAN += OUTPUT[output_i] + "\n"
			output_i += 1	
		
		# print "OUTPUT_CLEAN" to stdout 
		print(f"{OUTPUT_CLEAN}")
		
		# Testing with a file, it turns out, xclip can accept new line, there is something just with a python
		# copy "OUTPUT_CLEAN" to clipboard (xclip does not accepts string containing "\n", so file workaround)
		# create file
		FILE = ".tmp_cisco_pass_fill"
		fw = open(FILE, "w")
		# write variable to file
		fw.write(f"{OUTPUT_CLEAN}")	
		# load file to xclip
		os.system(f'cat {FILE} | xclip -selection clipboard')
		# close file
		fw.close()


		# wait for an input, so it prints one set of chars at a time
		input()
		# continue loop through the all (writable) characters
		i += 1

main()
