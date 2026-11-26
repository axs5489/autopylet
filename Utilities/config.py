#!/usr/bin/env python
from __future__ import print_function, unicode_literals
##############################################################################
# Config file utility                                                        #
##############################################################################
__author__  = 'Arshia Sasson'                                                #
__date__    = '25-Nov-2026'                                                  #
__version__ = '0.1.0'                                                        #
##############################################################################
#   DATE   | VERSION |  AUTHOR  | CHANGELOG                                  #
#----------|---------|----------|--------------------------------------------#
# 20-07-08 |  0.0.1  | asasson  | Initial split from win.pu                  #
# 26-11-10 |  0.1.0  | asasson  | Modernization (tabs, header)               #
##############################################################################
#                             See LICENSE at the base directory              #
##############################################################################
import os

def get(fileaddr="C:\\Harris\\config.txt", debugOn = False):
	""" Checks for a computer configuration file and returns dictionary of settings"""
	try:
		if(not os.path.exists(fileaddr)) :
			new(fileaddr)
		
		if debugOn : print('Config File: ', fileaddr)
		with open(fileaddr,"r") as f:
			lcfg = f.readlines()
			if debugOn : print("Stored Config: ", lcfg)
			dcfg = {}
			for line in lcfg:
				try:
					if(line[0] == '#'):
						pass
					else:
						ki = line.index(' ')
						vi1 = line.index('\'') + 1
						vi2 = line.index('\'', vi1)
						if debugOn : print(ki, line[0:ki])
						if debugOn : print(vi1, vi2)
						if debugOn : print(line[vi1:vi2])
						if(vi2 > vi1) : dcfg[line[0:ki]] = line[vi1:vi2]
				except ValueError:
					print("Line Error in Config File")
		return dcfg
	except:
		print("File Error")

def save(cfg, filepath="C:\\Harris\\config.txt"):
	""" Writes a default computer configuration file if one is not there"""
	if(os.path.exists(filepath)) :
		print("File already made")
		with open(filepath,"r+") as f:
			pass
		return (-1)
	else:
		print("New Config File")
		with open(filepath,"w") as f:
			pass
		pass

def new(filepath=None):
	""" Writes a default computer configuration file if one is not there"""
	if(os.path.exists(filepath)) :
		print("File already made")
		return (-1)
	
	try:
		with open(filepath,"w") as f:
			print("File Opened")
			f.write("ADU = ''")
			f.write("STP = 'COM1'")
			f.write("RCR = ''")
			f.write("RCB = ''")
			f.write("RED = ''")
			f.write("BLK = ''")
			f.write("PM = 'GPIB0::14::INSTR'")
			f.write("SIG = ''")
			f.write("SA = ''")
			f.write("NA = ''")
			f.write("SCP = ''")
	except:
		print("New File Error")
	return 1
