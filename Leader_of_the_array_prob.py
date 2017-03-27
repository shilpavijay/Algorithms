#Problem Description:
#Given is a sorted non-empty array of non-negetive integers.
#Leader of the array is the value occurring in more than half of the elements in the Array
#i.e Return the number which occurs more than half times 
#in the array. if no element occurs more than half the times, return -1.

#Example:
#If the array is [2,2,2,2,2,3,4,4,5,6] return -1
#for the array: [2,2,2,2,3,4] return 2

def solution(A):
    n = len(A)
    L =  A
    print("list: " + str(L))
    count = 0
    pos = n // 2
    # print("pos: " + str(pos))
    candidate = L[pos]
    # print("picked element: " + str(candidate))
    for i in range(0, n):
        if (L[i] == candidate):
            count = count + 1
    # print('count: '+ str(count))
    if (count > pos):  
        return candidate
    print("Result:")
    return -1


print(solution([2,2,2,2,2,3,4,4,5,6]))