# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
思路：分别摘下奇数和偶数的节点，然后再拼起来
"""
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None or head.next.next is None:
            return head
        odd = new_head = head
        even = head.next
        even_head = even
        while odd.next.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            if odd.next is None:
                break
        odd.next = even_head
        return new_head
