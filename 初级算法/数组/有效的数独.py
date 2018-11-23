import numpy as np
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #rule 1 no duplicate nums in rows
        for list_ in board:
            if list_.count(".") != 0:
                if 9 - list_.count(".") != len(set(list_)) - 1:
                    return False
            if list_.count(".") == 0:
                if len(set(list_)) != 9:
                    return False
        board = np.array(board)
        # rule 2 no duplicate nums in cols
        for i in range(9):
            if list(board[:,i]).count(".") != 0:
                if 9 - list(board[:,i]).count(".") != len(set(list(board[:,i]))) - 1:
                    return False
            if list(board[:,i]).count(".") == 0:
                if len(set(list(board[:,i]))) != 9:
                    return False
        #rule 3 no duplicate nums in 3*3
        list_ = []
        for i in range(1,8,3):
            for j in range(1,8,3):
                for k in range(-1,2):
                    for l in range(-1,2):
                        list_.append(board[i+k][j+l])
                if 9 - list_.count(".") != len(set(list_)) - 1:
                    return False
                list_ = []
        return True

"""
大神的解法
"""


class Solution1:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        #         # check row
        #         for row in board:
        #             rowStr = ''
        #             for ch in row:
        #                 if ch in rowStr:
        #                     return False
        #                 if ch != '.':
        #                     rowStr += ch

        #         # check column
        #         for i in range(9):
        #             columnStr = ''
        #             for j in range(9):
        #                 ch = board[j][i]
        #                 if ch in columnStr:
        #                     return False
        #                 if ch != '.':
        #                     columnStr += ch

        #         # chech grid
        #         for center in [ (i, j) for i in range(1, 9, 3) for j in range(1, 9, 3)]:
        #             points = [ (i, j) for i in range(center[0]-1, center[0]+2) for j in range(center[1]-1, center[1]+2)]
        #             gridStr = ''
        #             for point in points:
        #                 ch = board[point[0]][point[1]]
        #                 if ch in gridStr:
        #                     return False
        #                 if ch != '.':
        #                     gridStr += ch

        #         return True

        Grid, Col, Row = [''] * 9, [''] * 9, [''] * 9

        for idx, row in enumerate(board):
            for i, ch in enumerate(row):
                if ch != '.':
                    GridIndx = idx // 3 * 3 + i // 3
                    if ch in Row[idx] or ch in Col[i] or ch in Grid[GridIndx]:
                        print(ch, Grid, Col, Row)
                        return False
                    Row[idx] += ch
                    Col[i] += ch
                    Grid[GridIndx] += ch

        return True