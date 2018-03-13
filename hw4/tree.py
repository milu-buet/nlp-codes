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


	def show(self):
		return "%s,%s"%(self.tag,self.level,)
