class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s[-1:-len(s)-1:-1]
        return a

"""
大神的解法
"""
class Solution1:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]