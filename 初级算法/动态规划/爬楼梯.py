class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        str_list = []
        for i in range(n // 2 + 1):
            s = ""
            s += "2" * i
            s += "1" * (n - i * 2)
            str_list.append(s)
        for item in str_list:
            num_1 = item.count("1")
            num += self.combine(num_1, len(item))
        return int(num)

    def combine(self, num_1, num_2):
        """
        :param num_1: small num
        :param num_2: large num
        :return: combine num_1 num_2
        """
        a = 1
        b = 1
        _num_1 = num_1
        _num_2 = num_2
        for i in range(num_1):
            a *= _num_2
            b *= _num_1
            _num_2 -= 1
            _num_1 -= 1
        return int(a / b)
