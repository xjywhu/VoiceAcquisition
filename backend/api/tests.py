# Create your tests here.
import os,sys

from algorithm.edit_distance import edit_distance,get_similarity
import xlrd
from backend.settings import *
from token_baidu.get_token import get_tokens,punctuation_replace,get_no_sign_tokens
import jieba

# text = '你好,我叫张三。'
# get_tokens(text)
# get_no_sign_tokens(text)

#################  jieba
#res = jieba.lcut('你好，我叫张三')
#print(res)


# sign,null = punctuation_replace(text)
# print(sign.split('|'))
# print(sign)
# print(null)

#################
# lis = ['a','b','c']
# lis.remove('d')
# print(lis)
#################
# lis = [1,2,3]
# print(lis+[4])

################
# a = [3,4,1,7,2]
# idx = [1,2]
# print(a[idx])


#####################
from algorithm.edit_distance import test_edit_distance,extended_edit_distance
# str1 = 'batyu'#'zabcd'#'batyu' # 写在左边的
# str2 = 'beauty'#'abcde'#'beauty' # 写在上边的
# rate,a,b ,matrix, id_matrix= extended_edit_distance(str1,str2)
# for row in matrix:
#     print(row)
#
# print('\n')
# for row in id_matrix:
#     print(row)
#
# row = len(id_matrix)
# col = len(id_matrix[0])
# lis = []
# i = row - 1
# j = col - 1
# while i!=0 and j!=0:
#     lis += [(i, j)]
#     cell = id_matrix[i][j]
#     i = cell[0]
#     j = cell[1]
#
#
# lis += [(i,j)]
# lis.reverse()
#
# print(lis)
# print('a:', a)
# print('b:', b)
##################
# c1=(1,2)
# c2 =(2,3)
# print(c2-c1)


###################
from my_jwt.jwt_handler import create_token,verify_token
import time
token = create_token("oVCRb5GmyJlyChS90erPLg-Jlz6c", 1)
# print(token)
# token = token[:44]+'A'+token[45:]

# time.sleep(2)
# 等待2s后再次验证token，因超时将导致验证失败
flag, info = verify_token(token)
if flag:
    wx = info['wx_number']
    print(wx)
#print(info)