class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if "" in strs or len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        s = ""
        min_length = len(strs[0])
        for item in strs:
            if len(item) < min_length:
                min_length = len(item)
        for i in range(min_length + 1):
            for item in strs:
                if s != item[:i]:
                    return s[:-1]
            if i == min_length:
                break
            s += strs[0][i]
        return s

"""
学到的知识：
min()函数可以接受key
"""
"""
大神的解法
"""
class Solution1:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest=min(strs,key=len)
        for x, y in enumerate(shortest):
            for s in strs:
                if s[x]!=y:
                    return shortest[:x]
        return shortest