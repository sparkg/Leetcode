class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        cur_str = ""
        max_str = ""
        for item in s:
            if item not in cur_str:
                cur_str += item
            else:
                if len(cur_str) == 1:
                    cur_str = item
                else:
                    cur_str = self.find(cur_str, item) + item
            if len(cur_str) > len(max_str):
                max_str = cur_str
        return len(max_str)

    def find(self, s, item):
        index = s.find(item)
        return s[index + 1:]