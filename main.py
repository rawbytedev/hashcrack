import argparse
import os 
import hashwolf


#Made by Xnetwolf
def banner():
	#A banner, Title whatever
	print("HashWolf")
	
	
def entry_point():
	banner()
	scan_input()
	
#def crack()
def scan_input():
    	
	if ar.attack == "direct":
		print("direct")
		## uncomment
		#try:
#			open(ar.wordlist, "r")
#		except:
#			print("""[#] An error occured while trying to use wordlist
#The cause of the error are listed:
#- File doesn't exist
#- Hashwolf doesn't have permission to read file
#- Wrong path

#Try again later, If the problem isn't solved, make an issue on github with you're log files """)
#		else:
#			print("## Wordlist verified")
	elif ar.attack == "rainbow":
		re = open("logs/rainlogs.txt", "r")
		if ar.type in re:
			print("## Rainbow dictionnary verified")
		else:
			print("error, Generate a dictionnary before starting")
			
	print("Attack starting ")
	print(f"""
Mode: {ar.attack}
Hash_Type: {ar.type}
Wordlist: {ar.wordlist}
hash_to_crack: {ar.hashed}
""")
##use hashwolf to start attack
	hashwolf.start(ar.attack, ar.hashed, ar.wordlist, ar.type)



#parse, parse, argument
## add more later	
p = argparse.ArgumentParser()
# attack
## modify it a little
p.add_argument('-a', '--attack', required=True, help="""You have 4 mode: direct, indirect, rainbows, rainbow

* direct cracking uses a wordlist provided by user, hashwolf make use of thread to be fast

* indirect cracks without wordlist, it make use of thread and a good technique to be fast(generate 20 words in a roll, hash all of them then compare)

* rainbows is the one that is used to generate hash directory for later use, the program generate them with care and store them in a predefined location

* rainbow cracking uses the dictionnary stored on the device by rainbows, fast and effective cause for cracking it uses, hash lenght + hash type, to avoid useless searching""")

# hash type
## edit to a better name
p.add_argument('-t', '--type', help="This is the hashtype to crack, specifie the hashtype to crack(if you don't know hashtype don't specifie it) ex: -hash md5, -hash sha256", required=True)
# wordlist
## edit to a better name
p.add_argument('-word', '--wordlist', help="This is the wordlist path provided by user for direct cracking mode")

p.add_argument('-hash', '--hashed', help="The hash you want to crack")

global ar
ar = p.parse_args()
entry_point()
	