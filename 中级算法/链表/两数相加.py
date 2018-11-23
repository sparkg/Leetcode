# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        需要考虑的情况有：两数不一样长  加完之后仍然有进位
        """
        root = ListNode((l1.val+l2.val)%10)
        count = (l1.val+l2.val) // 10
        node = root
        while l1.next is not None and l2.next is not None:
            l1 = l1.next
            l2 = l2.next
            temp = ListNode((l1.val+l2.val+count) % 10)
            count = (l1.val+l2.val+count) // 10
            node.next = temp
            node = temp
        if l1.next is not None:
            while l1.next is not None:
                l1 = l1.next
                temp = ListNode((l1.val + count) % 10)
                count = (l1.val + count) // 10
                node.next = temp
                node = temp
        elif l2.next is not None:
            while l2.next is not None:
                l2 = l2.next
                temp = ListNode((l2.val + count) % 10)
                count = (l2.val + count) // 10
                node.next = temp
                node = temp
        if count != 0:
            temp = ListNode(count)
            node.next = temp
            node = temp
        return root