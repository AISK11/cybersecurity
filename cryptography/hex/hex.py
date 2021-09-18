#!/usr/bin/env python3

###################################################
# Author: AISK11								  #
# This script encrypts and decrypts Hex To String #
###################################################

import sys
import os
import argparse


def main():
    # create ArgumentParser object and add description of program:
    parser = argparse.ArgumentParser(
        description="Decrypts and encrypts HEX to string")

    # mutually exclusive arguments:
    crypt = parser.add_mutually_exclusive_group()
    crypt.add_argument(
        "-d",
        "--decrypt",
        action="store_true",
        default=True,
        help="decryption - convert hex values to string (DEFAULT)")
    crypt.add_argument(
        "-e",
        "--encrypt",
        action="store_true",
        default=False,
        help="encryption - convert string to hex values")
    # mutually exclusive arguments:
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=True,
        help="print header (DEFAULT)")
    verbosity.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        default=False,
        help="print decrypted/encrypted output only")
    # mutually exclusice arguments:
    text = parser.add_mutually_exclusive_group()
    text.add_argument(
        "-t",
        "--text",
        action="store_true",
        default=True,
        help="read from stdin (DEFAULT)")
    text.add_argument(
        "-f",
        "--file",
        action="store_true",
        default=False,
        help="read from file")

    # positional argument:
    parser.add_argument(
        "MESSAGE",
        help="specify message or file from which input will be read")

    # pass arguments
    args = parser.parse_args()

    # check if file flag was set and return message to "msg":
    if args.file:
        msg = readFile(args.MESSAGE)
    else:
        msg = args.MESSAGE

    # check if encrypt flag was set:
    decrypt = 1
    if args.encrypt:
        decrypt = 0
        output = hexToString(decrypt, msg)
        if not args.quiet:
            print(f"\n[+] Encrypted message to hexadecimal:")
        print(f"{output}")
    else:
        output = hexToString(decrypt, msg)
        if not args.quiet:
            print(f"\n[+] Decrypted hexadecimal message:")
        print(f"{output}")


# return text from a file
def readFile(input_file):
    # check if file "input_file" exists:
    if not os.path.exists(input_file):
        print(
            f"[!] ERROR! File '{input_file}' does not exists!",
            file=sys.stderr)
        sys.exit(1)

    # open file:
    fo = open(input_file, "r+")

    # read whole file to variable "msg":
    msg = fo.read(-1)

    # close file:
    fo.close()

    return msg


def hexToString(decrypt, msg):
    output = ""

    # auto remove '\n':
    msg_f = ""
    i = 0
    while i < len(msg):
        if msg[i] != '\n':
            msg_f += msg[i]
        i += 1

    if decrypt:
        # 1A2b = 1a2b:
        msg_f = msg_f.lower()

        # "msg_f" must have even length:
        if len(msg_f) % 2 != 0:
            print(
                f"[!] ERROR! '{msg_f}' has odd amount of characters ({len(msg_f)})!",
                file=sys.stderr)
            sys.exit(2)

        # remove "0x" and "\x" if it does exists and write to "msg":
        msg = ""
        i = 0
        # make sure, that 'i+1' will not get bigger than "len(msg_f)":
        while i < len(msg_f) - 1:
            if (msg_f[i] != '0' or msg_f[i] != '\\') and msg_f[i + 1] != 'x':
                msg += msg_f[i] + msg_f[i + 1]
            i += 2

        # range must be from [0-9,a-f]:
        for l in msg:
            if l < '0' or (l > '9' and l < 'a') or l > 'f':
                print(
                    f"[!] ERROR! '{l}' in {msg} is not a hexadecimal character!")
                sys.exit(3)

        # convert "msg" to hex and store in "output":
        i = 0
        while i < len(msg) - 1:
            tmp = msg[i] + msg[i + 1]  # hex value contains 2 hex nums

            dec = int(tmp, 16)  # hex to dec
            output += chr(dec)  # add decoded value to output as char

            i += 2
    else:
        i = 0
        while i < len(msg_f):
            # convert char to hex value and add to "output: as string:
            # get ascii dec value, convert to hex, strip leading "0x"
            output += hex(ord(msg_f[i])).strip("0x")
            i += 1

    return output


main()
