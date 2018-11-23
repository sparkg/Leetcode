"""
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows < 1:
        return []
    list_ = []
    for i in range(1, numRows + 1):
        list = []
        if i == 1:
            list = [1]
        elif i == 2:
            list = [1,1]
        else:
            list.append(1)
            for j in range(len(list_[-1]) - 1):
                list.append(list_[-1][j] + list_[-1][j+1])
            list.append(1)
        list_.append(list)
    return list_

print(generate(5))