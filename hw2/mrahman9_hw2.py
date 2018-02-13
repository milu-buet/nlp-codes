# Natural Language Processing, Spring'18
# Assignment #2
# Md Lutfar Rahman
# mrahman9@memphis.edu

import re

brownfile = 'SnapshotBROWN.pos.all.txt'
browncleanfile = 'BROWN-clean.pos.txt'


#code for task_i
#---------------------------------------------------
def getBROWN():
	with open(brownfile, 'r') as myfile:
		data=myfile.read()

	return data


def getSentences(data):
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
	#print(sentences)
	return sentences

def saveSentencesToBrownClean(sentences):
	file = open(browncleanfile,'w')
	for sentence in sentences:
		file.write(sentence+'\n')

	file.close()


def runTask_i():
	data = getBROWN()
	sentences = getSentences(data)
	saveSentencesToBrownClean(sentences)
# -------------------------------------------------------


#code for task_ii
#---------------------------------------------------

def createHashofHashes():
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


def runTask_ii():
	HashOfHash = createHashofHashes()
	print(HashOfHash)
#-------------------------------------------------------


#code for task_iii
#---------------------------------------------------

def get20FrequentTags():
	HashOfHash = createHashofHashes()
	word_tag = {}
	for word,tag_freq in HashOfHash.items():
		for tag,freq in tag_freq.items():
			word_tag[tag,word,freq] = freq
	return sorted(word_tag, key=word_tag.__getitem__, reverse=True)[0:20]


def runTask_iii():
	frequent_tags = get20FrequentTags()
	print(frequent_tags)


#--------------------------------

#code for task_iv
#---------------------------------------------------
def getMostFrequentTag():
	return get20FrequentTags()[0]

def tagWithMostFrequent():
	tag,word,freq = getMostFrequentTag()

def runTask_iv():
	tagWithMostFrequent()
	

#---------------------------------------------------


runTask_iv()