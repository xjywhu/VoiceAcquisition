import requests
import os,sys
# from backend import settings
# sys.path.append(settings.BASE_DIR)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.getcwd().split(BASE_DIR)[0] + BASE_DIR)
from token_baidu import Token_Global
from aip import AipNlp

def get_tokens(text):
    client = AipNlp(Token_Global.get_app_id(), Token_Global.get_api_key(), Token_Global.get_secret_key())
    res = client.lexer(text)
    items = res['items']
    result = [item['item'] for item in items]
    print(result)
    return result


# get_tokens('今天天气怎么样')