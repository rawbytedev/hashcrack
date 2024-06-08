#import necessary libs
import argparse
from genericpath import isfile
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
            
## Analyse input and check errors
def analyse(args):
    print(args)
    ## Crack Mode
    ## direct-hashtype-hashed-wordlist(default) or direct-hashtype-hashed-wordlist-output
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
## Handle inputs
#Initilise
p = argparse.ArgumentParser()
#argument list
## -c or --crack to define cracking process to use
p.add_argument('-m', '--mode', help="",default="direct")
## The hash type or hashing algorithm to use.eg:md5, sha1
p.add_argument('-t', '--type', help="", required=True)
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
    analyse_wordlist("test.txt")
    #logging.info("Message")
    

if __name__=="__main__":
    main()
