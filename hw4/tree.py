# Natural Language Processing, Spring'18
# Assignment #4
# Md Lutfar Rahman
# mrahman9@memphis.edu



class BrownNode(object):
	"""docstring for BrownNode"""
	def __init__(self, tag, level):
		super(BrownNode, self).__init__()
		self.tag = tag
		self.level = level
		self.parent =None
		self.children = []

	def setParent(self,parent):
		self.parent = parent

	def addChild(self,child):
		self.children.append(child)
		child.setParent(self)

	def getLevel(self):
		return self.level

	def getAncestorByLevel(self,level):
		pNode = self
		while(pNode.level >= level and pNode.parent is not None):
			pNode = pNode.parent
		return pNode

	def printExceptRoot(self):
		if len(self.children) > 0 and len(self.children[0].children) > 0:
			self.children[0].children[0].printChildren()

	def hasNonLeafNodes(self):
		for child in self.children:
			if len(child.children) > 0:
				return True
		return False


	def printChildren(self):
		print('%s -> '%(self.tag),end='')
		#print(len(self.children))
		for child in self.children:
			if len(child.children) > 0:
				print('%s '%(child.tag),end='')

		print('')

		for child in self.children:
			if len(child.children) > 0 and child.hasNonLeafNodes():
				child.printChildren()

		#print('')

	def getRulesExceptRoot(self, WithNONTerminal = True):
		if len(self.children) > 0 and len(self.children[0].children) > 0:
			return self.children[0].children[0].getRules(WithNONTerminal)
		return []

	def getRules(self, WithNONTerminal = True):
		rules = []
		schild = ''
		if(WithNONTerminal):
			schild = '%s -> '%(self.tag)
		for child in self.children:
			if len(child.children) > 0:
				#print('%s '%(child.tag),end='')
				schild = schild + '%s '%(child.tag)

		schild = schild.strip()

		rules.append(schild)
		for child in self.children:
			if len(child.children) > 0 and child.hasNonLeafNodes():
				crules = child.getRules(WithNONTerminal)
				rules.extend(crules)

		return rules

	def getRulesByTagExceptRoot(self,TagRule):
		if len(self.children) > 0 and len(self.children[0].children) > 0:
			self.children[0].children[0].getRulesByTag(TagRule)

	def getRulesByTag(self,TagRule):
		schild = ''
		for child in self.children:
			if len(child.children) > 0:
				schild = schild + '%s '%(child.tag)
		schild = schild.strip()

		if self.tag not in TagRule:
			TagRule[self.tag] = []
		
		TagRule[self.tag].append(schild)
		for child in self.children:
			if len(child.children) > 0 and child.hasNonLeafNodes():
				child.getRulesByTag(TagRule)
				



	def show(self):
		return "%s,%s"%(self.tag,self.level,)
