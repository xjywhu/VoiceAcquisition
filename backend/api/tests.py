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

	
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir = BASE_DIR+"\\voices\\tmp.mp3"
any2pcm(dir)