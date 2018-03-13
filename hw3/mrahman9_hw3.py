# Natural Language Processing, Spring'18
# Assignment #3
# Md Lutfar Rahman
# mrahman9@memphis.edu

import re


brownfile = 'BROWN.pos.all'
browncleanfile = 'BROWN-clean.pos.txt'

Snapshotbrownfile = 'SnapshotBROWN.pos.all.txt'
Snapshotbrowncleanfile = 'SnapshotBROWN-clean.pos.txt'

T25brownfile = '25brown.pos.txt'
T25browncleanfile = '25brown-clean.pos.txt'


#code for task_i
#---------------------------------------------------
def getBROWN(brownfile):
	with open(brownfile, 'r') as myfile:
		data=myfile.read()

	return data


def getSentences(data):
	sep1 = '(TOP END_OF_TEXT_UNIT)'
	sep2 = '(ROOT'
	pattern = "\((\w|\$|\.\-)+ (\w|\.|\]|\[|\'|\-)+\)"
	sentences = []
	sentence = ''
	for x in re.finditer(pattern, data):
		word = x.group(0)
		if word == sep1:
			sentences.append(sentence.strip(' '))
			sentence = ''
		else:
			sentence += word[1:-1] + ' '
	sentences.append(sentence.strip(' '))

	while('' in sentences):
		sentences.remove('')
	#print(sentences)
	return sentences

def saveSentencesToBrownClean(sentences, browncleanfile):
	file = open(browncleanfile,'w')
	for sentence in sentences:
		file.write(sentence+'\n')

	file.close()


def createBrownClean(brownfile, browncleanfile):
	data = getBROWN(brownfile)
	sentences = getSentences(data)
	saveSentencesToBrownClean(sentences, browncleanfile)
	print("ended")
# -------------------------------------------------------


#---------------------------------------------------

def createHashofHashes(browncleanfile):
	HashOfHash = {}
	with open(browncleanfile, 'r') as myfile:
		for sentence in myfile:
			tag_words = sentence.strip('\n').split(' ')
			for i in range(0, len(tag_words),2):
				tag = tag_words[i]
				word = tag_words[i+1]
				#print(word)

				if word not in HashOfHash:
					HashOfHash[word] = {}

				if tag not in HashOfHash[word]:
					HashOfHash[word][tag] = 0
				
				HashOfHash[word][tag]+=1
	return HashOfHash

#---------------------------------------------------

def addNewRule(HashofHashes):
	HashofHashes['Rabada'] = {'NNP':3}
	HashofHashes['Maharaj'] = {'NNP':4}
	HashofHashes['Shaun'] = {'NNP':3}
	HashofHashes['Philander'] = {'NNP':3}
	HashofHashes['Kock'] = {'NNP':3}
	HashofHashes['Morkel'] = {'NNP':3}
	HashofHashes['Quinton'] = {'NNP':3}
	HashofHashes['Keshav'] = {'NNP':3}
	HashofHashes['Steven'] = {'NNP':3}
	HashofHashes['Usman'] = {'NNP':3}
	HashofHashes['Villiers'] = {'NNP':3}
	HashofHashes['Morne'] = {'NNP':3}
	HashofHashes['Khawaja'] = {'NNP':3}
	HashofHashes['lbw'] = {'NNP':3}
	HashofHashes['Kagiso'] = {'NNP':3}
	HashofHashes['Kingsmead'] = {'NNP':3}




#-----------------------------------------------------

def evaluateTagging(fullHashofHashes, TestHashofHashes):
	count = 0
	correct = 0
	cc = 0
	for word in TestHashofHashes:
		if word in fullHashofHashes:
			trained_tag_freq = fullHashofHashes[word]
			trained_frequent_tag = sorted(trained_tag_freq, key=trained_tag_freq.__getitem__, reverse=True)[0]
			#print(word,trained_frequent_tag,type(TestHashofHashes))
			tag_freqs = TestHashofHashes[word]
			for tag in tag_freqs:
				count+=tag_freqs[tag]

			if trained_frequent_tag in tag_freqs:
				correct+=tag_freqs[trained_frequent_tag]
		else:
			#print(word,TestHashofHashes[word])
			tag_freqs = TestHashofHashes[word]
			for tag in tag_freqs:
				count+=tag_freqs[tag]


	accuracy = correct/count
	print("accuracy=%s"%(accuracy,))
#----------------------------------------------------

def runTask_i():
	createBrownClean(brownfile, browncleanfile)
	fullHashofHashes=createHashofHashes(browncleanfile)
	print(fullHashofHashes)

def runTask_ii():
	fullHashofHashes=createHashofHashes(browncleanfile)
	SnapshotHashofHashes=createHashofHashes(Snapshotbrowncleanfile)
	evaluateTagging(fullHashofHashes, SnapshotHashofHashes)

def runTask_iii():
	fullHashofHashes=createHashofHashes(browncleanfile)
	T25HashofHashes=createHashofHashes(T25browncleanfile)
	evaluateTagging(fullHashofHashes, T25HashofHashes)

	print('\nWith new rules:')
	addNewRule(fullHashofHashes)
	evaluateTagging(fullHashofHashes, T25HashofHashes)



if __name__ == "__main__":
	#createBrownClean(brownfile, browncleanfile)
	#createBrownClean(Snapshotbrownfile, Snapshotbrowncleanfile)
	#createBrownClean(T25brownfile, T25browncleanfile)

	#runTask_i()
	#runTask_ii()
	runTask_iii()


	