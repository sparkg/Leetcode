class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)-1):
            if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                return nums[i]
        if nums[0] == nums[1]:
            return nums[-1]
        else:
            return nums[0]
"""
大神的解法
"""
class Solution1:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums)))*2 - sum(nums)