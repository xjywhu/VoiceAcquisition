import os
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'contexts', Task_ContextViewSet)
router.register(r'upload', FileViewSet)

users_service = UserViewSet.as_view({"get":"list","post":"update"})
tasks_service = TaskViewSet.as_view({"get":"list","post":"create"})
task_sentence_service = Task_ContextViewSet.as_view({"get":"list","post":"create"})

API_V1 = [
    url(r'^users_service/$', users_service, name='users_service'),
    url(r'^user_info/(?P<pk>.*)$',UserView.as_view(),name='user_info'),  # 获取单个用户信息、修改某个用户信息、删除某个用户信息
    #path(r'^user_info/<str:pk>/',UserView.as_view(),name='user_info'),  # 获取单个用户信息、修改某个用户信息、删除某个用户信息
    url(r'^user_info/$',UserView.as_view(),name='user_info'),  # 获取所有用户信息、增加用户信息
    url(r'^task_info/(?P<tid>\d+)$',TaskView.as_view(),name='task_info'), # 获取单个任务信息、修改某个任务信息、删除某个任务信息
    url(r'^task_info/$',TaskView.as_view(),name='task_info'),  # 获取所有任务信息、增加任务信息
    url(r'^context_info/$',ContextView.as_view(),name='context_info'), # 获取所有句子、增加句子
    url(r'^context_info/(?P<pk>\d+)$',ContextView.as_view(),name='context_info'), # 根据句子id获取句子
    url(r'^internal/context/$',InternalContextView.as_view(),name='internal_context'),# 增加句子,获得所有句子
    url(r'^internal/context/(?P<cid>\d+)/',InternalContextView.as_view(),name='internal_context'),# 修改、删除句子
    url(r'^task_finish/$',TaskFinishView.as_view(),name='task_finish'), # 获取所有的任务完成情况，客户端应该用不上
    url(r'^task_finish/(?P<cid>\d+)/(?P<wx_number>.*)',TaskFinishView.as_view(),name='task_finish'),#根据用户id和cid获取完成情况
    url(r'^task_finish/(?P<wx_number>.*)$',TaskFinishView.as_view(),name='task_finish'), # 获取某人完成任务的情况

    #url(r'^context_info/(?P<cid>\d+)/(?P<context>.*)$',ContextView.as_view(),name='context_info'),# 修改某一句子、删除某一句子
    url(r'^images/(?P<wx_number>.*)$', ImageView.as_view(), name='images'), # 获得图片
    url(r'^openid/(?P<code>.*)$',OpenIdView.as_view(),name='openid'),
    url(r'^voices_info/(?P<cid>\d+)/(?P<wx_number>.*)$',VoiceView.as_view(),name='voices_info'),
]

API_V1 += router.urls
API_VERSIONS = [url(r'^v1/', include(API_V1))]

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(API_VERSIONS)),
]
