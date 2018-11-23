import math
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        num = round(math.log(n, 3))
        if math.pow(3, num) == n:
            return True
        else:
            return False
"""
大神的解法
"""
class Solution1:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0