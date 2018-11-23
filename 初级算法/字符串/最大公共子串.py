a = "abc"
b = "dabcer"

class Solution:
    def maxCommonStr(self, s1, s2):
        if len(s1) == 0 or len(s2) == 0:
            return ""
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        matrix = [[0] * (len(s1) + 1)] * (len(s2) + 1)
        count = 0
        pos = 0
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    matrix[i + 1][j + 1] = matrix[i][j] + 1
                    if matrix[i + 1][j + 1] > count:
                        count = matrix[i + 1][j + 1]
                        pos += 1
        return s1[count - pos:count], count

