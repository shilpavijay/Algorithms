#RingBuffer or Circular Queue:
class RingBuffer:
	def __init__(self,buffersize):
		self.size = buffersize
		self.queue = [None for i in range(self.size)] #initialize the buffer
		self.front = self.rear = -1 # initialize the pointers

	def enqueue(self,element):
		print("\nEnqueue: " + str(element))
		if self.front == (self.rear + 1) % self.size: #Queue full
			print("Queue is full. No more insertions possible.")
			return False
		elif self.front == -1: #first insertion
			self.front = self.rear = 0
			self.queue[self.rear] = element
		else:   #next position
			self.rear = (self.rear + 1) % self.size
			self.queue[self.rear] = element
		print(self.queue)
		print("Front: "+str(self.front))
		print("Rear: "+str(self.rear))

	def dequeue(self):
		print("\nDequeue: ")
		if self.front == -1: #Queue Empty
			return False
		elif(self.front == self.rear):  #when single element is left
			element = self.queue[self.front]
			self.queue[self.front] = None
			self.front = self.rear = -1
		else:
			element = self.queue[self.front]
			self.queue[self.front] = None
			self.front = (self.front + 1) % self.size
		print(self.queue)
		print("Front: "+str(self.front))
		print("Rear: "+str(self.rear))
		return "Element Returned: " + str(element)

#Usage:
ring = RingBuffer(5)
ring.enqueue(10)
ring.enqueue(20)
ring.enqueue(30)
ring.enqueue(40)
ring.enqueue(50)
ring.enqueue(60)
ring.dequeue()
ring.dequeue()
ring.dequeue()
ring.dequeue()
ring.dequeue()