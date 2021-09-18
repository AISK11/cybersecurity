# base16.py
Decrypts and encrypts Hex To String.\
*Basically base16 encoder and decoder*

### INSTALLATION
1. make sure to have **python3**, **make** and **git** pacakges installed. You can install it with:
* Debian based distros:\
`sudo apt install python3 make git`
1. clone repository:\
`git clone https://github.com/AISK11/cybersecurity`
1. navigate to directory:\
`cd ./cybersecurity/cryptography/base16/`
1. make executable:\
`make`

### Syntax
`usage: base16.py [-h] [-d | -e] [-v | -q] [-t | -f] MESSAGE`

### Examples
* Get help:\
`./base16.py -h`
* Decrypt hex string from stdin\
`./base16.py MESSAGE`\
`./base16.py -d -v -t MESSAGE`
* Decrypt specified file with quiet output:\
`./base16.py -q -f FILE`
* Encrypt specific string from file:\
`./base16.py -e -f FILE`
