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
from algorithm.edit_distance import test_edit_distance
str1 = 'aaaaa'
str2 = 'aaaab'
test_edit_distance(str1,str2)