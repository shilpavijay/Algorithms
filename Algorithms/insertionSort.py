#Insertion Sort
#Time Complexity: 
#Avg and worst case: O^n
#Best case: n

def insertionSort(lst):
	n = len(lst)
	for i in range(1,n):
		v = lst[i]
		j = i - 1
		while j >= 0 and lst[j] > v:
			lst[j+1] = lst[j]
			j -=1
		lst[j+1] = v
		print(lst)
	return lst


l=[89,34,12,55,1,3,5]
print(l)
insertionSort(l)