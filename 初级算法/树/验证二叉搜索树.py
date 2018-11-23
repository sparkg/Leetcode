# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        bool_, _, __ = self.ValidBST(root)
        if bool_ is True:
            return True
        else:
            return False

    def ValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool minVal maxVal
        """
        if root is None:
            return True, None, None
        if root.left is None and root.right is None:
            return True, root.val, root.val
        if root.left is None:
            bool_, min_, max_ = self.ValidBST(root.right)
            if bool_ is False:
                return False, None, None
            if root.val < min_:
                return True, root.val, max_
            else:
                return False, None, None
        if root.right is None:
            bool_, min_, max_ = self.ValidBST(root.left)
            if bool_ is False:
                return False, None, None
            if max_ < root.val:
                return True, min_, root.val
            else:
                return False, None, None
        bool_, min_, max_ = self.ValidBST(root.left)
        bool__, min__, max__ = self.ValidBST(root.right)
        if bool_ is False or bool__ is False:
            return False, None, None
        if max_ < root.val and root.val < min__:
            return True, min_, max__
        else:
            return False, None, None
