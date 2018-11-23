# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        new_root = root
        if new_root is None or new_root.left is None and new_root.right is None:
            return new_root
        if new_root.left is None:
            new_root.left = self.invertTree(new_root.right)
            new_root.right = None
            return new_root
        if new_root.right is None:
            new_root.right = self.invertTree(new_root.left)
            new_root.left = None
            return new_root
        new_root.left, new_root.right = self.invertTree(new_root.right), self.invertTree(new_root.left)
        return new_root