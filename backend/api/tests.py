# Create your tests here.
import os,sys
import Global
def any2pcm(filename):
    ext = filename.split(".")[-1]
    pcm_filename = "%s.pcm" % (filename.split(".%s" % ext)[0])
    print(pcm_filename)
    # 就是此前我们在cmd窗口中输入命令,这里面就是在让Python帮我们在cmd中执行命令
    os.system("%s/ffmpeg -y  -i %s  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s" % (
    Global.get_ffmpeg_path(), filename, pcm_filename))
    return pcm_filename

<<<<<<< HEAD
	
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir = BASE_DIR+"\\voices\\tmp.mp3"
any2pcm(dir)
=======
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
a = [3,4,1,7,2]
idx = [1,2]
print(a[idx])
>>>>>>> 8ce0265cede4d7eb452d281a2c7253a812c75fce
