# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pointer = None
        while head is not None:
            temp = head
            head = head.next
            temp.next = pointer
            pointer = temp
        return pointer