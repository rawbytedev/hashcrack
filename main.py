#import necessary libs
from functools import partial
import argparse
from genericpath import isfile
import sys
import os
import logging
import itertools
import string 
import multiprocessing
import hashlib
import time

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
times = 0
# Compare function
# customized to suit my needs
#def compare_hash(orig_hashs, target_hash):
def compare_hash(orig_hashs, target_hash):
    global times
    if orig_hashs[0] == target_hash:    
           return True, orig_hashs[0], orig_hashs[1]
    else:
        times = times+1
        print(f"Tried {times} times")

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
 # Assuming default_characters is defined elsewhere
    for length in range(min_length, max_length + 1):
        for word_tuple in itertools.product(*(default_characters[char] for char in pattern)):
            word = ''.join(word_tuple)
            if not any(char in word for char in exclude):
                yield word

                
# Wordlist read (generator) function
def wordlist_read(files_list):
    for is_true, item in files_list:
        if not is_true:
        # Handle the case where the boolean is True
            for words in open(item, "r").readlines():
                    yield words.strip()    
            
# Parallel hashing function
def parallel_hashing(word_generator, hashtype):
    partial_hash_word = partial(hash_word, hashtype=hashtype)
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:

        # Use 'imap' for lazy iteration over the results
        for hashed_word, word in pool.imap(partial_hash_word,word_generator):
            if hashed_word is None:
                break # Stop the loop if the stop event is set
            yield hashed_word, word
      
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

## Sanitize inputs(This test the inputs and return error if they're unusable)
def san_input(args):
    gen_mode = False
    wordlist = False
    pattern = False
    output = False
    htype = None
    if (args.mode == "Gendict" ):
        if args.hashed != None:
            print("1 You can't do that")
        gen_mode = True
            #exit()
    if args.hashed == None and gen_mode == False:
        print("2 You can't do that")
    if args.wordlist != None and args.pattern != None:
        print("3 Please check you're input first")
        ## Ends here
    if args.wordlist != None:
      try: 
           open(args.wordlist, "r")
           wordlist = True
      except:
           print("4 Unable to use file")
    if args.pattern != None:
      for char in args.pattern:
           if char not in default_characters:
               print("5 Please refer to the documentation when using pattern")
           else:
               pattern = True
    if args.output != None:
      try: 
         open(args.output, "w")
         output = True
      except:
         print("6 Unable to use file")
    if pattern == True:
        
        try:
            if int(args.minlenght) > int(args.maxlenght):
                print("7 lenght aren't consistent")
        except:
            print("7-1 excepting integer")
        # End
    if pattern == True:
      while len(args.pattern)<int(args.minlenght):
            args.pattern = args.pattern+"?"
            print("8 Using default lenghts")
    if args.type != None:
        hash_type = args.type.lower() # Convert to lowercase for consistency
        try:
            getattr(hashlib, hash_type)()
            htype = True
        except AttributeError:
            print(f"Invalid hash type: {hash_type}")
    if args.type == None:
        print("Please specifie the hash type to use")
            
    return gen_mode, wordlist, pattern, output, htype
def st_crack(gene=False):
    if gene == False:
        for hashes in parallel_hashing(wordlist_read(sanitize(analyse_item(args.wordlist))), args.type):
            try:
                ## hashes, target_hash
                a = compare_hash(hashes,args.hashed)
                if a[0] == True:
                    print(f"{a[1]} : {a[2]}")
                    return None ## to stop all the multipocessing
            except Exception as e:
                print("",end="")
    else:
        for lenght in range(int(args.minlenght), int(args.maxlenght)+1):
            if len(args.pattern)<lenght:
                args.pattern = args.pattern+"?"
                word = wordlist_generator(args.pattern,lenght,int(args.maxlenght))
            else:
                word = wordlist_generator(args.pattern,lenght,int(args.maxlenght))
            for hashes in parallel_hashing(word, args.type):
                try:
                    ## hashes, target_hash
                    a = compare_hash(hashes,args.hashed)
                    if a[0] == True:
                        print(f"{a[1]} : {a[2]}")
                        return None ## to stop all the multipocessing
                except Exception as e:
                        print("",end="")
                
