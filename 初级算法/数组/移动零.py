import collections
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = list(collections.Counter(nums).items())[0]
        if a[0] != 0:
            pass
        else:
            for i in range(a[1]):
                nums.remove(0)
            for i in range(a[1]):
                nums.append(0)