# 1.
# Sort the array such that odd elements are to the left followed by even elements to the right

def oddeven(l):
    return sorted(l,key=lambda x: x%2)

print(oddeven([1,2,3,4,5,6,7,8]))

# 2.
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
#The first node is considered odd, and the second node is even, and so on.
#Note that the relative order inside both the even and odd groups should remain as it was in the input.
#You must solve the problem in O(1) extra space complexity and O(n) time complexity.

