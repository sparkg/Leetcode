# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root_val = preorder[0]
        root_index = inorder.index(root_val)
        len_left = root_index
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:len_left+1], inorder[:len_left])
        root.right = self.buildTree(preorder[1+len_left:], inorder[1+len_left:])
        return root