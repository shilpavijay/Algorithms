#Problem Description:
# Given is a Linked List with the data Structure having an Integer and a pointer to the next element. 
# The implementation of the data structure is given below

class IntList(object):
  value = 0
  next = None

#Write code to traverse through the Linked List to find the total number of /values stored in the linked list

############traversal#############

def solution(L):
	root = L.value
	pointer = L.next
	count=1
	while pointer != None:
		pointer = pointer.next
		count +=1
	return count