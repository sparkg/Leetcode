class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        def backtrack(num=nums,array=[]):
            if len(array) == len(nums):
                res.append(array)
                return
            for i in range(len(num)):
                if i == 0:
                    backtrack(num[1:], array+[num[0]])
                elif i == len(num) - 1:
                    backtrack(num[:-1], array+[num[-1]])
                else:
                    backtrack(num[:i]+num[i+1:], array+[num[i]])
        backtrack()
        return res