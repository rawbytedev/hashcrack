import argparse
import os
import hashwolf
import logging

# Logging configuration
logging.basicConfig(filename='hashcrack.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def entry_point(arguments):
    validate_input(arguments)

def validate_input(arguments):
    if arguments.attack == "direct":
        print("Attempting direct attack mode...")
        try:
            open(arguments.wordlist, "r")
        except FileNotFoundError:
            print("""Error: Unable to use the specified wordlist.
Possible reasons:
- The file does not exist.
- Insufficient permissions to read the file.
- Incorrect file path provided.

Please check the wordlist file and try again. If the issue persists, report it on GitHub with your log files.""")
        else:
            print("## Wordlist verified successfully")

    elif arguments.attack == "rainbow":
        try:
            with open("logs/hash_logs.txt", "r") as log_file:
                if arguments.type in log_file.read():
                    print("## Rainbow dictionary verified successfully")
                else:
                    print("Error: Dictionary for the specified hash type not found. Generate the dictionary before starting the attack.")
        except FileNotFoundError:
            print("Error: Hash logs not found. Generate a dictionary first before attempting rainbow cracking.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("Starting attack...")
    print(f"""
Note: None == Default
Mode: {arguments.attack}
Hash Type: {arguments.type}
Wordlist: {arguments.wordlist}
Hash to crack: {arguments.hashed}
Characters to use: {arguments.character}
Output file: {arguments.output}
""")

    # Use hashwolf to start attack
    if arguments.character is None:
        hashwolf.start(arguments.attack, arguments.hashed, arguments.type, arguments.wordlist, output_file=arguments.output)
    else:
        hashwolf.start(arguments.attack, arguments.hashed, arguments.type, arguments.wordlist, arguments.character, arguments.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--attack', required=True, help="""Select attack mode: direct, indirect, rainbow, or rainbow table.

* direct: Uses a wordlist provided by the user for cracking.
* indirect: Generates and hashes words without a wordlist.
* dictionary: Generates hash dictionaries for future use.
* rainbow table: Uses pre-generated dictionaries for efficient cracking.""")
    parser.add_argument('-t', '--type', required=True, help="Specify the hash type to crack (e.g., md5, sha256).")
    parser.add_argument('-w', '--wordlist', help="Path to the wordlist for direct cracking mode.")
    parser.add_argument('-hash', '--hashed', help="The hash value you want to crack.")
    parser.add_argument('-o', '--output', help="Path to the file where cracking results will be saved.")
    parser.add_argument('-c', '--character', help="Characters to generate wordlist for indirect or dictionary mode; default will be used if not specified.")

    arguments = parser.parse_args()
    entry_point(arguments)
