class Node:
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None
		self.level = None
	def __str__(self):
		return(str(self.key))


class Btree:
	def __init__(self):
		self.root = None

	def createTree(self,info):
		if self.root == None:
			self.root = Node(info)
		else:
			current = self.root	
			while 1:
				if info < current.key:
					if current.left:
						current = current.left
					else:
						current.left = Node(info)
						break
				elif info > current.key:
					if current.right:
						current = current.right
					else:
						current.right = Node(info)
						break
				else:
					break


	def preOrder(self,node):
		if node is not None:
			print(node.key)
			self.preOrder(node.left)
			self.preOrder(node.right)

	def inOrder(self,node):
		if node is not None:
			self.inOrder(node.left)
			print(node.key)
			self.inOrder(node.right)

	def postOrder(self,node):
		if node is not None:
			self.postOrder(node.left)
			self.postOrder(node.right)
			print(node.key)

	def DFS(self,search,node):
		if node is not None:
			key = node.key
			print(key)
		
			if key == search:
				print("Found")
			elif search < key:
				self.DFS(search,node.left)
			else:
				self.DFS(search,node.right)
		else:
			print("Not Found")

if __name__ == "__main__":
	# Creating the BTree:
	bt = Btree()
	array = [8,12,3,1,4,18,20]
	for i in array:
		bt.createTree(i)
	print("\nPre-Order Traversal: ")
	bt.preOrder(bt.root)
	print("\nIn-Order Traversal: ")
	bt.inOrder(bt.root)
	print("\nPost-Order Traversal")
	bt.postOrder(bt.root)
	print("\nDepth First Search. \nWill Return 'Found' or 'Not Found' dependind on the presence of the given element. \nAlso prints the order of search:")
	bt.DFS(2,bt.root)