class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        #在闭合的括号内，所有括号必须都闭合
        flagS = 0
        flagM = 0
        flagL = 0
        flag_list = []
        for item in s:
            if item == "(":
                flagS += 1
                flag_list.append("flagS")
            elif item == "[":
                flagM += 1
                flag_list.append("flagM")
            elif item == "{":
                flagL += 1
                flag_list.append("flagL")
            elif item == ")":
                if flagS == 0:
                    return False
                if flag_list[-1] != "flagS":
                    return False
                flagS -= 1
                flag_list = flag_list[:-1]
            elif item == "]":
                if flagM == 0:
                    return False
                if flag_list[-1] != "flagM":
                    return False
                flagM -= 1
                flag_list = flag_list[:-1]
            elif item == "}":
                if flagL == 0:
                    return False
                if flag_list[-1] != "flagL":
                    return False
                flagL -= 1
                flag_list = flag_list[:-1]
        if flagS == 0 and flagM == 0 and flagL == 0:
            return True
        else:
            return False

"""
大神的解法
"""
class Solution1:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        dic={")":"(","]":"[","}":"{"}
        for x in s:
            if x in dic.values():
                l.append(x)
            elif x in dic.keys():
                if l==[] or dic[x]!=l.pop():
                    return False
            else:
                return False
        return l==[]

