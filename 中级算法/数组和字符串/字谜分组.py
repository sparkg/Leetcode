"""
通过升序排列字符串的元素和字典，获得字符串的同字母异构列表
"""
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_map = {}
        result = []
        for item in strs:
            key = "".join(sorted(item))
            if key in str_map:
                str_map[key].append(item)
            else:
                str_map[key] = [item]
        for strlist in str_map.values():
            result.append(strlist)
        return result