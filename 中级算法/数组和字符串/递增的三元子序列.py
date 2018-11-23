class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small = float("inf")
        mid = float("inf")
        for item in nums:
            if item > mid:
                return True
            if item <= small:
                small = item
            else:
                mid = item
        return False
