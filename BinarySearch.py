import math

def BinSearch(A,key):
	l=0
	r=len(A)-1
	while l<=r:
		mid = (l+r)//2
		if key == A[mid]:
			return mid
		elif key < A[mid]:
			r = mid - 1
		else:
			l = mid + 1
	return -1



#Binary search works on a sorted list
lst = [1, 2, 3, 9, 12, 21, 23, 34, 87, 344, 455]
print(lst)
print(BinSearch(lst,21))