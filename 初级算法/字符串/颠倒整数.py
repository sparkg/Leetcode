class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = x
        if a == -2**31:
            return 0
        neg = 0
        if a < 0:
            neg = 1
            a = abs(a)

        a = str(a)
        a = a[::-1]
        a = int(a)
        if neg == 1:
            a = -a
        if a > 2**31 - 1 or a < -2**31:
            return 0
        return a