"""
思路为：首先排序，从头到倒数第三个元素循环
取该元素后一个为left，最后一个元素为right
求和之后如果为0就添加进数组，如果不为0，则根据和的大小调整左边或右边指针
具体为如果和大于零，则右边指针减一；如果和小于零，则右边指针加一
在排除重复元素方面
针对i排除重复元素：
如果nums[i]和之前的元素相同，则向后找，避免重复
在求得和为零之后继续寻找left和right时，为避免重复
也应该在寻找指针时和之前的值比较，如果重复则继续
"""
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #处理数组大小小于2的特殊情况
        if len(nums) <= 2:
            return []
        #若数组大小为3，则直接计算
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
        return_list = []
        nums.sort()
        #从第一个元素到倒数第三个元素
        for i in range(len(nums) - 2):
            left = i+1
            right = len(nums) - 1
            #排除nums[i]的重复
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ == 0:
                    return_list.append([nums[i] , nums[left] , nums[right]])
                    left += 1
                    right -= 1
                    #排除找到符合条件的数组之后，后面找到的数组和前面的重复
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif sum_ > 0:
                    right -= 1
                else:
                    left += 1
        return return_list