from pybrain.datasets import SupervisedDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer

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
			asint.append(0)
	return asint

def inttowords(word_list,nums):
	aswords = list()
	for i in nums:
		try:
			aswords.append(word_list[int(i)])
		except Exception:
			aswords.append(" ")
	return aswords

#BEGIN VARIABLE DECLARATIONS
word_list = list()
insize=3
outsize = 6
nwords = list()
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

with open('raps.txt') as f:
	content = f.readlines()
	for line in content:
		for subline in line.split(':'):
			words = set(word.strip() for word in subline.split())
			for word in words:
				if not wordinlist(word_list,word.lower()):
					word_list.append(word.lower())
					nwords.append(word.lower())
with open('wordlist.txt', 'a') as f:
	for word in nwords:
		f.write(word + " ")

with open('raps.txt') as f:
	contents = f.readlines()
	for line in contents:
			linesplit = line.split(":")
			if(len(linesplit) ==2):
				inp = linesplit[0].split()
				inp = converttoint(word_list,inp)
				for i in range(0,3-len(inp)):
					inp.append(0)
				rap = linesplit[1].split()
				rap = converttoint(word_list,rap)
				for i in range(0,6-len(rap)):
					rap.append(0)
				if len(rap) == 6:
					if len(inp) == 3:	
						ds.addSample(inp,rap)
	
trainer.trainUntilConvergence()

n1 = int(input())
n2 = int(input())
n3 = int(input())

output = net.activate((n1,n2,n3))

output = inttowords(word_list,output)
print(output)

