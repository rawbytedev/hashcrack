
import hashlib
import sys
import os

__author__="Rad Taren(radiationbolt@gmail.com)"
__doc__ = """
hashwolf module - A hash cracker interface
supported hash:
	md5, sha1, sha224, sha256, sha384, sha512, blake2b, blake2s

chash - hash to crack
wordlist - path to wordlist

whathash(chash, wordlist) - find what kind of hash chash is then crack it : not available for now
example:
	wordlist contains: 
	hi
	bye 
	hello
   >>> import hashlib
   >>> h = hashlib.md5()
   >>> h.update("hello")

   >>> import hashwolf
   >>> hash = h.digest()
   >>> print(hash)


b']A@*\xbcK*v\xb9q\x9d\x91\x10\x17\xc5\x92'


>>> hashwolf.md5(hash, wordlist)
cracking attempt: 1
cracking attempt: 2

hash used md5

hash found

hash = b']A@*\xbcK*v\xb9q\x9d\x91\x10\x17\xc5\x92'

hexdecimal = '5d41402abc4b2a76b9719d911017c592'

hashed = hello

"""

# md5 hash crack 
def md5(hash, wordlist):
	
	try: # check if file really exist
		r = open(wordlist,"r").read().split("\n")
	except: # prompt error message
		print("please provide a wordlist")
		print("exiting")
		sys.exit() # exit program
	a = "1" # variable
	loop = 0 # variable
	
	#this is a very simple way to compare hash
	while "1" == a:
		ush = hashlib.md5() # hash object
		try:
			ush.update(r[loop].encode()) # try to hash the word
		except: # error (IndexError)
			print("file empty or wordlist exhausted") # prompt error
			sys.exit() # exit
		if ush.digest() == hash: #condition
		   	a = "4" # change a variable
		   	print(f"""
			hash used: md5
			hash found
hash: {ush.digest()}
hexdecimal: {ush.hexdigest()}
hashed: {r[loop]}
	
	""") # print what user need to know
		else:
		   	os.system("clear")
		   	print(f"""
cracking attempt: {loop +1}
""") # let user know 
		   	loop = loop + 1 
		   	
#sha1 hash crack
def sha1(hash, wordlist):
	try: # check if file really exist
		r = open(wordlist,"r").read().split("\n")
	except: # prompt error message
		print("please provide a wordlist")
		print("exiting")
		sys.exit() # exit program
	a = "1" # variable
	loop = 0 # variable
	
	#this is a very simple way to compare hash
	while "1" == a:
		ush = hashlib.sha1() # hash object
		try:
			ush.update(r[loop].encode()) # try to hash the word
		except: # error (IndexError)
			print("file empty or wordlist exhausted") # prompt error
			sys.exit() # exit
		if ush.digest() == hash: #condition
		   	a = "4" # change a variable
		   	print(f"""
			hash used: sha1
			hash found
hash: {ush.digest()}
hexdecimal: {ush.hexdigest()}
hashed: {r[loop]}
	
	""") # print what user need to know
		else:
		   	os.system("clear")
		   	print(f"""
cracking attempt: {loop +1}
""") # let user know 
		   	loop = loop + 1   	

#sha224 hash crack
def sha224(hash, wordlist):
	try: # check if file really exist
		r = open(wordlist,"r").read().split("\n")
	except: # prompt error message
		print("please provide a wordlist")
		print("exiting")
		sys.exit() # exit program
	a = "1" # variable
	loop = 0 # variable
	
	#this is a very simple way to compare hash
	while "1" == a:
		ush = hashlib.sha224() # hash object
		try:
			ush.update(r[loop].encode()) # try to hash the word
		except: # error (IndexError)
			print("file empty or wordlist exhausted") # prompt error
			sys.exit() # exit
		if ush.digest() == hash: #condition
		   	a = "4" # change a variable
		   	print(f"""
			hash used: sha224
			hash found
hash: {ush.digest()}
hexdecimal: {ush.hexdigest()}
hashed: {r[loop]}
	
	""") # print what user need to know
		else:
		   	os.system("clear")
		   	print(f"""
cracking attempt: {loop +1}
""") # let user know 
		   	loop = loop + 1 
