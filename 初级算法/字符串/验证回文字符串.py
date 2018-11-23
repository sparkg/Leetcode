class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = ""
        for i in s:
            if i.isalnum():
                a += i
        a = a.lower()
        for i in range(len(a)//2):
            if a[i] != a[-(i+1)]:
                return False
        return True