#!/usr/bin/env python3

def main():
	# Do password encryption:
	print("enable")
	print("conf t")
	print("service password-encryption")
	print("end\n\n")

	#0x20 = ' ', 0x7E = '~'
	i = 32
	while i < 126:
		#print(f"\nCURRENT char: {chr(i)}\n")
	
		print("enable")
		print("conf t")
		print("line console 0")
		print(f"password {20 * chr(i)}")
		print("end")
		print("show run | i password 7")
		print("!")
		print("!")
		
		# ToDo: Add copy to X11 clipboard

		input()
		i += 1

main()
