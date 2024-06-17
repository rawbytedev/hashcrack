# HashCrack

This project is an object oriented open source, Software for Windows/Linux made in Python 3 

## Installation

You will need:

* [Python 3.6+](https://www.python.org/downloads) (Make sure to add python to PATH during installation)
* A Windows/Linux Computer
1. Download the repository via github or git eg. `git clone https://github.com/rawbytedev/Hashcrack`
2. install the required modules by running `python -m pip install -r requirements.txt`

## Features

#### Flexibility

*  Work with multiple wordlist at once
- Work with multiple wordlist of hashes(in hexadecimal)

- Custom patterns with lenght constraints 

#### Object Oriented

- Can be used in another project

- Documentation of [HashCrack](https://github.com/HashCrack/docs/index.md) 

#### Supported Hashes

Support all the hashes provided by hashlib library

#### Memory Friendly

Most of the functions depends upon disk(speed) and cpu, the usage of memory is limited and is only used to stored data needed for processing. For memory comsumption process like generation of words, Generators is used instead of holding entire list in memory 

- Optimizing Character Sets

- Reducing Redundant Combinations

- Pattern Matching

#### MultiProcessing

The use multiprocessing based hash generator increase efficiency

Hashing is a task that depend hightly on the cpu that's why multiprocessing is used here, that way it uses all the cores availbale for the hashing process

#### 

## Quick Usage

1. Run `main.py` and follow the instructions on screen 

## Help

If you need any help at all, feel free to open a "help" issue.

## Error / Bugs

Please if you enconteer an error while using it, feel free to open an issue

## About

Project Created by rawbytedev(Aren)
My repo: [rawbytedev](https://github.com/rawbytedev)

## Disclaimer

This program is for educational purposes only! I take no responsibility or liability for own personal use.

## Licence

copyright (c) Aren. All rights reserved.

[license] under MIT(./license)
