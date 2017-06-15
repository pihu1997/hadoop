#!/usr/bin/python
import os,time,commands,sys,socket
options="""
TO SETUP HADOOP PROCESS : PRESS 1
FOR M.R. SETUP : PRESS 2
FOR HIVE : PRESS 3
"""
print options

ch=raw_input()
if ch == '1':
	print "START SETUP PROCESS:::"
	execfile('hdfs-setup.py')
elif ch =='2':
	print "CPU cores..."
	execfile('mrsetup.py')
else:
	print "Option is wrong.!!!!"
	execfile ('start.py')
 
