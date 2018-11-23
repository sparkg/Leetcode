# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
思路：
首先确定链表是否相交，以及链表的长度
从两个链表根节点开始，直到最后的节点，长度加一，如果最后两个链表节点相等，说明有相交的节点
长链表先走长度差值的步数，然后两个链表指针跟进，直到相交，就找到了初始相交节点
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        node1, node2 = headA, headB
        lA = lB = 0
        while node1.next is not None:
            lA += 1
            node1 = node1.next
        while node2.next is not None:
            lB += 1
            node2 = node2.next
        if node1 != node2:
            return None
        node1, node2 = headA, headB
        if lA >= lB:
            for i in range(lA - lB):
                node1 = node1.next
        if lB > lA:
            for i in range(lB - lA):
                node2 = node2.next
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next
        return node1