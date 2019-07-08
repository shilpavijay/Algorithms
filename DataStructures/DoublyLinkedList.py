# Doubly-Linked List
# Elements: Key, Prev, Next
# Operations: display, append, remove

class Node:
	def __init__(self,key,prev,next):
		self.key = key
		self.prev = prev
		self.next = next

class DLL:
	head = None
	tail = None

	def display(self):
		print("Doubly Linked List: ")
		current_node = self.head
		while current_node is not None:	
			print(current_node.key)
			current_node = current_node.next
		print("*"*50)
	def append(self,key):
		n = Node(key,None,None)
		if self.head == None:
			self.head = self.tail = n
		else:
			n.prev = self.tail
			n.next = None
			self.tail.next = n
			self.tail = n

	def remove(self,el):
		cur = self.head
		while cur is not None:
			if cur.key == el:
				if cur.prev is None:
					self.head = cur.next
					self.head.prev = None
				elif cur.next is None:
					self.tail = cur.prev
					self.tail.next = None
				else:
					cur.prev.next = cur.next
					cur.next.prev = cur.prev
			cur = cur.next

#Usage:
dll = DLL()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.display()
dll.remove(20)
dll.display()

#Output:
# Doubly Linked List:
# 10
# 20
# 30
# 40
# **************************************************
# Doubly Linked List:
# 10
# 30
# 40
# **************************************************