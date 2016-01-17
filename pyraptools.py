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
