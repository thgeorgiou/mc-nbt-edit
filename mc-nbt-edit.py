#!/usr/bin/python
#mc-nbt-edit by sakisds <sakisds@gmx.com>
#Uses the NBT library by Thomas Woolford <woolford.thomas@gmail.com>
#Based on the NBT specifications by Markus Persson

from nbt import *
import sys

def help(): #Prints help
		print "mc-nbt-edit by sakisds <sakisds@gmx.com>\n\nUsage: mc-nbt-edit (--help) file tag value(v)\n"
		print "File: level.dat, usually inside .minecraft/saves/[mapname]\nTag: Tag to edit, possible values are GameType and hardcore"
		print "Value: 1 for true, 0 for false. For GameType it's 1 for Creative and 0 for Survival.\n\n\nOptions:"
		print "--print: Prints the contents of the file and exits\n--help: Displays this message."
		exit()
def complain(): #Complains on wrong options.
	print "Invalid options. Try --help."
	exit()

print len(sys.argv)
if len(sys.argv) == 1 : #Decide about printing help or complaining
	help()
elif len(sys.argv) == 2:
	if sys.argv[1] == "--help":
		help()
	else:
		complain()
elif len(sys.argv) == 3:
	complain()

try: #Try to read the file.
	nbt = NBTFile(sys.argv[1],'rb')
except Exception:
	print "Could not open file "+sys.argv[1]


compound = nbt.__getitem__("Data") #Do the editing

if sys.argv[2] == "GameType" or sys.argv[2] == "hardcore":
	tag = TAG_Int(sys.argv[2])
	tag.name = sys.argv[2]
else:
	print "Unknown tag. Try --help."

if sys.argv[3] == "0":
	tag.value = 0
elif sys.argv[3] == "1":
	tag.value = 1
else:
	complain()

compound.__setitem__(sys.argv[2], tag)

try:
	nbt.write_file() #Save changes to disk
except Exception:
	print "Could not save buffer to disk. Chances are discarded."

