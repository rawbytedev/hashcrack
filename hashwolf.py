import hashlib
import os
import sys
from io import StringIO
import contextlib
import time

global h
h = 0
## stdout
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
			code =f"""import hashlib
us = hashlib.{hash_type}()
us.update({raw.encode()})
t = us.digest()
print(t)"""
			exec(code)
		except:
			print("Error something went wrong, try again or make an issue on github")
	out = s.getvalue()
	return out
	
def result(hash_type, hash_to_crack, out, output_file=None):
	msg= f"""Cracked successfully
hash used: {hash_type}
hash cracked: {hash_to_crack}
*hashed: {out}"""
	print(msg)
	if output_file == None:
		os._exit(0)
	else:
		open(output_file, "w").write(msg)
		print(f"saved to file: {output_file}")
		os._exit(0)
	os._exit(0)

## direct mode
def direct(hash_type, wordlist, hash_to_crack, output_file=None):
	a = "1"
	b = 0
	t = open(wordlist, 'r').read().split("\n")
	try:
		while a == "1":
					
		#generate hash just give hashtype + word
				r = generatehash(hash_type, t[b])
		#convert byte to str without changing the byte
				l = f"{hash_to_crack}"
				s= r.split("\n")
				if l == s[0]:
					out = t[b]
					if output_file==None:
						result(hash_type, hash_to_crack, out)
					else:
						result(hash_type, hash_to_crack, out, output_file)
				else:
					print(f"Cracking attempt: {b+1}")
					b= b+1
	except:
		print("Wordlist exhausted")

def compare(hash_type, newPrefix, bytehash, output_file=None):
	strhash = generatehash(hash_type, newPrefix)
	strhash1 = strhash.split("\n")
	strhash2 = strhash1[0]
	if strhash2 == f"{bytehash}":
		#dt = time.time() #speed test
		#print(f"took: {dt-t} second") #speed test
		#print(f"{dt-tim}")
		result(hash_type, bytehash, newPrefix, output_file )
		os._exit(0)
	else:
		print(f"cracking attempt: {h+1}")
		
	

def printAllKLengthRec(set, prefix, n, k, hash_type, hash_to_crack, output_file=None):
    #global tim
    #tim = time.time()
    global h
    if (k == 0) :
        return
    for i in range(n):
        global newPrefix
        newPrefix = prefix + set[i]
        compare(hash_type, newPrefix, hash_to_crack, output_file)
        h = h +1
        
        printAllKLengthRec(set, newPrefix, n, k - 1, hash_type, hash_to_crack)
        
def indirect(hash_type, hash_to_crack, char_to_use="qwertzuiopasdfghjklyxcvbnm+×÷=%/\$€£@*!#:;&_()-'\",.?￦¥°¿¡^[]<>~`§μ¬Г´·{}©|¤₹៛₪", output_file=None, lenght=16):
	n = 0
	#global b
	#b = 0
#	global t
#	t = time.time() #speed test;
	try:
		while n == 0:
			printAllKLengthRec(list(char_to_use), "", len(char_to_use), lenght, hash_type, hash_to_crack, output_file)
			#print(f"cracking attempt: {b+1}")
			#b = b+1
	except:
				print("Error please report the error on github with all details")
			
def analyse(hash_type):
	try:
		f = open("logs/rainlogs.txt", "r")
	except:
		f = open("logs/rainlogs.txt", "w").write(f"{hash_type}\n")
	else:
		fi = open("logs/rainlogs.txt", "r").read()
		fil = open("logs/rainlogs.txt", "w").write(f"{fi}{hash_type}\n")

## dictionnary	
def dictionnary(hash_type, set = "qwertzuiopasdfghjklyxcvbnm+×÷=%/\\$€£@*!#:;&_()-'\",.?￦¥°¿¡^[]<>~`§μ¬Г´·{}©|¤₹៛₪﷼฿Ωθฯ1234567890QWERTZUIOPASDFGHJKLYXCVBNM"):
			
			prefix = ""
			n = len(set)
			k = 32
			analyse(hash_type)
			generate(set, prefix, n, k, hash_type)

def writeout(raw, hash_type):
	a = 0
	b = 0
	while b == 0:
		try:
			open(f"dict/{hash_type}/{a}.txt", "r").read()
		except:
			open(f"dict/{hash_type}/{a}.txt", "w")
			writeout(hash_type, a)
		else:
			a = a + 1
def generate(set, prefix, n, k, hash_type):
    global h
    if (k == 0) :
        return
    for i in range(n):
        global newPrefix
        newPrefix = prefix + set[i]
        store(newPrefix, hash_type)
        h = h +1
        
        generate(set, newPrefix, n, k - 1)
## entry point
def start(mode, hash_type, wordlist, hash_to_crack, char_to_use, output_file):
	if mode == "direct":
		direct(hash_type, wordlist, hash_to_crack, output_file)
	elif mode == "indirect":
		indirect(hash_type, hash_to_crack, char_to_use, output_file)
	elif mode == "dictionnary":
		print("Unavailable under development")
		#dictionnary(hash_type)
	elif mode == "rainbow":
		print("underdevelopment")
		#rainbow(hash_type, hash_to_crack, output_file)
	else:
		print("[#] An error occured please create an issue at github.com/Xnetwolf/hashwolf to be helped")


#direct("md5","txt.txt",  b'I\xf6\x8a\\\x84\x93\xec,\x0b\xf4\x89\x82\x1c!\xfc;', "heloo.txt")
#print(generatehash("md5", "hi"))