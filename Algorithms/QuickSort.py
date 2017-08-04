""" Quicksort """

"""
Quicksort is a divide and conquer algorithm which sorts the given array 
with an average time complexity of O(NlogN).

A pivot is selected (mostly the first element of the array) and all the 
elements less than the pivot are moved to the left of the pivot. The process 
is again continued by sorting the left and right part of the Array repeatedly 
until all the elements have undergone sorting. 

Here i denotes the boundary between elements less than the pivot element and those 
greater than it. j denotes the boundary between partition and unpartitioned part of the Array

"""

def partition(Arr,strt,end):
  i = strt + 1
  pivot = Arr[strt]
  for j in range(strt+1,end+1):
    if Arr[j] < pivot:
      Arr[i], Arr[j] = Arr[j], Arr[i]
      i += 1
  Arr[strt], Arr[i-1] = Arr[i-1], Arr[strt]
  return i-1
  
def quicksort(Arr,strt,end):
  if strt < end:
    piv_pos = partition(Arr,strt,end)
    quicksort(Arr,strt,piv_pos-1)
    quicksort(Arr,piv_pos+1,end)
  
if __name__ == '__main__':
  lst = [222, 12, 1 ,23, 211, 122, 600, 96, 34]
  print("Given List: " + str(lst))
  quicksort(lst,0,len(lst)-1)
  print("Sorted List: " +str(lst))
