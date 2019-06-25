#!/usr/local/bin/python
from sys import argv
from scanfile import scanner
class UnknowCommand(Exception):pass

commands={'*':'Ms.','+':'Mr.'}

def proccessLine(line):
	try:
		print("%s%s"%(commands[line[0]],line[1:]))
	except KeyError:
		raise UnknowCommand(line)

filename='data.txt'
if len(argv)==2:
	filename=argv[1]
scanner(filename,proccessLine)
	