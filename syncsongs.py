from os import listdir
import os
from os.path import isfile,join
import rapconverter
mypath = os.getcwd()+"\\raps"
files = [f for f in listdir(mypath) if isfile(join(mypath,f))]
for f in files:
	split = f.split("--")
	rapconverter.main(split[0],f)
