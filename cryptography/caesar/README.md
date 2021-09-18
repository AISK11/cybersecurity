# caesar.py
Decrypts and encrypts Caesar cipher.

### INSTALLATION
1. make sure to have **python3**, **make** and **git** pacakges installed. You can install it with:
* Debian based distros:\
`sudo apt install python3 make git`
1. clone repository:\
`git clone https://github.com/AISK11/cybersecurity`
1. navigate to directory:\
`cd ./cybersecurity/cryptography/caesar/`
1. make executable:\
`make`

### Syntax
`./caesar.py [-h] [-d | -e] [-s SHIFT] [-u] [-l] [-v | -q] [-t | -f] MESSAGE`

### Examples
* Get help:\
`./caesar.py -h`
* Decrypt string with default letter shift by 3:\
`./caesar.py MESSAGE`\
`./caesar.py -d -s 3 -v -t MESSAGE`
* Decrypt specified file by all possible letter shift with quiet output:\
`./caesar.py -s 0-25 -q -f FILE`
* Encrypt specified file by 11 and 14 letter shift with letters only in uppercase:\
`./caesar.py -e -s 11,14 -u -l -f FILE`
