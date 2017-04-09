def BubbleSort(l):
	for num in range((len(l)-1),0,-1):
		for i in range(num): 
			if l[i] > l[i+1]:
				l[i],l[i+1] = l[i+1],l[i]  #swap
			i += 1
	return l


lst = [87,34,1,2,344,23,9,12,3,455,21]	
print(lst)
print('Sorted List: ' + str(BubbleSort(lst)))