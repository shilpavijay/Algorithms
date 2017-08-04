""" Counting Sort """

"""

In Counting sort, the frequencies of distinct elements of the array to be sorted is counted 
and stored in an auxiliary array, by mapping its value as an index of the auxiliary array. 

Time Complexity: O(N + K) where N is the number of elements in the given array. N is the number 
of elements in the Auxiliary Array; in other words, it is the max element in the given array.

"""

import functools as ft

def count_sort(Arr):
  sortedArr = []
  K, j = 0, 0
  
  for i in Arr:
    K = max(K, i)
    
  Aux = [0 for i in range(0, K+1)]
  
  for a in Arr:
    Aux[a] += 1
    
  for i in range(0,len(Aux)):
    tmp = Aux[i]
    lst = [i for j in range(0,tmp)]
    if lst:
      sortedArr.append(lst)
  return ft.reduce(lambda a,b: a+b, sortedArr)
  
if __name__ == "__main__":
  print(count_sort([5,2,9,5,2,3,5]))