import hashlib
import os
import sys
import contextlib
import logging
from io import StringIO

global h
h = 0

# Logging configuration
logging.basicConfig(filename='hashwolf.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

def generatehash(hash_type, raw):
    with stdoutIO(stdout=None) as s:
        try:
            code = f"""import hashlib
us = hashlib.{hash_type}()
us.update({raw.encode()})
t = us.digest()
print(t)"""
            exec(code)
        except Exception as e:
            logging.error(f"Error in generating hash: {e}")
            print("Error: Something went wrong. Try again or make an issue on GitHub")
    return s.getvalue().strip()

def result(hash_type, hash_to_crack, out, output_file=None):
    msg = f"""Cracked successfully
Hash used: {hash_type}
Hash cracked: {hash_to_crack}
*Hashed: {out}"""
    print(msg)
    logging.info(msg)
    if output_file:
        with open(output_file, "w") as f:
            f.write(msg)
        print(f"Saved to file: {output_file}")
    sys.exit(0)

def direct(hash_type, wordlist, hash_to_crack, output_file=None):
    t = open(wordlist, 'r').read().split("\n")
    for b, word in enumerate(t):
        try:
            r = generatehash(hash_type, word)
            if r == f"b'{hash_to_crack}'":
                result(hash_type, hash_to_crack, word, output_file)
            else:
                print(f"Cracking attempt: {b + 1}")
        except Exception as e:
            logging.error(f"Error during direct cracking: {e}")
            print(f"An error occurred: {e}")
            break
    else:
        print("Wordlist exhausted")
        logging.info("Wordlist exhausted without cracking the hash.")

def compare(hash_type, newPrefix, bytehash, output_file=None):
    strhash = generatehash(hash_type, newPrefix)
    if strhash == f"b'{bytehash}'":
        result(hash_type, bytehash, newPrefix, output_file)
    else:
        global h
        h += 1
        print(f"Cracking attempt: {h}")

def printAllKLengthRec(set, prefix, n, k, hash_type, hash_to_crack, output_file=None):
    if k == 0:
        return
    for i in range(n):
        newPrefix = prefix + set[i]
        compare(hash_type, newPrefix, hash_to_crack, output_file)
        printAllKLengthRec(set, newPrefix, n, k - 1, hash_type, hash_to_crack, output_file)

def indirect(hash_type, hash_to_crack, char_to_use="qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM+×÷=%/\\$€£@*!#:;&_()-'\",.?°¿¡^[]<>~`§μ¬Г´·{}©|¤₹៛₪θฯ1234567890Ω", output_file=None, length=2):
    while True:
        printAllKLengthRec(list(char_to_use), "", len(char_to_use), length, hash_type, hash_to_crack, output_file)

def analyse(hash_type):
    log_path = "logs/rainlogs.txt"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    try:
        with open(log_path, "r") as f:
            if hash_type not in f.read():
                with open(log_path, "a") as fw:
                    fw.write(f"{hash_type}\n")
    except FileNotFoundError:
        with open(log_path, "w") as fw:
            fw.write(f"{hash_type}\n")

def writeout(raw, hash_type, file_idx):
    with open(f"dict/{hash_type}/{file_idx}.txt", "a") as f:
        f.write(raw + "\n")

def generate(set, prefix, n, k, hash_type, file_idx):
    if k == 0:
        return
    for i in range(n):
        newPrefix = prefix + set[i]
        store(newPrefix, hash_type, file_idx)
        generate(set, newPrefix, n, k - 1, hash_type, file_idx)

def store(raw, hash_type, file_idx):
    hashed = generatehash(hash_type, raw)
    writeout(f"{raw}:{hashed}", hash_type, file_idx)

def dictionnary(hash_type, set="qwertzuiopasdfghjklyxcvbnm+×÷=%/\\$€£@*!#:;&_()-'\",.?°¿¡^[]<>~`§μ¬Г´·{}©|¤₹៛₪θฯ1234567890QWERTZUIOPASDFGHJKLYXCVBNM"):
    os.makedirs(f"dict/{hash_type}", exist_ok=True)
    analyse(hash_type)
    prefix = ""
    n = len(set)
    k = 32  # You can adjust this length as needed
    generate(set, prefix, n, k, hash_type, 0)

def rainbow_table(hash_type, hash_to_crack, output_file=None):
    log_path = "logs/rainlogs.txt"
    try:
        with open(log_path, "r") as f:
            if hash_type not in f.read():
                print("Error: Generate a dictionary for this hash type first.")
                return
    except FileNotFoundError:
        print("Error: Rainlogs not found. Generate a dictionary first.")
        return

    # Attempt to crack hash using pre-generated dictionary
    dict_path = f"dict/{hash_type}"
    for file_name in os.listdir(dict_path):
        if file_name.endswith(".txt"):
            with open(os.path.join(dict_path, file_name), "r") as f:
                for line in f:
                    raw, hashed = line.strip().split(":")
                    if hashed == f"b'{hash_to_crack}'":
                        result(hash_type, hash_to_crack, raw, output_file)
                        return
    print("Hash not found in rainbow table.")
    logging.info("Hash not found in rainbow table.")

## Entry point
def start(mode, hash_to_crack, hash_type, wordlist=None, char_to_use="qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM+×÷=%/\\$€£@*!#:;&_()-'\",.?°¿¡^[]<>~`§μ¬Г´·{}©|¤₹៛₪θฯ1234567890Ω", output_file=None):
    if mode == "direct":
        direct(hash_type, wordlist, hash_to_crack, output_file)
    elif mode == "indirect":
        indirect(hash_type, hash_to_crack, char_to_use, output_file)
    elif mode == "dictionary":
        dictionnary(hash_type, char_to_use)
    elif mode == "rainbow":
        rainbow_table(hash_type, hash_to_crack, output_file)
    else:
        print("[#] An error occurred. Please create an issue at github.com/rawbytedev/hashcrack to be helped")
