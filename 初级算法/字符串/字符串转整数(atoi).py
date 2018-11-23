class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #排除极特殊情况
        if str == "" or str == "+" or str == "-" or str == " ":
            return 0
        #去除前面的空格
        for i in range(len(str)):
            if str[i] != " ":
                str = str[i:]
                break
        #去除正负号
        neg = 0
        if str[0] == "-" or str[0] == "+":
            if str[0] == "-":
                neg = 1
            str = str[1:]
        #去除非数字
        if str[0].isdigit() == False:
            return 0
        #去除数字后面的部分
        for i in range(len(str)):
            if str[i].isdigit() == False:
                str = str[:i]
                break
        str = int(str)
        if neg == 1:
            str = -str
        if str < -2 ** 31:
            return -2 ** 31
        elif str > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return str