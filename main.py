#import necessary libs
<<<<<<< Updated upstream
import argparse
from genericpath import isfile
=======
from functools import partial
import argparse
from genericpath import isfile
import sys
>>>>>>> Stashed changes
import os
import logging
import itertools
import string
import multiprocessing
import hashlib

## Banners
def banner():
    print("banner")

# Define default character sets
default_characters = {
 'L': string.ascii_lowercase,
 'U': string.ascii_uppercase,
 'N': string.digits,
 'S': string.punctuation,
 '?': string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
}
<<<<<<< Updated upstream
# Hashing function
def hash_word(word, hashtype):
    # Example using SHA256; you can use other algorithms as needed
    hash_type = hashtype.lower() # Convert to lowercase for consistency
    try:
        hash_object = getattr(hashlib, hash_type)()
    except AttributeError:
        print(f"Invalid hash type: {hash_type}")
    hash_object.update(word)
    ## assignement is not needed here just return hash_object.hexdigest()
    hash_value = hash_object.hexdigest()
    return hash_value

# Wordlist generator function
def wordlist_generator(pattern="L?N", min_length=3, max_length=10, exclude=''):
    for length in range(min_length, max_length + 1):
        for word_tuple in itertools.product(*(default_characters[char] for char in pattern)):
            word = ''.join(word_tuple)
            if len(word) == length and not any(char in word for char in exclude):
                yield word

# Parallel hashing function
def parallel_hashing(word_generator):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Use 'imap' for lazy iteration over the results
        for hashed_word in pool.imap(hash_word, word_generator):
            yield hashed_word
            
=======
times = 0
# Compare function
# customized to suit my needs
#def compare_hash(orig_hashs, target_hash):
def compare_hash(orig_hashs, target_hash):
    global times
    if orig_hashs[0] == target_hash:    
            print(orig_hashs[1])
            open("Working", "w")
            
    else:
        times = times+1
        print(f"Tried {times} times\n")

# Hashing function
def hash_word(word, hashtype):
    # Example using SHA256; you can use other algorithms as needed
    hash_type = hashtype.lower() # Convert to lowercase for consistency
    try:
        hash_object = getattr(hashlib, hash_type)()
    except AttributeError:
        print(f"Invalid hash type: {hash_type}")
    hash_object.update(word.encode('utf-8'))
    ## assignement is not needed here just return hash_object.hexdigest()
    hash_value = hash_object.hexdigest()
    return hash_value, word

# Wordlist generator function
def wordlist_generator(pattern="L?N", min_length=3, max_length=10, exclude=''):
    for length in range(min_length, max_length + 1):
        for word_tuple in itertools.product(*(default_characters[char] for char in pattern)):
            word = ''.join(word_tuple)
            if len(word) == length and not any(char in word for char in exclude):
                yield word
                
# Wordlist read (generator) function
def wordlist_read(files_list):
    for i in files_list:
        for words in open(i, "r").readlines():
            yield words.strip()
            
# Parallel hashing function
def parallel_hashing(word_generator, hashtype):
    partial_hash_word = partial(hash_word, hashtype=hashtype)
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Use 'imap' for lazy iteration over the results
        for hashed_word, word in pool.imap(partial_hash_word,word_generator):
            yield hashed_word, word
    
>>>>>>> Stashed changes
## Analyse input and check errors
def analyse(args):
    print(args)
    ## Crack Mode
    ## direct-hashtype-hashed-wordlist(default) or direct-hashtype-hashed-wordlist-output
<<<<<<< Updated upstream
    if args.mode == "direct":
        if args.type != None:
            if args.hashed != None:
                args.hashed = analyse_hashed(args.hashed)
                if args.wordlist != None:
                    args.wordlist = analyse_wordlist(args.wordlist)
                    
    
    ## indirect-hashtype-hashed-charact(default) or indirect-hashtype-hashed-charact-output
    if args.mode == "indirect":
        if args.type != None:
            if args.hashed != None:
                args.hashed = analyse_hashed(args.hashed)
                if args.charact != None:
                    args.charact = analyse_charact(args.wordlist)
                    
    ## Generate mode
    if args.mode == "Gendict":
        if args.type != None:
            if args.hashed != None or args.hashed ==None:
                args.hashed = None
                if args.charact != None and args.wordlist == None:
                    args.charact = analyse_charact(args.charact)
                if args.charact == None and args.wordlist != None:
                    args.wordlist = analyse_wordlist(args.wordlist)
    """
    # Create a generator for the wordlist
 words_to_hash = wordlist_generator('L?N', 3, 3, 'aeiou')
 
 # Process each hashed word as it's generated
 for hashed_word in parallel_hashing(words_to_hash):
 print(hashed_word)
 # Include a condition to break the loop if necessary

    """
