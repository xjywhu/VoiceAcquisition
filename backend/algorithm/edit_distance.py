
def edit_distance(str1, str2):
    '''
            :type str1: str
            :type str2: str
            :rtype: int
    '''
    matrix = [[i+j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1] == str2[j-1]:
                d = 0
            else:
                d = 1
            matrix[i][j] = min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+d)
    return matrix[len(str1)][len(str2)]

def extended_edit_distance(str1, str2):
    matrix = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    id_matrix = [[None for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                d = 0
            else:
                d = 1
            lis = [matrix[i - 1][j - 1] + d, matrix[i - 1][j] + 1, matrix[i][j - 1] + 1]
            minNum = min(lis)
            idx = lis.index(minNum)
            matrix[i][j] = minNum
            if idx == 0:
                id_matrix[i][j] = (i - 1, j - 1)
            elif idx == 1:
                id_matrix[i][j] = (i - 1, j)
            else:
                id_matrix[i][j] = (i, j - 1)
    row = len(id_matrix)
    col = len(id_matrix[0])
    lis = []
    i = row - 1
    j = col - 1
    while i != 0 and j != 0:
        lis += [(i, j)]
        cell = id_matrix[i][j]
        i = cell[0]
        j = cell[1]
    lis += [(i, j)]
    lis.reverse()
    a = [-1 for i in range(len(str2))]
    b = [-1 for i in range(len(str1))]
    lastCell = lis[0]
    if lastCell != (0, 0):
        if lastCell == (0, 1):  # 右
            a[0] = 1
        elif lastCell == (1, 0):  # 下
            b[0] = 1
    for i in range(1,len(lis)):
        curCell = lis[i]
        dd = curCell[0] - lastCell[0]  # 向下的步数
        dr = curCell[1] - lastCell[1]  # 向右的步数
        if dd == 1 and dr == 1:  # 向右下走
            if matrix[lastCell[0]][lastCell[1]] == matrix[curCell[0]][curCell[1]]:
                a[curCell[1] - 1] = 0
                b[curCell[0] - 1] = 0
            else:
                a[curCell[1] - 1] = 0  # 不变
                b[curCell[0] - 1] = 2  # 修改
        elif dd == 1 and dr == 0:  # 向下走
            b[curCell[0] - 1] = 1
        elif dd == 0 and dr == 1:  # 向右走
            a[curCell[1] - 1] = 1
        lastCell = lis[i]
    maxlen = max(len(str1), len(str2))
    rate = 1 - matrix[len(str1)][len(str2)] / maxlen
    return rate, a, b  #, matrix, id_matrix

def get_similarity(str1,str2):
    distance = edit_distance(str1,str2)
    maxlen = max(len(str1),len(str2))
    ret = 1 - distance/maxlen
    return ret


def test_edit_distance(str1,str2): # str2是上边的,str1是左边的
    matrix = [[i+j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    id_matrix = [[None for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                d = 0
            else:
                d = 1
            lis = [matrix[i - 1][j - 1] + d,matrix[i - 1][j] + 1,matrix[i][j - 1] + 1]
            minNum = min(lis)
            idx = lis.index(minNum)
            matrix[i][j] = minNum
            if idx == 0:
                id_matrix[i][j] = (i - 1, j - 1)
            elif idx == 1:
                id_matrix[i][j] = (i - 1, j)
            else:
                id_matrix[i][j] = (i, j - 1)
    return matrix,id_matrix

