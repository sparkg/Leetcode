class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_ = self.split(s)
        dict_ = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
                 "CD": 400, "CM": 900}
        num = 0
        for item in list_:
            num += dict_[item]
        return num

    def split(self, s):
        list_ = []
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                list_.append(s[i])
            elif s[i:i + 2] == "IV" or s[i:i + 2] == "IX" or s[i:i + 2] == "XL" or s[i:i + 2] == "XC" or s[
                                                                                                         i:i + 2] == "CD" or s[
                                                                                                                             i:i + 2] == "CM":
                list_.append(s[i:i + 2])
                i += 1
            else:
                list_.append(s[i])
            i += 1
        return list_
