
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

def get_similarity(str1,str2):
    distance = edit_distance(str1,str2)
    maxlen = max(len(str1),len(str2))
    ret = 1 - distance/maxlen
    return ret