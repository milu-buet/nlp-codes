# Natural Language Processing, Spring'18
# Assignment #4
# Md Lutfar Rahman
# mrahman9@memphis.edu

import re
from tree import *


brownfile = 'BROWN.pos.all'
browncleanfile = 'BROWN-clean.pos.txt'

Snapshotbrownfile = 'SnapshotBROWN.pos.all.txt'
Snapshotbrowncleanfile = 'SnapshotBROWN-clean.pos.txt'


def getTags(line):
	free_tags = line.replace('(',' ').replace(')',' ')
	free_tags = free_tags.split(' ')

	while '' in free_tags:
		free_tags.remove('')

	#free_tags  = free_tags[0:len(free_tags)-2]

	removables = []
	unwanteds = ["-","'",",","`","\n"]
	for tag in free_tags:
			for unwanted in unwanteds:
				if unwanted in tag:
					removables.append(tag)

	for removable in removables:
		while removable in free_tags:
			free_tags.remove(removable)



	return free_tags


def getTagLevel(line,tag):
	return line.index(tag)


def addTagsInTree(line,lastNode):
	tags = getTags(line)
	#print(tags)
	for tag in tags:
		tag_level = getTagLevel(line,tag)
		node = BrownNode(tag,tag_level)
		ancestor = lastNode.getAncestorByLevel(tag_level)
		#print(ancestor.show())
		#print(tag,tag_level)
		ancestor.addChild(node)

		lastNode = node

	return lastNode


def getSentenceTrees(brownfile):
	sep = '(TOP END_OF_TEXT_UNIT)\n'
	end = "(. .))"
	sentences = []
	rootNode = BrownNode('ROOT',0)
	lastNode = rootNode 

	with open(brownfile) as fp:
		for line in fp:
			if len(line) < 2 or end in line:
				continue
			elif line == sep:
				sentences.append(rootNode)
				rootNode = BrownNode('ROOT',0)
				lastNode = rootNode
				#print(line)
			else:
				#print(line)
				lastNode = addTagsInTree(line,lastNode)

	return sentences

def getAllRules(sentences,WithNONTerminal):
	AllRules = []
	for sentence in sentences:
		rules = sentence.getRulesExceptRoot(WithNONTerminal)
		#print(len(rules))
		AllRules.extend(rules)
	return AllRules


def getDistinctRulesCount(AllRules):
	distinctRules = set(AllRules)
	return len(distinctRules)

def getFrequentRules(AllRules):
	Rules_count = {}
	for rule in AllRules:
		if rule in Rules_count:
			Rules_count[rule]+=1
		else:
			Rules_count[rule]=1

	frequentRules = sorted(Rules_count, key=Rules_count.__getitem__, reverse=True)[0:10]
	frequentRulesCount = []

	for frequentRule in frequentRules:
		frequentRulesCount.append((frequentRule, Rules_count[frequentRule])) 
	
	return frequentRulesCount

def getMostDiverse(sentences):
	TagRule = {}
	for sentence in sentences:
		sentence.getRulesByTagExceptRoot(TagRule)

	TagRuleCount = {}
	for tag in TagRule:
		TagRuleCount[tag] = len(set(TagRule[tag]))

	mostDiverseTag = sorted(TagRuleCount, key=TagRuleCount.__getitem__, reverse=True)[0]
	
	#print(mostDiverseTag,TagRuleCount[mostDiverseTag])
	#print(TagRuleCount)

	return mostDiverseTag,TagRuleCount[mostDiverseTag]




def runTask_i(brown):
	sentences = getSentenceTrees(brown)
	sentences = sentences[1:len(sentences)]
	
	AllRules = getAllRules(sentences,True)
	distinctRules = getDistinctRulesCount(AllRules)
	print('Distinct rules = %s'% (distinctRules,))

	AllRulesWithOutNONTerminal = getAllRules(sentences,False)
	frequentRules = getFrequentRules(AllRulesWithOutNONTerminal)
	print('Ten frequent rules:')
	print(frequentRules)	

	print('Most diverse non-terminal:')
	mostDiverseTag = getMostDiverse(sentences)	
	print(mostDiverseTag)		



def runTask_ii(brown):
	pass
 

brown =  brownfile
brown = Snapshotbrownfile
runTask_i(brown)


print("ended")