def genedict(gene=False):
    if gene == False:
        for hashes in parallel_hashing(wordlist_read(sanitize(analyse_item(args.wordlist))), args.type):
            try:
                print(f"{hashes[0]} : {hashes[1]}")
            except Exception as e:
                print("",end="")
    else:
        for lenght in range(int(args.minlenght), int(args.maxlenght)+1):
            if len(args.pattern)<lenght:
                args.pattern = args.pattern+"?"
                word = wordlist_generator(args.pattern,lenght,int(args.maxlenght))
            else:
                word = wordlist_generator(args.pattern,lenght,int(args.maxlenght))
            for hashes in parallel_hashing(word, args.type):
                try:
                    ## hashes, target_hash
                    print(f"{hashes[0]} : {hashes[1]}")
                except Exception as e:
                        print("",end="")
## Analyse input check errors launch other functions accordinaly
def Manager(args):
    #
    tests = san_input(args)
    print(tests)
    if tests[0] == False:
        if tests[1] == True:
            st_crack()
        else:
            if tests[2] == True:
                st_crack(gene=True)
    else:
         if tests[1] == True:
             genedict()
         else:
            if tests[2] == True:
                genedict(gene=True)
## Handle inputs
#Initilise
p = argparse.ArgumentParser()
#argument list
## -c or --crack to define cracking process to use
p.add_argument("-m",'--mode',choices=["direct","indirect","Gendict"], help="")
## The hash type or hashing algorithm to use.eg:md5, sha1
p.add_argument('-t', '--type', help="")
## The hash that needs to be cracked
p.add_argument('-hash', '--hashed', help="")
## The wordlist to use for the cracking process
p.add_argument('-w','--wordlist', help="")
## The file were the result will be saved
p.add_argument('-o', '--output', help="")
## minimun lenght
p.add_argument('-min','--minlenght', help="")
## maximun lenght
p.add_argument('-max', '--maxlenght', help="")
## pattern to use
p.add_argument('-p', '--pattern', help="")
##
## The verbose level

#p.add_argument('-v','--verbose', help="Verbose", action="store_true")
#p.add_argument('-d', '--debug', help="Print debugging statements", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.WARNING)
args = p.parse_args()
#logging.basicConfig(level=args.loglevel)

#ver_inp(args)
def hi():
    print(args)
    
def main():
    Manager(args)
    # banner()
    #analyse(args)
    ### Hash a word
    #print(hash_word("aT9", "md5"))
    ### Word generator
    #for word in wordlist_generator("L?", min_length=2, max_length=3):
     #   print(word)
    ### Word
    
    ### Hash Generetor2
    """minl =5
    maxl =10
    for length in range(minl, maxl+1):
        print(length)
    """
    """
    save = open("start.txt", "a")
    ## sanitize to remove duplicates, analyse_item to get all files
    word = wordlist_generator()
    for hashes in parallel_hashing(word, "md5"):
        try:
            print(hashes[0]) ## Hash
            print(hashes[1]) ## Word
        except:
            print("1")
            return None
    """
    ### Hash Generator1
    """
    save = open("start.txt", "a")
    ## sanitize to remove duplicates, analyse_item to get all files
    word = wordlist_read(sanitize(analyse_item("test.txt")))
    for hashes in parallel_hashing(word, "md5"):
        try:
            print(hashes[0]) ## Hash
            print(hashes[1]) ## Word
        except:
            print("1")
    """
    ### Generator, direct with good cracking
    """
    save = open("start", "a")
    ## sanitize to remove duplicates, analyse_item to get all files
    word = wordlist_read(sanitize(analyse_item("test.txt")))
    for hashes in parallel_hashing(word, "md5"):
        try:
            ## hashes, target_hash
            a = compare_hash(hashes,"16636a84a876abfbe4105bb63cbdeb07")
            if a[0] == True:
                print(a[1]) ## Hash
                print(a[2]) ## Word
                return None ## to stop all the multirpocessing
        except:
            print("1")
     """
    ### Generator, indirect with good cracking
    """        
    save = open("start","a")
    word = wordlist_generator()
    for hashes in parallel_hashing(word, "md5"):
        try:
            ## hashes, target_hash
            a = compare_hash(hashes,"16636a84a876abfbe4105bb63cbdeb07")
            if a[0] == True:
                print(a[1]) ## Hash
                print(a[2]) ## Word
                return None ## to stop all the multirpocessing
        except:
            print("1")
     """

if __name__=="__main__":
    main()
