class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val >= l2.val:
            l1, l2 = l2, l1
        node1 = l1
        node2 = l2
        if node1.next is None:
            node1.next = node2
            return l1
        while node2 is not None:
            if node1.val <= node2.val and (node1.next == None or node1.next.val >= node2.val):
                temp = node2
                node2 = node2.next
                self.insertNode(node1, temp)
            else:
                node1 = node1.next
        return l1

    def insertNode(self, node1, node2):
        # node1为原链表
        # node2为要插入的节点
        node2.next = node1.next
        node1.next = node2
