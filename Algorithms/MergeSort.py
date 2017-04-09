import math

def mergesort(l):
	n = len(l)
	if n > 1:
		pointer = math.floor(n/2)
		A = l[:pointer]
		B = l[pointer:]
		mergesort(A)
		mergesort(B)
		merge(A,B,l)

def merge(A,B,l):
	p = len(A)
	q = len(B)
	i=j=k=0

	while i<p and j<q:
		if A[i]<=B[j]:
			l[k] = A[i]
			i += 1
		else:
			l[k] = B[j]
			j += 1
		k += 1

	#Handle the rest of the list items:
	if i == p:
		l[k:] = B[j:]
	else:
		l[k:] = A[i:]



#Sample usage: 
l=[233,34,1,2,32,12,11,37,1,322,100,1200,1024,1.23,1.20,89.912]
mergesort(l)
print(l)



