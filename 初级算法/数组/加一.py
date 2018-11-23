class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_ = ""
        list_ = []
        for item in digits:
            str_ += str(item)
        str_ = int(str_)
        str_ += 1
        str_ = str(str_)
        for item in str_:
            list_.append(int(item))
        return list_