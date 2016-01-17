from pybrain.datasets import SupervisedDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from random import randint
#END IMPORTS

#FUNCTION DECLARATIONS BEGIN
def wordinlist(word_list,tword):
	for word in word_list:
		if word == tword:
			return True
	return False

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
			aswords.append(" ")
		else:
			try:
				aswords.append(word_list[int(i)])
			except Exception:
				aswords.append(" ")
	return aswords

#FUNCTION DECLARATIONS END

#BEGIN VARIABLE DECLARATIONS
word_list = list()
insize=2
outsize = 50
nwords = list()
rapper_list = list()
ds = SupervisedDataSet(insize,outsize)
net = buildNetwork(insize,5,outsize)
trainer = BackpropTrainer(net,ds)
#END VARIABLE DECLARATIONS


#fetching list of all possible words
with open('wordlist.txt') as f:
	content = f.readlines()
	for line in content:
		for subline in line.split(':'):
			for word in subline.split():
				word_list.append(word.strip())

#fetching list of rappers
with open('rapperlist.txt') as f:
	content = f.readlines()
	for line in content:
		for subline in line.split():
			for word in subline:
				rapper_list.append(word.strip())

#adding any unused words from the raps to nwords
with open('raps.txt') as f:
	content = f.readlines()
	for line in content:
		slines = line.split(":")
		rappername = slines[0]
		if not wordinlist(rapper_list,rappername):
			rapper_list.append(rappername)
		for subline in slines:
			words = set(word.strip() for word in subline.split())
			for word in words:
				if not wordinlist(word_list,word.lower()):
					word_list.append(word.lower())
					nwords.append(word.lower())

#adding them in to the wordlist file
with open('wordlist.txt', 'a') as f:
	for word in nwords:
		f.write(word + " ")

#opening up raps
with open('raps.txt') as f:
	contents = f.readlines()
	for line in contents:
			linesplit = line.split(":")
			if(len(linesplit) ==2):
				inp = linesplit[0]
				inp = converttoint(rapper_list,inp)
				for i in range(0,insize-len(inp)):
					inp.append(randint(0,9))
				rap = linesplit[1].split()
				rap = converttoint(word_list,rap)
				for i in range(0,outsize-len(rap)):
					rap.append(-1)
				if len(rap) == outsize:
					if len(inp) == insize:	
						ds.addSample(inp,rap)
	
trainer.trainUntilConvergence()

print("Enter a rappers name from the list of rappers available:")
n1 = input()
print("Enter an integer between 0 and 9")
n2 = int(input())

output = net.activate((n1,n2))
output = inttowords(word_list,output)
print(output)

