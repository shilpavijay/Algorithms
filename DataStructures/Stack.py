# - Implements FIFO - First In First out
# - Operations: Push, Pop, Count

class Stack:
	def __init__(self,l):
		self.stack = l
	def count(self):
		print("Stack count: "+ str(len(self.stack)))
	def push(self,element):
		self.stack.append(element)
		print("Pushed: " + str(element))
		print(self.stack)
	def pop(self):
		try:
			print("Popped: "+ str(self.stack[-1]))
			print(self.stack.pop())
			return 1
		except:
			print("Stack is Empty")
			return 0

# Usage:
s = Stack([])
s.push(10)
s.push(20)
s.push(30)
s.count()
s.pop()
s.pop()
s.pop()
s.pop()

# Output:
# Pushed: 10
# [10]
# Pushed: 20
# [10, 20]
# Pushed: 30
# [10, 20, 30]
# Stack count: 3
# Popped: 30
# [10, 20]
# Popped: 20
# [10]
# Popped: 10
# []
# Stack is Empty