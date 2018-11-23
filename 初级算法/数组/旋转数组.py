class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        for i in range(k):
            nums.append(nums[i])
        for i in range(k):
            del (nums[0])
        nums.reverse()
