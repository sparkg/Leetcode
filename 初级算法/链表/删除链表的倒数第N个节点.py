# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        len_ = self.length(head)
        if n > len_:
            return head
        if len_ == 1 and n == 1:
            return None
        if len_ == n:
            return head.next
        node = head
        for i in range(len_ - n - 1):
            node = node.next
        node.next = node.next.next
        return head

    def length(self, head):
        length = 0
        while head.next is not None:
            length += 1
            head = head.next
        return length + 1
