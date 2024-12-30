import hashlib
import os
import sys
import contextlib
import logging
from io import StringIO

global attempt_count
attempt_count = 0

# Logging configuration
logging.basicConfig(filename='hashwolf.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Context manager to capture stdout
@contextlib.contextmanager
def capture_stdout(stdout=None):
    old_stdout = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old_stdout

# Generate the hash using the specified hash type and raw input
def generate_hash(hash_type, raw):
    with capture_stdout(stdout=None) as s:
        try:
            code = f"""import hashlib
hasher = hashlib.{hash_type}()
hasher.update({raw.encode()})
hashed_output = hasher.hexdigest()
print(hashed_output)"""
            exec(code)
        except Exception as e:
            logging.error(f"Error in generating hash: {e}")
            print("Error: Something went wrong. Try again or report the issue on GitHub")
    return s.getvalue().strip()

# Print the result and exit the program
def display_result(hash_type, hash_to_crack, cracked_word, output_file=None):
    message = f"""Cracked successfully
Hash type: {hash_type}
Hash to crack: {hash_to_crack}
Original word: {cracked_word}"""
    print(message)
    logging.info(message)
    if output_file:
        with open(output_file, "w") as f:
            f.write(message)
        print(f"Results saved to file: {output_file}")
    sys.exit(0)

# Direct hash cracking using a wordlist
def direct_crack(hash_type, wordlist, hash_to_crack, output_file=None):
    words = open(wordlist, 'r').read().split("\n")
    for attempt, word in enumerate(words):
        try:
            generated_hash = generate_hash(hash_type, word)
            if generated_hash == hash_to_crack:
                display_result(hash_type, hash_to_crack, word, output_file)
            else:
                print(f"Attempt: {attempt + 1}")
        except Exception as e:
            logging.error(f"Error during direct cracking: {e}")
            print(f"An error occurred: {e}")
            break
    else:
        print("Wordlist exhausted")
        logging.info("Wordlist exhausted without cracking the hash.")

# Compare the generated hash with the target hash
def compare_hashes(hash_type, current_word, target_hash, output_file=None):
    generated_hash = generate_hash(hash_type, current_word)
    if generated_hash == target_hash:
        display_result(hash_type, target_hash, current_word, output_file)
    else:
        global attempt_count
        attempt_count += 1
        print(f"Attempt: {attempt_count}")

# Generate all possible combinations of characters recursively
def recursive_combinations(charset, prefix, charset_length, remaining_length, hash_type, target_hash, output_file=None):
    if remaining_length == 0:
        return
    for i in range(charset_length):
        new_prefix = prefix + charset[i]
        compare_hashes(hash_type, new_prefix, target_hash, output_file)
        recursive_combinations(charset, new_prefix, charset_length, remaining_length - 1, hash_type, target_hash, output_file)

# Indirect hash cracking by generating all possible combinations of characters
def indirect_crack(hash_type, target_hash, charset="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM+×÷=%/\\$€£@*!#:;&_()-'\",.?°¿¡^[]<>~`§μ¬Г´·{}©|¤₹៛₪θฯ1234567890Ω", output_file=None, length=2):
    while True:
        recursive_combinations(list(charset), "", len(charset), length, hash_type, target_hash, output_file)

# Analyze and log the hash type
def log_hash_type(hash_type):
    log_path = "logs/hash_logs.txt"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    try:
        with open(log_path, "r") as f:
            if hash_type not in f.read():
                with open(log_path, "a") as fw:
                    fw.write(f"{hash_type}\n")
    except FileNotFoundError:
        with open(log_path, "w") as fw:
            fw.write(f"{hash_type}\n")

# Write the raw word and its hash to a file
def write_to_file(raw, hash_type, file_idx):
    with open(f"dict/{hash_type}/{file_idx}.txt", "a") as f:
        f.write(raw + "\n")

# Generate combinations and store them in the dictionary
def generate_combinations(charset, prefix, charset_length, remaining_length, hash_type, file_idx):
    if remaining_length == 0:
        return
    for i in range(charset_length):
        new_prefix = prefix + charset[i]
        store_combination(new_prefix, hash_type, file_idx)
        generate_combinations(charset, new_prefix, charset_length, remaining_length - 1, hash_type, file_idx)

# Store the raw word and its hash in the dictionary
def store_combination(raw, hash_type, file_idx):
    hashed = generate_hash(hash_type, raw)
    write_to_file(f"{raw}:{hashed}", hash_type, file_idx)

# Create a dictionary of hashes for the given hash type
def create_hash_dictionary(hash_type, charset="qwertyuiopasdfghjklzxcvbnm+×÷=%/\\$€£@*!#:;&_()-'\",.?°¿¡^[]<>~`§μ¬Г´·{}©|¤₹៛₪θฯ1234567890QWERTYUIOPASDFGHJKLZXCVBNM"):
    os.makedirs(f"dict/{hash_type}", exist_ok=True)
    log_hash_type(hash_type)
    prefix = ""
    charset_length = len(charset)
    max_length = 32  # You can adjust this length as needed
    generate_combinations(charset, prefix, charset_length, max_length, hash_type, 0)

# Crack the hash using a pre-generated rainbow table
def rainbow_crack(hash_type, target_hash, output_file=None):
    log_path = "logs/hash_logs.txt"
    try:
        with open(log_path, "r") as f:
            if hash_type not in f.read():
                print("Error: Generate a dictionary for this hash type first.")
                return
    except FileNotFoundError:
        print("Error: Hash logs not found. Generate a dictionary first.")
        return

    dict_path = f"dict/{hash_type}"
    for file_name in os.listdir(dict_path):
        if file_name.endswith(".txt"):
            with open(os.path.join(dict_path, file_name), "r") as f:
                for line in f:
                    raw, hashed = line.strip().split(":")
                    if hashed == target_hash:
                        display_result(hash_type, target_hash, raw, output_file)
                        return
    print("Hash not found in rainbow table.")
    logging.info("Hash not found in rainbow table.")

# Entry point for the program
def start(mode, hash_to_crack, hash_type, wordlist=None, charset="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM+×÷=%/\\$€£@*!#:;&_()-'\",.?°¿¡^[]<>~`§μ¬Г´·{}©|¤₹៛₪θฯ1234567890Ω", output_file=None):
    if mode == "direct":
        direct_crack(hash_type, wordlist, hash_to_crack, output_file)
    elif mode == "indirect":
        indirect_crack(hash_type, hash_to_crack, charset, output_file)
    elif mode == "dictionary":
        create_hash_dictionary(hash_type, charset)
    elif mode == "rainbow":
        rainbow_crack(hash_type, hash_to_crack, output_file)
    else:
        print("[#] An error occurred. Please create an issue at github.com/rawbytedev/hashcrack to be helped")
