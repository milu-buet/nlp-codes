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



				




a = getSentenceTrees(Snapshotbrownfile)
a[1].printExceptRoot()
print("ended")



