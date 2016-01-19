from random import randint
import random
from datetime import datetime
import pyraptools
from pybrain.tools.customxml import NetworkReader
print("Enter the name of the rapper xml file")
rappername = input()
net = NetworkReader.readFrom(rappername+".xml")
word_list = list()
rapper_list = list()
random.seed(datetime.now())
#fetching list of all possible words
with open('progfiles/wordlist.txt') as f:
	content = f.readlines()
	for line in content:
		for subline in line.split(':'):
			for word in subline.split():
				word_list.append(word.strip())

#fetching list of rappers
with open('progfiles/rapperlist.txt') as f:
	content = f.readlines()
	for line in content:
		for word in line.split(","):
			if not word =="\n":
				if not word =="":
					rapper_list.append(word.strip())


print("Enter a rappers name from the list of rappers available:")
print(rapper_list)
n1 = input()
n1 = rapper_list.index(n1)

n2 = randint(0,9)
print(n2)
print("Enter file to save the rap to.")
fname = input()
output = net.activate((n1,n2))
output = pyraptools.inttowords(word_list,output)
toprint = ""
for word in output:
	if not word == "":
		toprint+=word+" "
#print(toprint)
with open(fname, "w+") as f:
	f.write(toprint)
