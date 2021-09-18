# hex.py
Decrypts and encrypts Hex To String

### INSTALLATION
1. make sure to have **python3**, **make** and **git** pacakges installed. You can install it with:
* Debian based distros:\
`sudo apt install python3 make git`
1. clone repository:\
`git clone https://github.com/AISK11/cybersecurity`
1. navigate to directory:\
`cd ./cybersecurity/cryptography/hex`
1. make executable:\
`make`

### Syntax
`usage: hex.py [-h] [-d | -e] [-v | -q] [-t | -f] MESSAGE`

### Examples
* Get help:\
`./hex.py -h`
* Decrypt hex string from stdin\
`./hex.py MESSAGE`\
`./hex.py -d -v -t MESSAGE`
* Decrypt specified file with quiet output:\
`./hex.py -q -f FILE`
* Encrypt specific string from file:\
`./hex.py -e -f FILE`
