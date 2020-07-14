import os,math,glob
import json
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.http import HttpResponse
import requests
from django.db.models import Q
import random
from voice2word_baidu.get_word import Converter
from tools.file_mover import FileHandler
from algorithm.edit_distance import get_similarity
from token_baidu.get_token import get_tokens
import xlrd

app_id = "wxfbbdf46e1f2546ef"
app_secret = "f71231c7013b49a9bdb1f60136dcbba5"

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class Task_ContextViewSet(ModelViewSet):
    queryset = Context.objects.all()
    serializer_class = ContextSerializer


class UserView(APIView):
    def post(self,request,*args,**kwargs):
        # 增加用户
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        if not pk:
            # 删除失败
            return Response({'StatusCode':'fail','failReason':'未在url中加入对应的wx_number'})
        else:
            User.objects.filter(wx_number=pk).delete()
            return Response({'StatusCode':'success'})

    def put(self,request,*args,**kwargs):
        '''更新'''
        pk = kwargs.get('pk')
        if not pk:
            # id错误
            print('获取pk失败')
            return Response({'StatusCode':'fail','failReason':'未在url中加入对应的wx_number'})
        else:
            # user = User.objects.filter(wx_number=pk).first()
            print('pk=',pk)
            res = User.objects.get_or_create(wx_number=pk)
            user = res[0]
            isCreated = res[1]
            if isCreated:
                # 创建
                print('是创建的')
            print(request.data)
            serializer = UserSerializer(instance=user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        if not pk:
            # 获取所有用户信息
            queryset = User.objects.all()
            serializer = UserSerializer(instance=queryset, many=True)
            return Response(serializer.data)
        else:
            # 获取单个用户信息
            print(pk)
            user = User.objects.filter(wx_number=pk).first()
            serializer = UserSerializer(instance=user, many=False)
            return Response(serializer.data)


class TaskView(APIView):
    def get(self,request,*args,**kwargs):
        ''' 获取全部列表 '''
        tid = kwargs.get('tid')
        if not tid:
            # 获取所有
            queryset = Task.objects.all()
            serializer = TaskSerializer(instance=queryset, many=True)
            return Response(serializer.data)
        else:
            # 获取单个
            print(tid)
            task = Task.objects.filter(tid=tid).first()
            serializer = TaskSerializer(instance=task, many=False)
            return Response(serializer.data)

    def dealPost(self,request,*args,**kwargs):
        try:
            data = request.data
            user = User.objects.filter(wx_number=data['releaser']).first()
            title = data['title']
            money = data['money']
            threshold_value = data['threshold_value']
            description = data['description']
            obj = Task(releaser=user, title=title, money=money, threshold_value=threshold_value, description=description)
            if user is not None:
                print('before new task save')
                obj.save()
                print('after new task save')
                # serializer.save()
                return Response({'StatusCode':'success'})
            else:
                return Response({'StatusCode': 'fail','failReason':'releaser的id不存在'})
                #return Response('wx_number不存在')
        except KeyError as e:
            return Response({'StatusCode': 'fail','failReason':'缺少字段，请补充完整'})
            # return Response('缺少字段，请补充完整')

    def post(self,request,*args,**kwargs):
        ''' 上传一个任务列表 '''
        print('before create task serializer')
        serializer = TaskSerializer(data=request.data)
        print('after create task serializer')
        if serializer.is_valid() or (len(serializer.errors) == 1 and serializer.errors.get('tid')):
            print(serializer.errors)
            return self.dealPost(request,args,kwargs)
        else:
            print(serializer.errors)
            return Response(serializer.errors)



    def put(self, request, *args, **kwargs):
        '''更新'''
        tid = kwargs.get('tid')
        if not tid:
            # id错误
            return Response({'StatusCode':'success','failReason':'未在url中填入tid'})
        else:
            task = Task.objects.filter(tid=tid).first()
            serializer = TaskSerializer(instance=task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        tid = kwargs.get('tid')
        if not tid:
            # 删除失败
            return Response({'StatusCode':'fail','failReason':'未在url中填入tid'})
        else:
            Task.objects.filter(tid=tid).delete()
            return Response({'StatusCode':'success'})

class InternalContextView(APIView):##################################################################
    def get(self, request, *args, **kwargs): # 获取所有context
        queryset = Context.objects.all()
        serializer = ContextSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def dealPost(self, request, *args, **kwargs):
        try:
            data = request.data
            token = data['token_baidu']
            sentence = data['sentence']
            finished_times = data['finished_times']
            obj = Context(token=token,sentence=sentence,finished_times=finished_times)
            obj.save()
            return Response({'StatusCode': 'success'})
        except KeyError as e:
            return Response({'StatusCode': 'fail', 'failReason': '缺少字段，请补充完整'})

    def post(self, request, *args, **kwargs):  ######################### 应该不需要了
        '''上传'''
        serializer = ContextSerializer(data=request.data)
        if serializer.is_valid() or (len(serializer.errors) == 1 and serializer.errors.get('cid')):
            print(serializer.errors)
            return self.dealPost(request, args, kwargs)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

    def put(self, request, *args, **kwargs): ############################### 应该不需要了
        cid = kwargs.get('cid')
        if cid:
            context = Context.objects.filter(cid=cid).first()
            serializer = ContextSerializer(instance=context, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'StatusCode':'fail','failReason':'url中获取cid失败'})

    def delete(self, request, *args, **kwargs): #####################应该不需要了
        cid = kwargs.get('cid')
        if cid:
            Context.objects.filter(cid=cid).delete()
            return Response({'StatusCode':'success'})
        else:
            return Response({'StatusCode':'fail','failReason':'url中获取cid失败'})


class ContextView(APIView):
    def get_recommended_contexts(self): ################################待修改
        MAX = 20
        MAX_WILLFINISH = 5
        if Context.objects.count() <= MAX:
            # 获取全部信息
            return Context.objects.all()
        else: # 获取MAX个信息
            # queryset = Context.objects.filter(task_id=[1,2])
            taskQuerySet = Task.objects.order_by('rest').values('tid')[:MAX_WILLFINISH]
            task_ids = [task['tid'] for task in taskQuerySet]
            nearlyFinishedContextsQuerySet = Context.objects.none()
            for tid in task_ids:
                cQuerySet = Context.objects.filter(~Q(required_times=0), task_id=tid)[:1]
                nearlyFinishedContextsQuerySet = nearlyFinishedContextsQuerySet | cQuerySet
            REST_NUM = MAX - MAX_WILLFINISH

            print('下面是选出的快完成的context的id:')
            for c in nearlyFinishedContextsQuerySet:
                print(c.cid)
            ContextQuerySet = Context.objects.all()
            for obj in nearlyFinishedContextsQuerySet:
                ContextQuerySet = ContextQuerySet.filter(~Q(cid=obj.cid))
            size = len(ContextQuerySet)
            random_indexs = random.sample(range(0, size), REST_NUM)
            print('下面是随机index')
            print(random_indexs)
            print('下面是除去快完成的context后剩下的context的id')
            for c in ContextQuerySet:
                print(c.cid)
            cids = [ContextQuerySet[idx].cid for idx in random_indexs]
            print('下面是随机选取的id:')
            print(cids)
            randomContextQuerySet = Context.objects.filter(pk__in=cids)
            print('下面是选出来的随机QuerySet中的Context的id:')
            for c in randomContextQuerySet:
                print(c.cid)
            queryset = Context.objects.all()[:MAX_WILLFINISH]
            return queryset

    def get(self, request, *args, **kwargs):
        ''' 新的post函数，根据某些算法，找出50条句子发送给前端 '''
        pk = kwargs.get('pk')
        if not pk:
            contexts = self.get_recommended_contexts()
            serializer = ContextSerializer(instance=contexts, many=True)
            return Response(serializer.data)
        else:
            # 获取某一cid对应的句子
            context = Context.objects.filter(cid=pk).first()
            serializer = ContextSerializer(instance=context, many=False)
            return Response(serializer.data)


class TaskFinishView(APIView):
    # 根据cid和 wx_number获取对应的任务
    def get(self, request, *args, **kwargs):
        wx_number = kwargs.get('wx_number')
        cid = kwargs.get('cid')
        if not cid and not wx_number: # 获取全部
            queryset = TaskFinish.objects.all()
            serializer = TaskFinishSerializer(instance=queryset,many=True)
            return Response(serializer.data)
        elif not cid and wx_number: # 获取某个用户的完成情况
            queryset = TaskFinish.objects.filter(user_id=wx_number)
            serializer = TaskFinishSerializer(instance=queryset, many=True)
            return Response(serializer.data)
        elif cid and wx_number: # 获取某用户对某句子的完成情况
            queryset = TaskFinish.objects.filter(user_id=wx_number,context_id=cid).first()
            serializer = TaskFinishSerializer(instance=queryset, many=False)
            return Response(serializer.data)



class ImageView(APIView):

    def get(self, request, *args, **kwargs):
        wx_number = kwargs.get('wx_number')
        print('1', wx_number)
        try:
            if not wx_number:
                return HttpResponse('请输入微信号')
            user = User.objects.filter(wx_number=wx_number).first()
            if not user:
                return HttpResponse('微信号不存在')
            f = user.image
            image_data = f.read()
            ext = f.name.split('.')[-1] # 后缀名
            return HttpResponse(image_data, content_type="image/%s" % ext)
            # image_path = os.path.join(settings.MEDIA_ROOT, img_path)
            # print('2',image_path)
            # with open(image_path, 'rb') as f:
            #     image_data = f.read()
            # return HttpResponse(image_data, content_type="image/png")
        except Exception as e:
            print(e)
            return HttpResponse(str(e))

    def put(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class OpenIdView(APIView):

    def get(self, request, *args, **kwargs):
        code = kwargs.get('code')
        if code:
            print('code:',code)
            url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&s' \
                  'ecret=%s&js_code=%s&grant_type=authorization_code' % (app_id,app_secret,code)
            res = requests.get(url=url)
            print(res.text)
            return Response(res.json())
        else:
            return Response({'StatusCode':'fail','failReason':'未在url中获得code参数'})
            #return Response('请传入code参数',status=400)
            #return Response('请传入code参数')

class FileViewSet(ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer


VOICE_BASE_URL = '../voices_store/'

class VoiceView(APIView):
    def get(self, request, *args, **kwargs):
        pass

    def get_rate(self,origin_str, convert_str):
        '''
        :param origin_str: context表中的句子
        :param convert_str: 语音转化而成的句子
        :return: 两个句子的匹配度  0-1之间
        '''
        return get_similarity(origin_str,convert_str)

    def post(self, request, *args, **kwargs):
        cid = kwargs.get('cid')
        wx_number = kwargs.get('wx_number')
        default_filename = 'tmp'
        default_ext = '.mp3'
        api_ext = '.pcm'
        dir = os.path.join(settings.BASE_DIR, 'voices/')

        dst_dir = os.path.join(settings.BASE_DIR, 'voice_store/')
        if not cid or not wx_number: # url没有给出cid或wx_number
            print('url中获取cid或wx_number失败')
            return Response({'StatusCode':'fail','failReason':'url中获取cid或wx_number失败'})

        print('cid : ',cid)
        print('wx_number : ',wx_number)
        # 给出了cid和wx_number，接着往下做
        # 失败的可能：1、没达到阈值   2、这个任务正好刚才被人做完  3、
        file = request.FILES.get("voice_file", None)
        if not file:
            print('接收文件失败.')
            return Response({'StatusCode': 'fail', 'failReason': '接收文件失败'})

        # file接收到了,就存储文件为  default_filename + default_ext
        destination = open(os.path.join(dir, default_filename + default_ext),
                           'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        # 调用api获取结果
        converter = Converter()
        words_from_voice = converter.get_words(dir+default_filename+default_ext)[0]
        print('words_from_voice: ',words_from_voice)
        # 根据cid获取文本
        context = Context.objects.filter(cid=cid).first()
        words_from_context = context.sentence
        print('words_from_context: ',words_from_context)
        min_rate = context.threshold_value / 100  # 设定的阈值
        print('min_rate: ',min_rate)
        rate = self.get_rate(words_from_context,words_from_voice)  # 匹配率
        # print('required_times: ',required_times)
        # if required_times <= 0:
        #     # 删除本地文件 --- 暂时不用删了
        #     return Response({'StatusCode':'fail','failReason':'此任务已被其他用户完成'})

        # 修改wx_number的用户的 task_times字段，让其加1
        #######
        user = User.objects.filter(wx_number=wx_number).first()
        user.task_times = user.task_times+1
        user.save()
        if rate < min_rate:
            # 删除本地文件 --- 暂时不用删了
            return Response({'StatusCode':'fail','failReason':'匹配度未达到阈值'})
        # 匹配度达到
        # 修改wx_number的用户的 success_times字段，让其加1
        #######
        user = User.objects.filter(wx_number=wx_number).first()
        user.success_times = user.success_times + 1
        # 修改context的finished_times
        ######
        context.finished_times = context.finished_times+1
        # 增加任务完成数据
        ######
        task_finsh = TaskFinish(user_id=wx_number,context_id=cid,quality=math.floor(100*rate))
        # 增加用户的积分
        ######
        user.score = user.score+math.floor(context.base_score*rate)
        # 保存
        ######
        user.save()
        context.save()
        task_finsh.save()
        # 将MP3文件重命名并移动到指定文件
        move_to_filename = user.wx_number+'_'
        if user.native_place:
            move_to_filename += user.native_place+'_'
        else:
            move_to_filename += "NONE"
        if user.age:
            move_to_filename += user.age
        else:
            move_to_filename += "NONE"


        move_to_dir = dst_dir+"%s/" % cid # 每个句子一个文件夹
        if not os.path.exists(move_to_dir):
            os.mkdir(move_to_dir)
        files = os.listdir(move_to_dir)
        #file_number = glob.glob(pathname=move_to_dir+'*.mp3')  # 获取当前文件夹下个数
        file_number = len(files)
        dst_filename = move_to_filename+("_%d"%file_number) + default_ext
        move_from_dir = dir
        src_filename = default_filename+default_ext


        handler = FileHandler(move_from_dir,move_to_dir)
        handler.moveFile(src_filename,dst_filename)
        print('成功移动文件')
        return Response({'StatusCode': 'success'})

class ReleaseContextViewSet(ModelViewSet):

    # def post(self, request, *args, **kwargs):
    #     pass
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer

    def write_file_to_db(self,filename):
        # filename = settings.BASE_DIR + '/temp/task.xlsx'
        # 打开工作表
        workbook = xlrd.open_workbook(filename=filename)
        # 用索引取第一个工作薄
        booksheet = workbook.sheet_by_index(0)
        # 返回的结果集
        for i in range(booksheet.nrows):
            list = booksheet.row_values(i)
            sentence = list[0]
            base_score = list[1]
            threshold_value = list[2]
            tokens = get_tokens(sentence)
            context_token = ''
            for tk in tokens:
                context_token+=tk+'|'
                obj = Token.objects.filter(token='aaa')
                if len(obj) == 0:
                    # 数据库中没有此token，加入
                    new_token = Token(token=tk)
                    new_token.save()
            context_token=context_token[0:-1]
            context = Context(sentence=sentence,base_score=base_score,threshold_value=threshold_value,token=context_token)
            context.save()

    def create(self, request, *args, **kwargs):
        TEMP_DIR = os.path.join(settings.BASE_DIR, 'temp/')
        default_filename = 'task'
        default_ext = '.xlsx'
        file = request.FILES.get("file", None)
        if not file:
            print('接收文件失败.')
            return Response({'StatusCode': 'fail', 'failReason': '接收文件失败'})

        # file接收到了,就存储文件为  default_filename + default_ext
        destination = open(os.path.join(TEMP_DIR, default_filename + default_ext),
                           'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        local_path = os.path.join(TEMP_DIR, default_filename + default_ext)
        self.write_file_to_db(local_path)
        print('文件下载完成')
        return Response({'StatusCode': 'success'})




