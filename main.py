import argparse
import os
import hashwolf
import logging

# Logging configuration
logging.basicConfig(filename='hashwolf.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def banner():
    print("HashCrack")

def entry_point(ar):
    banner()
    scan_input(ar)

def scan_input(ar):
    if ar.attack == "direct":
        print("direct")
        try:
            open(ar.wordlist, "r")
        except FileNotFoundError:
            print("""[#] An error occured while trying to use wordlist
The causes of the error are listed:
- File doesn't exist
- Hashwolf doesn't have permission to read file
- Wrong path

Try again later. If the problem isn't solved, make an issue on GitHub with your log files""")
        else:
            print("## Wordlist verified")

    elif ar.attack == "rainbow":
        try:
            with open("logs/rainlogs.txt", "r") as re:
                if ar.type in re.read():
                    print("## Rainbow dictionary verified")
                else:
                    print("Error: Generate a dictionary before starting")
        except FileNotFoundError:
            print("Error: Rainlogs not found. Generate a dictionary first.")

    print("Attack starting ")
    print(f"""
    Note: None == Default
Mode: {ar.attack}
Hash_Type: {ar.type}
Wordlist: {ar.wordlist}
Hash to crack: {ar.hashed}
Characters to use: {ar.character}
Output file: {ar.output}
""")

    # Use hashwolf to start attack
    if ar.character is None:
        hashwolf.start(ar.attack, ar.hashed, ar.type, ar.wordlist, output_file=ar.output)
    else:
        hashwolf.start(ar.attack, ar.hashed, ar.type, ar.wordlist, ar.character, ar.output)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('-a', '--attack', required=True, help="""You have 4 modes: direct, indirect, rainbows, rainbow

* direct cracking uses a wordlist provided by user, hashwolf uses threading to be fast.

* indirect cracks without wordlist, uses threading and efficient techniques to generate and hash words.

* rainbows generates hash dictionaries for later use, storing them in a predefined location.

* rainbow cracking uses pre-generated dictionaries for fast and effective cracking by avoiding unnecessary searching.""")
    p.add_argument('-t', '--type', help="Specify the hash type to crack (e.g., -hash md5, -hash sha256)", required=True)
    p.add_argument('-w', '--wordlist', help="Path to the wordlist for direct cracking mode")
    p.add_argument('-hash', '--hashed', help="The hash you want to crack")
    p.add_argument('-o', '--output', help="Path to the file where cracking results will be saved")
    p.add_argument('-c', '--character', help="Characters to generate wordlist for indirect or dictionary mode; default will be used if not specified")

    ar = p.parse_args()
    entry_point(ar)
