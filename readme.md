# HashWolf

This project is a object oriented open source, Software for Windows/Linux made in Python 3 
Hashwolf is an hashcracker design to be user friendly, easy to use, fast and lightweight, it currently have 2/4(direct and indirect) of it available modes(direct, indirect, dictionnary, rainbow)
the other modes will be finished in a week or two after this version publish
This project is lightweight and can be used to crack hash in environment with low storage space but high ram or medium
Hashwolf(library) can be used in other program as it works independly from hashwolf(launcher or main), hashwolf(main) only provide the input needed for hashwolf(library) to work
that's how it is represented:
	`hashwolf.start(mode, hash_type, wordlist, hash_to_crack, char_to_use, output_file)`some input can be left undefined(None) those are char_to_use, output_file, wordlist(for indirect but must be defined for direct mode)

## direct mode
Direct mode of hashwolf is a mode in which hashwolf uses a wordlist provided by user to crack an hash (in ROM)
## indirect mode
indirect mode uses high amount of free ram, it generate a word in ram, hash it then compare instead of generating whole list in memory, which eventually will freeze the device
It tries to use minimal ram

## Installation

You will need:

* [Python 3.6+](https://www.python.org/downloads) (Make sure to add python to PATH during installation)
* A Windows/Linux Computer
* Can be run on terminal emulator such as termux...
* Atleast 800 mb ram free if you intend to use indirect mode

1. Download the repository via github or git eg. `git clone https://github.com/Xnetwolf/hashwolf`
2. No need to install any requirements this project uses pre install modules

## Features

Currently this program crack those hash:

* md5
* sha1
* sha224
* sha256
* sha384
* sha512
* blake2b
* blake2s

## Quick Usage

1. use the following command:
`python main.py -h` and follow the instructions on screen to start you're cracking 
2. Don't forget to inclose the hash to crack between quotes `' '`('{hash}')

example of usage:
`python main.py -a indirect -t md5 -out cracked.txt -hash 'I\xf6\x8a\\\x84\x93\xec,\x0b\xf4\x89\x82\x1c!\xfc;' ` 
you notice the absence of b and presence of quote(' hash ')

## Help

If you need any help at all, feel free to open a "help" issue.

## Error / Bugs

If you find any error, feel free to let me know

## Contribute to this project
buy me a cup of coffee

Bitcoin: `12iuxEDyQtGY2QgD3sHp3KrV363rcsBcMi`
Dogecoin: `DPDuizKPUe8LodMGR9S8S388aKqnTbjWto`
Litecoin: `LZqvfZYXdJr3D7nHQWi9KxW5hL6DaThbnE`
BNB: `0x07A88F71AD5f95F592FFfd3D58306bED55706667`
Polygon: `0x07A88F71AD5f95F592FFfd3D58306bED55706667`
ETH: `0x07A88F71AD5f95F592FFfd3D58306bED55706667`
DGB: `dgb1qvhuw7tddr7hat93365tkj4ee9v8yzd9ghjpe2w`
TRX: `TTLvFFxpDyvvB7rvjVpYDQjeMzRqvwssXo`



## About

Project Created by Rad Taren
My repo:
	https://github.com/Xnetwolf

## Disclaimer

This program is for educational purposes only! I take no responsibility or liability for own personal use.

## Licence 
copyright (c) Rad Taren. All rights reserved.

[license] under MIT(./license)