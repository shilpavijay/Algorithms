# - Implements LIFO - Last In First out
# - Operations: Add, Remove, Count

class Queue:
	def __init__(self,l):
		self.queue = l
	def count(self):
		print("Queue length: "+ str(len(self.queue)))
	def add(self,element):
		self.queue.append(element)
		print("Added: " + str(element))
		print(self.queue)
	def remove(self):
		try:
			print("Removed: "+ str(self.queue[0]))
			self.queue = self.queue[1:]
			print(self.queue)
			return 1
		except:
			print("Queue is Empty")
			return 0

# Usage:
s = Queue([])
s.add(10)
s.add(20)
s.add(30)
s.count()
s.remove()
s.remove()
s.remove()
s.remove()

# Output:
# Added: 10
# [10]
# Added: 20
# [10, 20]
# Added: 30
# [10, 20, 30]
# Queue length: 3
# Removed: 10
# [20, 30]
# Removed: 20
# [30]
# Removed: 30
# []
# Queue is Empty