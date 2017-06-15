#!/usr/bin/python
import os,time,commands,sys,socket
options="""
press 1 for manual setup
press 2 for automatic setup
"""
print options
ch=raw_input()
if ch =='1':
	print"find ip of all systems"
	execfile('ip-cpu.py') 
else:
	print"wrong"
	execfile('menu.py')
