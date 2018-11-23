class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict_ = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if len(digits) == 0:
            return res
        if len(digits) == 1:
            for i in range(len(dict_[digits])):
                res.append(dict_[digits][i])
            return res

        def backtrack(dig=digits, strs=""):
            if len(dig) == 1:
                for i in range(len(dict_[dig])):
                    temp = strs
                    temp += dict_[dig][i]
                    res.append(temp)
                return
            for j in range(len(dict_[dig[0]])):
                backtrack(dig[1:], strs + dict_[dig[0]][j])

        backtrack()
        return res
