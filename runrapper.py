import jsonpickle
from random import randint
print("Enter the name of the rapper with .rpr at the end")
rappername = input()
jsonrapper = ""
with open(rappername+".rpr") as f:
	jsonrapper = f.read()
rapper = jsonpickle.decode(jsonrapper)
print(rapper)
word_list = list()
rapper_list = list()

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
				rapper_list.append(word.strip())


print("Enter a rappers name from the list of rappers available:")
print(rapper_list)
n1 = input()
n1 = rapper_list.index(n1)
n2 = randint(0,9)

output = rapper.net.activate((n1,n2))
output = inttowords(word_list,output)
toprint = ""
for word in output:
	if not word == "":
		toprint+=word+" "
print(toprint)
