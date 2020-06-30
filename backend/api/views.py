import os
import json
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.http import HttpResponse
import requests

app_id = "wxfbbdf46e1f2546ef"
app_secret = "f71231c7013b49a9bdb1f60136dcbba5"

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class Task_ContextViewSet(ModelViewSet):
    queryset = Task_Context.objects.all()
    serializer_class = Task_ContextSerializer


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
            return Response('删除失败')
        else:
            User.objects.filter(wx_number=pk).delete()
            return Response('删除成功')

    def put(self,request,*args,**kwargs):
        '''更新'''
        pk = kwargs.get('pk')
        if not pk:
            # id错误
            print('获取pk失败')
            return Response('获取pk失败')
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

    def post(self,request,*args,**kwargs):
        ''' 上传一个任务列表 '''
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def put(self, request, *args, **kwargs):
        '''更新'''
        tid = kwargs.get('tid')
        if not tid:
            # id错误
            return Response('获取tid失败')
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
            return Response('删除失败')
        else:
            Task.objects.filter(tid=tid).delete()
            return Response('删除成功')


class Task_ContextView(APIView):
    def get(self,request,*args,**kwargs):
        '''查找'''
        tid = kwargs.get('tid')
        if not tid:
            # 获取全部信息
            queryset = Task_Context.objects.all()
            serializer = Task_ContextSerializer(instance=queryset, many=True)
            return Response(serializer.data)
        else:
            # 获取某一tid对应的所有
            queryset = Task_Context.objects.filter(tid=tid)
            serializer = Task_ContextSerializer(instance=queryset, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        '''上传'''
        serializer = Task_ContextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def put(self, request, *args, **kwargs):
        tid = kwargs.get('tid')
        context = kwargs.get('context')
        if tid and context:
            task_context = Task_Context.objects.filter(tid=tid,context=context).first()
            serializer = Task_ContextSerializer(instance=task_context, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response('获取tid或context失败')

    def delete(self, request, *args, **kwargs):
        tid = kwargs.get('tid')
        context = kwargs.get('context')
        if tid and context:
            Task_Context.objects.filter(tid=tid,context=context).delete()
            return Response('删除成功')
        else:
            return Response('删除失败')


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
            return Response('请传入code参数',status=400)
            #return Response('请传入code参数')

class FileViewSet(ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer
