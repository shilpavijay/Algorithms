class Trie:
	def __init__(self,char):
		self.char = char
		self.children = []
		self.finish = False
		self.counter = 1

	def add(self,root,word):
		node = root
		for char in word:
			found = False
			for child in node.children:
				if child.char == char:
					child.counter += 1
					node = child
					found = True
					break
			if not found:
				newNode = Trie(char)
				node.children.append(newNode)
				node = newNode
		node.finish = True

	def find_prefix(self,prefix):
		node = root
		if not root.children:
			return False,0
		for char in prefix:
			charNotFound = True
			for child in node.children:
				if child.char == char:
					charNotFound = False
					node = child
					break
			if charNotFound:
				return False, 0
		return True, node.counter


if __name__ == "__main__":
    root = Trie('*')
    root.add(root, "hackathon")
    root.add(root, 'hack')

    print(root.find_prefix('hac'))
    print(root.find_prefix('hack'))
    print(root.find_prefix('hackathon'))
    print(root.find_prefix('ha'))
    print(root.find_prefix('hammer'))