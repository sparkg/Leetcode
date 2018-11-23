"""
函数官方已经给好，不需要自己定义
"""
def isBadVersion(num):
    pass
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while end - start > 1:
            mid = (end + start) // 2
            if isBadVersion(mid) is False:
                #右边
                start = mid
            elif isBadVersion(mid) is True:
                #左边
                end = mid
        if isBadVersion(start) is True:
            return start
        else:
            return end