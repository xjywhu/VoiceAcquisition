import requests
import os,sys
# from backend import settings
# sys.path.append(settings.BASE_DIR)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.getcwd().split(BASE_DIR)[0] + BASE_DIR)
from token_baidu import Token_Global
from aip import AipNlp
from string import punctuation as en_punctuation  # 引入英文标点
from zhon.hanzi import punctuation as cn_punctuation  # 引入中文标点
import re


def punctuation_replace(text):
    #en_ = " ".join([c for c in text if c not in en_punctuation])
    #cn_ = " ".join([c for c in en_ if c not in cn_punctuation])
    REPLACE_SIGN = '|'
    replace_en = re.sub(r'[{}]+'.format(en_punctuation), REPLACE_SIGN, text)
    replace_with_sign = re.sub(r'[{}]+'.format(cn_punctuation), REPLACE_SIGN, replace_en)
    replace_with_null = replace_with_sign.replace(REPLACE_SIGN,'')
    return replace_with_sign,replace_with_null

def get_tokens(text):
    client = AipNlp(Token_Global.get_app_id(), Token_Global.get_api_key(), Token_Global.get_secret_key())
    res = client.lexer(text)
    #print(res)
    items = res['items']
    result = [item['item'] for item in items]
    print(result)
    return result

def get_no_sign_tokens(text): # 获得分词列表，且删除了标点符号
    client = AipNlp(Token_Global.get_app_id(), Token_Global.get_api_key(), Token_Global.get_secret_key())
    res = client.lexer(text)
    #print(res)
    items = res['items']
    result = [item['item'] for item in items if item['pos'] != 'w']
    print(result)
    return result


# get_tokens('今天天气怎么样')