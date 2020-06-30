# coding=gbk
# 作者：邹鑫、石亮禾
import Global, format_transfer, delete_voices, download_voice
from aip import AipSpeech

# 作用：将传入的音频识别为文字
class Converter:
    def __init__(self):
        self._client = AipSpeech(Global.get_app_id(), Global.get_api_key(), Global.get_secret_key())

    # 识别本地文件
    # file string:文件名
    # client client对象
    # dev_pid int 语言id
    # format string 音频格式
    def __recognize(self, file, dev_pid, format):
        # 读取文件
        def get_file_content(file_path):
            with open(file_path, 'rb') as fp:
                return fp.read()

        res = self._client.asr(get_file_content(file), format, 16000, {
            'dev_pid': dev_pid,
        })
        # 3301 音质过差
        # 3305 用户日请求量超限
        # 3307 目前请确保16000的采样率音频时长低于30s
        # 3308 音频过长，高于了60s
        # 3311 rate输入错误，目前rate参数支持16000、8000，填写4000即会有此错误
        # 3312 目前格式仅仅支持pcm，wav或amr，如填写mp3即会有此错误
        if res["err_no"] == 0:
            return res["result"]
        else:
            return "error %d" % res["err_no"]


    # 作用：直接通过url下载音频并将其转化为文字
    # mode : 只有'LOCAL'和'URL'两种，当为'LOCAL'时，地址是本地文件，当为'URL'时，地址是远程音频文件下载网址
    def get_words(self, url, mode = 'LOCAL'):
        if mode == 'LOCAL':
            pcm_filename = format_transfer.any2pcm(url)
            res = self.__recognize(pcm_filename, 1537, "pcm")
            return res
        elif mode == 'URL':
            # 清除所有amr文件
            delete_voices.remove(".amr")
            # 下载文件
            download_voice.download_by_path(url, "voice.amr")
            # 文件格式转换
            pcm = format_transfer.amr2pcm("voice.amr")
            # 获得结果
            res = self.__recognize(pcm, 1537, "pcm")
            return res


#######################################################花旗测试用例 start
# delete_voices.remove()
# converter = Converter()
# pcm = format_transfer.wav2pcm("v3.wav")
# # pcm = format_transfer.wav2pcm("voice.amr")
# res = converter.recognize(pcm, 1536, "pcm")
# # res = converter.recognize("v2.pcm", 1536, "pcm")
# print(res)
# c = Converter()
# res = c.recognize("voice.pcm",)
# res = c.get_words("https://api.weixin.qq.com/cgi-bin/media/get?access_token=23_r71wkIzje7RNunfdC_3UVpWkGzk4Ak68a0wAD4bYFkqhwephJMlMj2kkLStTpVu7-Zi42z6kh0T2eAtYI48t_wjSjOO8MM0deAHQxmEd2M5Csfze2PDBXJ-x2qALFIcAHAGAD&media_id=dABM-WBO-UJTrrg20-d4UF3HBuazXzP0Tvm3ZFHdYs4b9vzwIj21klAoGCUCFhbi")
# print(res)
#######################################################花旗测试用例 end

####################################################### 语音收集APP测试用例 start
converter = Converter()
res = converter.get_words('http://tmp/wxfbbdf46e1f2546ef.o6zAJs1WD6ZBhsSA0-IkczMPWtXE.G64x9jvhFpt571279d946a0ce10647a15976e9bce513.durationTime=3307.mp3')
print(res)
####################################################### 语音收集APP测试用例 end