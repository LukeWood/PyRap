import sys
import string
def main(arg1,arg2):

	fname = "raps/"+arg2
	rname = arg1
	lyrics = ""
	try:
		with open(fname) as f:
			contents = f.readlines()
			for line in contents:
				lyrics+=line
	except Exception:
		print(fname+ "is an INVALID FILENAME")
		sys.exit()
	lyrics = lyrics.lower()
	lyrics = lyrics.replace("\n"," ")
	allc = string.maketrans("","")
	noweirdchars = allc.translate(allc,string.ascii_lowercase+ " ")
	lyrics = lyrics.translate(allc,noweirdchars)
	with open("progfiles/raps.txt","a") as f:
		f.write("\n"+rname+":"+lyrics)
