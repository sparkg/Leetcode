# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.isSame(s, t):
            return True
        if s.left is None and s.right is None:
            return False
        if s.left is None:
            return self.isSubtree(s.right, t)
        if s.right is None:
            return self.isSubtree(s.left, t)
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val == b.val:
            l = self.isSame(a.left, b.left)
            r = self.isSame(a.right, b.right)
            return l and r
        return False