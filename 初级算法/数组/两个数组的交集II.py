class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        list_ = []
        if len(set(nums1)) < len(set(nums2)):
            for i in nums1:
                if i in nums2:
                    list_.append(i)
                    nums2.remove(i)
        elif len(set(nums1)) > len(set(nums2)):
            for i in nums2:
                if i in nums1:
                    list_.append(i)
                    nums1.remove(i)
        elif len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1:
                    list_.append(i)
                    nums1.remove(i)
        elif len(nums1) < len(nums2):
             for i in nums1:
                if i in nums2:
                    list_.append(i)
                    nums2.remove(i)
        else:
            list_ = nums1
        return list_
"""
大神的解法
"""
import collections
class Solution1:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list((collections.Counter(nums1)&collections.Counter(nums2)).elements())