class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        set_ = []
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [nums, []]
        nums.sort()

        def backtrack(num = nums, route=[]):
            set_.append(route)
            if num == []:
                return
            for i in range(len(num)):
                if i < len(num) - 1:
                    backtrack(num[i+1:],route+[num[i]])
                else:
                    backtrack([],route+[num[i]])
        backtrack()
        return set_