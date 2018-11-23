class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set([i for i in range(len(nums) + 1)])
        return list(a.difference(set(nums)))[0]

"""
大神的解法
"""
class Solution1:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        n = len(nums)
        return n * (n+1) // 2 - s