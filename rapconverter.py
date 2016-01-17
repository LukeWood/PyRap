import sys
import string

if(len(sys.argv)!=3):
	print("Please run this file with the syntax of: rapconv.py fname rappername")
	sys.exit()
fname = sys.argv[1]
rname = sys.argv[2]
lyrics = ""
try:
	with open(fname) as f:
		contents = f.readlines()
		for line in contents:
			lyrics+=line
except Exception:
	print("INVALID FILENAME")
	sys.exit()
lyrics = lyrics.lower()
lyrics = lyrics.replace("\n"," ")
allc = string.maketrans("","")
noweirdchars = allc.translate(allc,string.ascii_lowercase+ " ")
lyrics = lyrics.translate(allc,noweirdchars)
with open("progfiles/raps.txt","a") as f:
	f.write("\n"+rname+":"+lyrics)
