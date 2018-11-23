# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        list_ = []
        root_list = [root]
        if root is None:
            return list_
        while len(root_list) > 0:
            nums = []
            root_list_ = []
            for item in root_list:
                # 添加本层元素
                nums.append(item.val)
            list_.append(nums)
            for item in root_list:
                left = item.left
                right = item.right
                if left is not None:
                    root_list_.append(left)
                if right is not None:
                    root_list_.append(right)
            root_list = root_list_

        # 层次遍历
        return list_
