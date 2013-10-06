#!/usr/bin/python

import hashlib
import sys
from termcolor import colored


U = ["nick","jack","vivek","admin","webadmin","sqladmin","jill","natasha"]

'''
Use The Following Command To Generate wordlist
#crunch 6 6 xyz123 -o wordlist.txt
'''
p = open('wordlist.txt','r')
P = [x.strip() for x in p.readlines()]
p.close()


for UserName in U:
	for Pass in P:

		realm = "Pentester-Academy"
		nonce = "X95LDujmBAA=9c8ec8a0aeee0ddf7f24a5a75c57d0f90245d0f5"
		OriginalResponse = "0fd7c603fdf61e89bfc9c95fb73e343a"
		qop = "auth"
		nc = "00000001"
		cnonce="89b024ea3adb54ec"
		URI = "/"

		Hash1 = hashlib.md5(UserName+":"+realm+":"+Pass).hexdigest()
		Hash2 = hashlib.md5("GET:"+URI).hexdigest()

		TestResponse = hashlib.md5(Hash1+":"+nonce+":"+nc+":"+cnonce+":"+qop+":"+Hash2).hexdigest()

		if TestResponse == OriginalResponse:
			print colored("Login with Username %s ... Password %s ... Response %s"%(UserName,Pass,TestResponse),"green")
			sys.exit(0)
		else:
			print "Login with Username %s ... Password %s ... Response %s ... Failed!"%(UserName,Pass,TestResponse)
