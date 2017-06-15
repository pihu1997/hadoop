#!/usr/bin/python
import os,time,commands,getpass

print  "WELCOME TO THE WORLD OF HADOOP"
print "______________________________"
print ".............................."
time.sleep(3)
user=raw_input("Type Username: ")
password= getpass.getpass("Type Password: ")
if user =='root' and password == 'redhat' :
	print "Sucessfull"
	execfile('menu.py')
else:
	print "WRONG AUTHENTICATION"
	time.sleep(1)
	print "____________________"
	execfile('start.py')
