class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while ((i+1)<len(nums)) and (nums[i] == nums[i+1]) :
                del(nums[i+1])
        return len(nums)


if __name__ == "__main__":
    nums = [1,1,2,2,3,3,3,4]
    solution = Solution()
    print(solution.removeDuplicates(nums))
    print(nums)

