from pybrain.datasets import SupervisedDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from random import randint
from pybrain.structure import FeedForwardNetwork
from pybrain.tools.customxml import NetworkWriter
#END IMPORTS

#CLASS DECLARATIONS BEGIN
#END CLASS DECLARATIONS
#FUNCTION DECLARATIONS BEGIN
def wordinlist(word_list,tword):
	for word in word_list:
		if word == tword:
			return True
	return False
def convertrappertoint(word_list, rapper):
	asint = list()
	try:
		asint.append(word_list.index(rapper))
	except Exception:
		asint.append(-1)
	return asint

def converttoint(word_list,words):
	asint = list()
	for word in words:
		try:
			asint.append(word_list.index(word))
		except Exception:
			asint.append(-1)
	return asint
def inttowords(word_list,nums):
	aswords = list()
	for i in nums:
		if i < -.5:
			aswords.append("")
		else:
			try:
				aswords.append(word_list[int(i)])
			except Exception:
				aswords.append("")
	return aswords

#FUNCTION DECLARATIONS END

#BEGIN VARIABLE DECLARATIONS
word_list = list()
insize=2
print("How long do you estimate the longest rap/poem is?")
outsize = int(input())
nwords = list()
rapper_list = list()
nrappers = list()
ds = SupervisedDataSet(insize,outsize)
print("Enter the size for the three layers (High numbers will take a very long time, reccomended to keep below 30):")
size = int(input())
net = buildNetwork(insize,size,size,size,outsize)
trainer = BackpropTrainer(net,ds)
#END VARIABLE DECLARATIONS


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

#adding any nonexisting words from the raps to nwords
with open('progfiles/raps.txt') as f:
	content = f.readlines()
	for line in content:
		slines = line.split(":")
		rappername = slines[0]
		if not wordinlist(rapper_list,rappername):
			if not rappername == "\n":
				rapper_list.append(rappername)
				nrappers.append(rappername)
		for subline in slines:
			words = set(word.strip() for word in subline.split())
			for word in words:
				if not wordinlist(word_list,word.lower()):
					word_list.append(word.lower())
					nwords.append(word.lower())

with open("progfiles/rapperlist.txt","a") as f:
	for rapper in nrappers:
		if not rapper == "\n":
			f.write(rapper+",")

#adding them in to the wordlist file
with open('progfiles/wordlist.txt', 'a') as f:
	for word in nwords:
		f.write(word + " ")

#opening up raps
with open('progfiles/raps.txt') as f:
	contents = f.readlines()
	for line in contents:
			linesplit = line.split(":")
			if(len(linesplit) ==2):
				inp = linesplit[0]
				inp = convertrappertoint(rapper_list,inp)
				inp.append(randint(0,9))
				rap = linesplit[1].split()
				rap = converttoint(word_list,rap)
				for i in range(0,outsize-len(rap)):
					rap.append(-1)
				if len(rap)>outsize:
					rap = rap[:-(len(rap)-outsize)]
				if len(rap) == outsize:
					if len(inp) == insize:	
						ds.addSample(inp,rap)
print("Training, this may take awhile.")
trainer.trainUntilConvergence()
print("Congratulations, your network has been trained")
print("Please enter where you want to save your file")
fname = input()
NetworkWriter.writeToFile(net,fname + ".xml")

print("Enter a rappers name from the list of rappers available:")
print(rapper_list)
n1 = input()
n1 = rapper_list.index(n1)
n2 = randint(0,9)

output = net.activate((n1,n2))
output = inttowords(word_list,output)
toprint = ""
for word in output:
	if not word == "":
		toprint+=word+" "
print(toprint)
