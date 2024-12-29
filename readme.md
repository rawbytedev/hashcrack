# HashCrack

HashCrack is a versatile and powerful hash cracking tool designed for various attack modes, including direct, indirect, dictionary, and rainbow table attacks. Developed by rawbytedev, HashCrack leverages threading to achieve high performance and supports multiple hash types for a wide range of use cases.

## Features

- **Direct Attack**: Uses a user-provided wordlist to crack the hash efficiently.
- **Indirect Attack**: Generates potential passwords without a wordlist, using threading and optimized techniques.
- **Dictionary Generation**: Generates all possible combinations of given characters up to a specified length and stores the hash values in files.
- **Rainbow Table Attack**: Uses pre-generated dictionaries to crack hashes efficiently.
- **Logging**: Detailed logging of operations and errors for easy debugging and monitoring.
- **Cross-Platform Compatibility**: Works on both Unix-like systems and Windows.

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/rawbytedev/hashcrack.git
   cd hashwolf
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. If not, download and install Python from [python.org](https://www.python.org/).

## Usage

### Command-Line Interface

HashWolf provides a command-line interface for ease of use. Below are the available options and their descriptions:

```sh
usage: main.py [-h] -a ATTACK -t TYPE [-w WORDLIST] [--hash HASHED] [-o OUTPUT] [-c CHARACTER]

options:
  -h, --help            show this help message and exit
  -a, --attack ATTACK   Choose from 4 modes: direct, indirect, rainbows, rainbow.
  -t, --type TYPE       Specify the hash type to crack (e.g., md5, sha256).
  -w, --wordlist WORDLIST
                        Path to the wordlist for direct cracking mode.
  --hash HASHED         The hash you want to crack.
  -o, --output OUTPUT   Path to the file where cracking results will be saved.
  -c, --character CHARACTER
                        Characters to generate wordlist for indirect or dictionary mode.
```

### Example Usage

#### Direct Attack

```sh
python main.py -a direct -t md5 -w /path/to/wordlist.txt --hash d41d8cd98f00b204e9800998ecf8427e -o results.txt
```

#### Indirect Attack

```sh
python main.py -a indirect -t sha256 --hash e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -c "abcdef123"
```

#### Dictionary Generation

```sh
python main.py -a dictionary -t sha1 -c "abc123"
```

#### Rainbow Table Attack

```sh
python main.py -a rainbow -t md5 --hash d41d8cd98f00b204e9800998ecf8427e -o results.txt
```

## Logging

HashWolf logs all operations and errors in `hashwolf.log`. This log file provides detailed information about the execution flow and helps in debugging issues.

## Contributions

Contributions are welcome! If you have suggestions, bug reports, or improvements, feel free to create an issue or submit a pull request on GitHub.

## License

HashWolf is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contact

For any questions or support, please create an issue on GitHub