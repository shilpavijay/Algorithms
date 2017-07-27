""" TERNARY SEARCH """

"""
Ternary Search is a divide and conquer Algorithm similar to binary search.  In this case, the array is divided into three parts. After each iteration it neglects 1/3 part of the array. The array is to be first sorted.
Complexity: O(log N)

"""
import logging

def ternarySearch(lst,l,r,element):
  if r>=l:
    mid1, mid2 = l + ((r - l)//3), r - ((r - l)//3)

    if element == lst[mid1]:
      return mid1
    if element == lst[mid2]:
      return mid2
    if element < lst[mid1]:
      return ternarySearch(lst,l,mid1-1,element)
    elif element > lst[mid2]:
      return ternarySearch(lst,mid2+1,r,element)
    else:
      return ternarySearch(lst,mid1+1,mid2-1,element)
  else:
    return "Element not found"
  

if __name__ == "__main__":
  logging.basicConfig(filename='ternarysrc.log', filemode='w', 
                      level=logging.DEBUG)

  lst = [2,3,5,6,8,9,12,13,14]
  logging.info(lst)  
  print("Result: ")                              
  print(ternarySearch(lst,0,len(lst)-1,14)) 
  