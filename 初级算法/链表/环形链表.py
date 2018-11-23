# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

"""
判断环节点入口：
让快指针在相遇之后回到头
然后快指针每一次走一步
和慢指针相遇的时候就是环节点入口
"""
