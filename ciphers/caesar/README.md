# caesar.py
This program will fill RAM with specified amount of megabytes.

### INSTALLATION
1. make sure to have **python3**, **make** and **git** pacakges installed. You can install it with:
* Debian based distros:\
`sudo apt install python3 make git`
1. clone repository:\
`git clone https://github.com/AISK11/cybersecurity`
1. navigate to directory:\
`cd ./cybersecurity/ciphers/caesar`
1. make executable:\
`make`

### Usage
* Get help:
`./caesar.py -h`
* Decrypt string with default letter shift by 3:
`./caesar.py -t ENCRYPTED-TEXT`
`./caesar.py -d -s 3 -t ENCRYPTED-TEXT`
* Decrypt specified file by 5 to 8 letter shift with quiet output:
`./caesar.py -d -s 5,8 -f ENCRYPTED-FILE -q`
/ Encrypt specified file by 1, 3, 8 to 11 and 15 letter shift with quiet output:
`./caesar.py -e -s 1,3,8-11,15 -f DECRYPTED-FILE -q`
