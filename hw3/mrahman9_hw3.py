# Natural Language Processing, Spring'18
# Assignment #3
# Md Lutfar Rahman
# mrahman9@memphis.edu

import re


brownfile = 'BROWN.pos.all'
browncleanfile = 'BROWN-clean.pos.txt'

Snapshotbrownfile = 'SnapshotBROWN.pos.all.txt'
Snapshotbrowncleanfile = 'SnapshotBROWN-clean.pos.txt'


#code for task_i
#---------------------------------------------------
def getBROWN(brownfile):
	with open(brownfile, 'r') as myfile:
		data=myfile.read()

	return data


def getSentences(data):
	pattern = "\((\w|\$|\.\-)+ (\w|\.|\]|\[|\'|\-)+\)"
	sentences = []
	sentence = ''
	for x in re.finditer(pattern, data):
		word = x.group(0)
		if word == '(TOP END_OF_TEXT_UNIT)':
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

def evaluateTagging(fullHashofHashes, SnapshotHashofHashes):
	count = 0
	correct = 0
	cc = 0
	for word in SnapshotHashofHashes:
		if word in fullHashofHashes:
			trained_tag_freq = fullHashofHashes[word]
			trained_frequent_tag = sorted(trained_tag_freq, key=trained_tag_freq.__getitem__, reverse=True)[0]
			#print(word,frequent_tag)
			tag_freqs = SnapshotHashofHashes[word]
			for tag in tag_freqs:
				count+=tag_freqs[tag]

			if trained_frequent_tag in tag_freqs:
				correct+=tag_freqs[trained_frequent_tag]
		else:
			tag_freqs = SnapshotHashofHashes[word]
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
	pass



if __name__ == "__main__":
	#createBrownClean(brownfile, browncleanfile)
	#createBrownClean(Snapshotbrownfile, Snapshotbrowncleanfile)

	#runTask_i()
	runTask_ii()
	#runTask_iii()


	