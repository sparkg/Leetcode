class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_ = []
        if len(nums) < 2:
            return list_
        for index, item in enumerate(nums):
            if target - item in nums:
                if target - item == item and nums.count(item) == 1:
                    continue
                else:
                    list_.append(index)

        return list_
"""
大神的解法
"""
class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if (target - num) in dic:
                return i,dic[target - num]
            dic[num] = i