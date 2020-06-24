from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'contexts', Task_ContextViewSet)

users_service = UserViewSet.as_view({"get":"list","post":"update"})
tasks_service = TaskViewSet.as_view({"get":"list","post":"create"})
task_sentence_service = Task_ContextViewSet.as_view({"get":"list","post":"create"})

API_V1 = [
    url(r'^users_service/$', users_service, name='users_service'),
    url(r'^user_info/(?P<pk>\w+)$',UserView.as_view(),name='user_info'),  # 获取单个用户信息、修改某个用户信息、删除某个用户信息
    url(r'^user_info/$',UserView.as_view(),name='user_info'),  # 获取所有用户信息、增加用户信息
    url(r'^task_info/(?P<tid>\d+)$',TaskView.as_view(),name='task_info'), # 获取单个任务信息、修改某个任务信息、删除某个任务信息
    url(r'^task_info/$',TaskView.as_view(),name='task_info'),  # 获取所有任务信息、增加任务信息
    url(r'^task_context_info/$',Task_ContextView.as_view(),name='task_context_info'), # 获取所有句子、增加句子
    url(r'^task_context_info/(?P<tid>\d+)$',Task_ContextView.as_view(),name='task_context_info'), # 获取某一任务对应的所有句子
    url(r'^task_context_info/(?P<tid>\d+)/(?P<context>\w+)$',Task_ContextView.as_view(),name='task_context_info'),# 修改某一句子、删除某一句子
    url(r'^images/(?P<wx_number>\w+)', ImageView.as_view(), name='images'), # 获得图片
]

API_V1 += router.urls
API_VERSIONS = [url(r'^v1/', include(API_V1))]

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(API_VERSIONS)),
]
