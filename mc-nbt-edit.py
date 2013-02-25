#!/usr/bin/env python
#mc-nbt-edit 0.3 by sakisds <sakisds@gmx.com>
#Uses the NBT library by Thomas Woolford <woolford.thomas@gmail.com>
#Based on the NBT specifications by Markus Persson

from nbt import nbt
from nbt.nbt import *
import sys, os

def help(): #Prints help
		print "mc-nbt-edit 0.2 by sakisds <sakisds@gmx.com>\n\nUsage: mc-nbt-edit file tag datatype value\n"
		print "Possible datatypes: byte, int, float, long, string, short, double.\n Lists are not yet supported.\n\n\nOptions:"
		print "--help: Displays this message and then exit."
		print "--print: Prints tree inside the given NBT file and then exit."
		exit()

def complain(): #Complains on wrong options.
	print "Invalid options. Try --help."
	exit(1)

def loadfile(filepath): #Loads the NBT file
	try:
		return nbt.NBTFile(filepath,'rb')
	except Exception:
		print "Could not open file "+sys.argv[1]
		exit(1)

def savefile(nbt):
	try:
		nbt.write_file()
	except Exception:
		print "Could not save buffer to disk. Chances are discarded."
		exit(1)

def settag(name, dtype, value): #Sets wanted tag
	if dtype == "byte":
		tag = TAG_Byte(name)
		tag.value = int(value)
	elif dtype == "int":
		tag = TAG_Int(name)
		tag.value = int(value)
	elif dtype == "float":
		tag = TAG_Float(name)
		tag.value = float(value)
	elif dtype == "long":
		tag = TAG_Long(name)
		tag.value = long(value)
	elif dtype == "string":
		tag = TAG_String(name)
		tag.value = value
	elif dtype == "short":
		tag = TAG_Short(name)
		tag.value = int(value)
	elif dtype == "double":
		tag = TAG_Double(sys.argv)
		tag.value = float(value)
	else:
		print "Unknown tag data type. "
		exit()
	tag.name = name
	return tag

def printtag(tag):
	print tag.name+":"+tag

#Decide about printing help or complaining
printing = False
if len(sys.argv) == 1 :
	help()
elif len(sys.argv) == 2:
	if sys.argv[1] == "--help":
		help()
	else:
		complain()
elif len(sys.argv) == 3:
	if sys.argv[2] == "--print":
		printing = True
	else:
		complain()

#Load file
nbt = loadfile(sys.argv[1])

#Print if needed
if printing:
	print nbt.pretty_tree()
	exit()

#Parse tag
path = sys.argv[2].split('.')

#Do the editing
if len(path) == 1:
	tag = settag(path[0], sys.argv[3], sys.argv[4])
	nbt.__setitem__(path[0], tag)
elif len(path) == 2:
	compound = nbt.__getitem__(path[0])
	tag = settag(path[1], sys.argv[3], sys.argv[4])
	compound.__setitem__(path[1], tag)
elif len(path) == 3:
	compound = nbt.__getitem__(path[0])
	subcompound = compound.__getitem__(path[1])
	tag = settag(path[2], sys.argv[3], sys.argv[4])
	subcompound.__setitem__(path[2], tag)

#Save changes to disk
savefile(nbt)
