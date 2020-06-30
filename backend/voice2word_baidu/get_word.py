# coding=gbk
# ���ߣ����Ρ�ʯ����
import Global, format_transfer, delete_voices, download_voice
from aip import AipSpeech

# ���ã����������Ƶʶ��Ϊ����
class Converter:
    def __init__(self):
        self._client = AipSpeech(Global.get_app_id(), Global.get_api_key(), Global.get_secret_key())

    # ʶ�𱾵��ļ�
    # file string:�ļ���
    # client client����
    # dev_pid int ����id
    # format string ��Ƶ��ʽ
    def __recognize(self, file, dev_pid, format):
        # ��ȡ�ļ�
        def get_file_content(file_path):
            with open(file_path, 'rb') as fp:
                return fp.read()

        res = self._client.asr(get_file_content(file), format, 16000, {
            'dev_pid': dev_pid,
        })
        # 3301 ���ʹ���
        # 3305 �û�������������
        # 3307 Ŀǰ��ȷ��16000�Ĳ�������Ƶʱ������30s
        # 3308 ��Ƶ������������60s
        # 3311 rate�������Ŀǰrate����֧��16000��8000����д4000�����д˴���
        # 3312 Ŀǰ��ʽ����֧��pcm��wav��amr������дmp3�����д˴���
        if res["err_no"] == 0:
            return res["result"]
        else:
            return "error %d" % res["err_no"]


    # ���ã�ֱ��ͨ��url������Ƶ������ת��Ϊ����
    # mode : ֻ��'LOCAL'��'URL'���֣���Ϊ'LOCAL'ʱ����ַ�Ǳ����ļ�����Ϊ'URL'ʱ����ַ��Զ����Ƶ�ļ�������ַ
    def get_words(self, url, mode = 'LOCAL'):
        if mode == 'LOCAL':
            pcm_filename = format_transfer.any2pcm(url)
            res = self.__recognize(pcm_filename, 1537, "pcm")
            return res
        elif mode == 'URL':
            # �������amr�ļ�
            delete_voices.remove(".amr")
            # �����ļ�
            download_voice.download_by_path(url, "voice.amr")
            # �ļ���ʽת��
            pcm = format_transfer.amr2pcm("voice.amr")
            # ��ý��
            res = self.__recognize(pcm, 1537, "pcm")
            return res


#######################################################����������� start
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
#######################################################����������� end

####################################################### �����ռ�APP�������� start
converter = Converter()
res = converter.get_words('http://tmp/wxfbbdf46e1f2546ef.o6zAJs1WD6ZBhsSA0-IkczMPWtXE.G64x9jvhFpt571279d946a0ce10647a15976e9bce513.durationTime=3307.mp3')
print(res)
####################################################### �����ռ�APP�������� end