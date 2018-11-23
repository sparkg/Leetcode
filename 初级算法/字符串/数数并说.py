class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        s = "1"
        for i in range(n - 1):
            s = self.convert(self.split(s))
        return s

    def convert(self, list):
        s = ""
        for item in list:
            s += str(len(item))
            s += item[0]
        return s

    def split(self, str):
        list_ = []
        s = ""
        for item in str:
            if s == "" or item in s:
                s += item
            else:
                list_.append(s)
                s = item
        list_.append(s)
        return list_