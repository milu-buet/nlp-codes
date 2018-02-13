# Natural Language Processing, Spring'18
# Assignment #2
# Md Lutfar Rahman
# mrahman9@memphis.edu

import re

def getBROWN():
	file = 'SnapshotBROWN.pos.all.txt'

	with open(file, 'r') as myfile:
		data=myfile.read()

	return data


def getPOS(data):
	pattern = "\((\w)+ (\')*(\w)+\)"
	sentences = []
	sentence = ''
	for x in re.finditer(pattern, data):
		word = x.group(0)
		if word == '(TOP END_OF_TEXT_UNIT)':
			sentences.append(sentence.strip(' '))
			sentence = ''
		else:
			sentence += word[1:-1] + ' '

	while('' in sentences):
		sentences.remove('')
	print(sentences)
	return sentences




data = getBROWN()
getPOS(data)