## Take a parameter determine whether the file is a wordlist or a path to multiple wordlists, it then extract all words from the list
## I should optimize this part later on to make more memory friendly
# as of now all the words are store in memory for processing    
def analyse_wordlist(wordlist):
    words = []
    f = open(wordlist,"r").readlines()
    size = f.__len__() - 1
    for i in f:
        a = i.strip()
        if open(a):
            print("hi")
        else:
            print("bye")
    return 
=======
    ## indirect-hashtype-hashed-charact(default) or indirect-hashtype-hashed-charact-output
    ## wordlist
    ## hashed
    ## charact
    
## Please don't provide a file of mixed path and words    
def analyse_item(input_path, result=None):
    if result is None:
        result = []
    if os.path.isfile(input_path):
        with open(input_path, 'r') as file:
            content = file.readlines()
 
        # Check each line in the file for file paths
        for line in content:
            line = line.strip()
            if os.path.isfile(line):
                result.extend([True, input_path])
                analyse_item(line, result)
            else:
                result.extend([False, input_path])
    else:
        # If the input is not a file path, return False and the input
        result = [False, input_path]
 
    return result

## Sanitize data so it can be used by program more easily
def sanitize(original_list):
    # Use list comprehension to pair each boolean with the subsequent item
    tuple_list = [(original_list[i], original_list[i + 1]) for i in range(0, len(original_list), 2)]
    unique_list = []
    for item in tuple_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

## Function to output results
def output(result,filepath):
    open(filepath, "r").append(result)
>>>>>>> Stashed changes
## Handle inputs
#Initilise
p = argparse.ArgumentParser()
#argument list
## -c or --crack to define cracking process to use
<<<<<<< Updated upstream
p.add_argument('-m', '--mode', help="",default="direct")
## The hash type or hashing algorithm to use.eg:md5, sha1
p.add_argument('-t', '--type', help="", required=True)
=======
p.add_argument("-m",'--mode',choices=["direct","indirect","Gendict"], help="",default="direct")
## The hash type or hashing algorithm to use.eg:md5, sha1
p.add_argument('-t', '--type', help="")
>>>>>>> Stashed changes
## The hash that needs to be cracked
p.add_argument('-hash', '--hashed', help="")
## The set of characters to use
p.add_argument('-char', '--charact', help="")
## The wordlist to use for the cracking process
p.add_argument('-w','--wordlist', help="")
## The file were the result will be saved
p.add_argument('-o', '--output', help="")
## minimun lenght
p.add_argument('-min','--minlenght', help="")
## maximun lenght
p.add_argument('-max', '--maxlenght', help="")
## The verbose level

#p.add_argument('-v','--verbose', help="Verbose", action="store_true")
#p.add_argument('-d', '--debug', help="Print debugging statements", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.WARNING)
args = p.parse_args()
#logging.basicConfig(level=args.loglevel)

#ver_inp(args)

def main():
    # banner()
    #analyse(args)
<<<<<<< Updated upstream
    analyse_wordlist("test.txt")
    #logging.info("Message")
    
=======
    ## Hashword
    #print(hash_word("Hello", "md5"))
    ## Generator wordlist
    #for words in wordlist_generator():
        #print(words)
    ## Generator Files
    #for words in wordlist_read(["test.txt"]):
     #   print(words)
    save = open("start","a")
    word = wordlist_generator()
    for hashes in parallel_hashing(word, "md5"):
        compare_hash(hashes,"16636a84a876abfbe4105bb63cbdeb07")
    
    """for hashes in parallel_hashing(words, "md5"):
        save.writelines(hashes+"\n")
    print(sanitize(analyse_item("test.txt")))
    #logging.info("Message")
    """
>>>>>>> Stashed changes

if __name__=="__main__":
    main()
