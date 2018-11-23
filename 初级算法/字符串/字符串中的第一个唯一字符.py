class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic_no_rep = {}
        dic_rep={}
        for index, item in enumerate(s):
            if item in dic_no_rep:
                dic_no_rep.pop(item)
                dic_rep[item] = index
            if item not in dic_rep:
                dic_no_rep[item] = index
        if len(dic_no_rep) == 0:
            return -1
        return min(dic_no_rep.values())

"""
大神的解法
"""


class Solution1:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = len(s)
        for c in set(s):
            c_s = s.find(c)
            c_r = s.rfind(c)

            if c_s == c_r and c_s != -1:
                ans = min(ans, c_s)

        if ans < len(s):
            return ans
        else:
            return -1