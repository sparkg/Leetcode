"""
超出时间限制的分治法
可能是因为sum
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        """
        将问题分为左半边最大子序，右半边最大子序，中间最大子序
        """
        index = len(nums)//2
        max_left = nums[index - 1]
        max_right = nums[index]
        for i in range(index - 1, -1 ,-1):
            if sum(nums[i:index]) > max_left:
                max_left = sum(nums[i:index])
        for i in range(index, len(nums)):
            if sum(nums[index:i+1]) > max_right:
                max_right = sum(nums[index:i+1])
        """
        中间最大子序为以分界点为界，左右两边临近分界点最大子序和的和
        若有其中一边是负的，也不影响最后的结果
        """
        max_mid = max_left + max_right
        return max(self.maxSubArray(nums[0:index]), self.maxSubArray(nums[index:]), max_mid)


class Solution1:
    """
    动态规划
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        max_sum = nums[0]
        cur_sum = nums[0]
        for item in nums[1:]:
            if cur_sum < 0:
                cur_sum = item
            else:
                cur_sum += item
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum
"""
更简洁的动态规划
"""
class Solution2:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        max_sum = nums[0]
        cur_sum = nums[0]
        for item in nums[1:]:
            cur_sum = max(cur_sum + item, item)
            max_sum = max(cur_sum, max_sum)
        return max_sum