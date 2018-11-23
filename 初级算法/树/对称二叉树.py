# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.symmetric(root.left, root.right)

    def symmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is not None and right is not None and left.val == right.val:
            l = self.symmetric(left.left, right.right)
            r = self.symmetric(left.right, right.left)
            return l and r
        else:
            return False