#sha256 hash crack
def sha256(hash, wordlist):
	try: # check if file really exist
		r = open(wordlist,"r").read().split("\n")
	except: # prompt error message
		print("please provide a wordlist")
		print("exiting")
		sys.exit() # exit program
	a = "1" # variable
	loop = 0 # variable
	
	#this is a very simple way to compare hash
	while "1" == a:
		ush = hashlib.sha256() # hash object
		try:
			ush.update(r[loop].encode()) # try to hash the word
		except: # error (IndexError)
			print("file empty or wordlist exhausted") # prompt error
			sys.exit() # exit
		if ush.digest() == hash: #condition
		   	a = "4" # change a variable
		   	print(f"""
			hash used: sha256
			hash found
hash: {ush.digest()}
hexdecimal: {ush.hexdigest()}
hashed: {r[loop]}
	
	""") # print what user need to know
		else:
		   	os.system("clear")
		   	print(f"""
cracking attempt: {loop +1}
""") # let user know 
		   	loop = loop + 1 
#sha384 hash crack
def sha384(hash, wordlist):
	try: # check if file really exist
		r = open(wordlist,"r").read().split("\n")
	except: # prompt error message
		print("please provide a wordlist")
		print("exiting")
		sys.exit() # exit program
	a = "1" # variable
	loop = 0 # variable
	
	#this is a very simple way to compare hash
	while "1" == a:
		ush = hashlib.sha384() # hash object
		try:
			ush.update(r[loop].encode()) # try to hash the word
		except: # error (IndexError)
			print("file empty or wordlist exhausted") # prompt error
			sys.exit() # exit
		if ush.digest() == hash: #condition
		   	a = "4" # change a variable
		   	print(f"""
			hash used: sha384
			hash found
hash: {ush.digest()}
hexdecimal: {ush.hexdigest()}
hashed: {r[loop]}
	
	""") # print what user need to know
		else:
		   	os.system("clear")
		   	print(f"""
cracking attempt: {loop +1}
""") # let user know 
		   	loop = loop + 1 
#sha512 hash crack
def sha512(hash, wordlist):
	try: # check if file really exist
		r = open(wordlist,"r").read().split("\n")
	except: # prompt error message
		print("please provide a wordlist")
		print("exiting")
		sys.exit() # exit program
	a = "1" # variable
	loop = 0 # variable
	
	#this is a very simple way to compare hash
	while "1" == a:
		ush = hashlib.sha512() # hash object
		try:
			ush.update(r[loop].encode()) # try to hash the word
		except: # error (IndexError)
			print("file empty or wordlist exhausted") # prompt error
			sys.exit() # exit
		if ush.digest() == hash: #condition
		   	a = "4" # change a variable
		   	print(f"""
			hash used: sha512
			hash found
hash: {ush.digest()}
hexdecimal: {ush.hexdigest()}
hashed: {r[loop]}
	
	""") # print what user need to know
		else:
		   	os.system("clear")
		   	print(f"""
cracking attempt: {loop +1}
""") # let user know 
		   	loop = loop + 1 

#blake2b hash crack
def blake2b(hash, wordlist):
	try: # check if file really exist
		r = open(wordlist,"r").read().split("\n")
	except: # prompt error message
		print("please provide a wordlist")
		print("exiting")
		sys.exit() # exit program
	a = "1" # variable
	loop = 0 # variable
	
	#this is a very simple way to compare hash
	while "1" == a:
		ush = hashlib.blake2b() # hash object
		try:
			ush.update(r[loop].encode()) # try to hash the word
		except: # error (IndexError)
			print("file empty or wordlist exhausted") # prompt error
			sys.exit() # exit
		if ush.digest() == hash: #condition
		   	a = "4" # change a variable
		   	print(f"""
			hash used: blake2b
			hash found
hash: {ush.digest()}
hexdecimal: {ush.hexdigest()}
hashed: {r[loop]}
	
	""") # print what user need to know
		else:
		   	os.system("clear")
		   	print(f"""
cracking attempt: {loop +1}
""") # let user know 
		   	loop = loop + 1 
#blake2s hash crack
def blake2s(hash, wordlist):
	try: # check if file really exist
		r = open(wordlist,"r").read().split("\n")
	except: # prompt error message
		print("please provide a wordlist")
		print("exiting")
		sys.exit() # exit program
	a = "1" # variable
	loop = 0 # variable
	
	#this is a very simple way to compare hash
	while "1" == a:
		ush = hashlib.blake2s() # hash object
		try:
			ush.update(r[loop].encode()) # try to hash the word
		except: # error (IndexError)
			print("file empty or wordlist exhausted") # prompt error
			sys.exit() # exit
		if ush.digest() == hash: #condition
		   	a = "4" # change a variable
		   	print(f"""
			hash used: blake2s
			hash found
hash: {ush.digest()}
hexdecimal: {ush.hexdigest()}
hashed: {r[loop]}
	
	""") # print what user need to know
		else:
		   	os.system("clear")
		   	print(f"""
cracking attempt: {loop +1}
""") # let user know 
		   	loop = loop + 1 