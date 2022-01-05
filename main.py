import hashlib
import hashwolf

#list of hash
print("""

             |
             |        - HashCrack -
             | author : XnetwolfX/Xnetwolf
             | ver: 1
             |  Crack hash

""")

#
print("""
{1} md5
{2} sha1
{3} sha224
{4} sha256
{5} sha384
{6} sha512
{7} blake2b
{8} blake2s
""")
option = input("μ~> ")
user = input("hash μ~> ")
wordlist = input("wordlist μ~> ")

if option == "1":
	hashwolf.md5(user, wordlist)
elif option == "2":
	hashwolf.sha1(user, wordlist)
elif option == "3":
	hashwolf.sha224(user, wordlist)
elif option == "4":
	hashwolf.sha256(user, wordlist)
elif option == "5":
	hashwolf.sha384(user, wordlist)
elif option == "6":
	hashwolf.sha512(user, wordlist)
elif option == "7":
	hashwolf.blake2b(user, wordlist)
elif option == "8":
	hashwolf.blake2s(user.wordlist)
	
else:
	print("error try again later")
	
	break