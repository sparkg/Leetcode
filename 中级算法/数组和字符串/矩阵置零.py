class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col_list = []
        row_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    col_list.append(j)
                    row_list.append(i)
        col_list = list(set(col_list))
        row_list = list(set(row_list))
        for item in row_list:
            matrix[item] = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for item in col_list:
                matrix[i][item] = 0
