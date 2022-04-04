#Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        first,sec = dummy,dummy
        for i in range(0,n+1): # move first to n nodes. keep first and sec n nodes apart
            first = first.next
        while (first != None):
            first = first.next
            sec = sec.next
            
        sec.next = sec.next.next
        return dummy.next