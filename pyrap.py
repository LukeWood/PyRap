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
		asint.append(word_list.index(word))
	return asint

def inttowords(word_list,nums):
	aswords = list()
	for i in nums:
		aswords.append(word_list[int(i)])
	return aswords
word_list = list()
with open('wordlist.txt') as f:
	content = f.readlines()
	for line in content:
		for subline in line.split(':'):
			for word in subline.split():
				word_list.append(word.strip())
nwords = list()
ds = SupervisedDataSet(3,3)
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
			inp = linesplit[0].split()
			inp = converttoint(word_list,inp)
			rap = linesplit[1].split()
			rap = converttoint(word_list,rap)
			ds.addSample(inp,rap)
			
net = buildNetwork(3,3,3)

trainer = BackpropTrainer(net,ds)
trainer.trainUntilConvergence()

n1 = int(input())
n2 = int(input())
n3 = int(input())

output = net.activate((n1,n2,n3))

output = inttowords(word_list,output)
print(output)
