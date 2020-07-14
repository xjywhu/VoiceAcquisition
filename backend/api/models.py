from django.db import models
from backend import settings


def wrapper(instance, filename):
    ext = filename.split('.')[-1]
    instance.name = str(instance.wx_number) + "." + ext
    # return the whole path to the file
    # path = settings.MEDIA_ROOT + "\\{}".format(instance.name)
    path = "./{}".format(instance.name)
    print(path)
    return path


def path_and_rename():
    return wrapper


class User(models.Model):
    wx_number = models.CharField(max_length=50, verbose_name='微信号', primary_key=True)
    nickName = models.CharField(max_length=50, verbose_name='昵称',null=True,default='请输入昵称')
    age = models.IntegerField(verbose_name='年龄',null=True)
    sex = models.CharField(max_length=3,verbose_name='性别',null=True)
    score = models.IntegerField(verbose_name='积分',default=0,null=True)
    native_place = models.CharField(max_length=50,verbose_name='籍贯',default='',null=True)
    image = models.CharField(max_length=200,null=True)
    task_times = models.IntegerField(verbose_name='做任务次数',default=0)
    success_times = models.IntegerField(verbose_name='成功次数',default=0)

    REQUIRED_FIELDS = ['wx_number']
    class Meta:
        unique_together = ('wx_number',)


class Task(models.Model):
    '''
    发布者，发布时间，任务名称，金额，阈值，任务描述
    '''
    tid = models.IntegerField(verbose_name='tid',primary_key=True,auto_created=True)
    releaser = models.ForeignKey(to='User', verbose_name='发布者', on_delete=models.CASCADE)
    release_time = models.DateField(auto_now=True)
    title = models.CharField(max_length=50,verbose_name='任务名称')
    money = models.IntegerField(verbose_name='金额')
    threshold_value = models.FloatField(verbose_name='阈值')
    description = models.CharField(max_length=1000,verbose_name='任务描述')
    # 还剩下多少个语音就完成了，一开始设置为0，最后计算出所有的语句的需求量之和替换当前字段值
    rest = models.BigIntegerField(verbose_name='剩余语句数',default=0)
    REQUIRED_FIELDS = ['tid','releaser','title','money','description']

    class Meta:
        unique_together = ('tid',)

class Context(models.Model):
    cid = models.IntegerField(verbose_name='id',primary_key=True,auto_created=True)
    sentence = models.CharField(max_length=100, verbose_name='内容')
    token = models.CharField(verbose_name='分词',max_length=200)
    finished_times = models.IntegerField(verbose_name='完成次数',default=0)
    base_score = models.IntegerField(verbose_name='最高积分',default=100)
    threshold_value = models.IntegerField(default=90,verbose_name='阈值')

    REQUIRED_FIELDS = ['sentence','token','finished_times']

class TaskFinish(models.Model):
    uid = models.IntegerField(verbose_name='id',primary_key=True,auto_created=True)
    user = models.ForeignKey(to='User', verbose_name='任务完成者', on_delete=models.CASCADE)
    context = models.ForeignKey(to='Context',verbose_name='完成的句子',on_delete=models.CASCADE)
    quality = models.IntegerField(verbose_name='匹配度',default=0)

    REQUIRED_FIELDS = ['user', 'context', 'quality']
    class Meta:
        unique_together = ('user','context')

class FileModel(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='temp',max_length=200)


class Token(models.Model):
    token = models.CharField(primary_key=True,verbose_name='token',max_length=30)
    finish_times = models.IntegerField(verbose_name='完成次数', default=0)





