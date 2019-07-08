# Binary Search Tree with Pre-order, In-order, Post-order traversals
# Elements: Key, Prev, Next
# Operations: insert, inOrder, preOrder, postOrder

class BST:
	def __init__(self,key,left,right):
		self.key = key
		self.left = left
		self.right = right

	def insert(self,el):
		n = BST(el,None,None)
		if self.key:
			if el < self.key:
				if self.left is None:
					self.left = n
				else:
					self.left.insert(el)
			elif el > self.key:
				if self.right is None:
					self.right = n
				else:
					self.right.insert(el)
			else:
				self.key = el

	def inOrder(self):
		if self.left:
			self.left.inOrder()
		print(self.key)
		if self.right:
			self.right.inOrder()

	def preOrder(self):
		print(self.key)
		if self.left:
			self.left.preOrder()
		if self.right:
			self.right.preOrder()

	def postOrder(self):
		if self.left:
			self.left.postOrder()
		if self.right:
			self.right.postOrder()
		print(self.key)



#Usage:
tree = BST(12,None,None)
tree.insert(10)
tree.insert(20)
tree.insert(4)
print("In-order Traversal: ")
tree.inOrder()
print("Pre-order Traversal: ")
tree.preOrder()
print("Post-order Traversal: ")
tree.postOrder()


#Output:
# In-order Traversal:
# 4
# 10
# 12
# 20
# Pre-order Traversal:
# 12
# 10
# 4
# 20
# Post-order Traversal:
# 4
# 10
# 20
# 12