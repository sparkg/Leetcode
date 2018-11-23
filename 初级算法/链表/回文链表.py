# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        len_ = self.length(head)
        if len_ == 1:
            return True
        list_ = []
        while head is not None:
            list_.append(head.val)
            head = head.next
        for i in range(len(list_) // 2):
            if list_[i] != list_[-(i + 1)]:
                return False
        return True

    def length(self, head):
        len_ = 0
        while head.next is not None:
            len_ += 1
            head = head.next
        return len_ + 1