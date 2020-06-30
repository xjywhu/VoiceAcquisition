from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('wx_number','nickName','score','native_place', 'image')

    # def update(self, instance, validated_data):
    #     instance.nickName = validated_data.get('nickName', instance.nickName)
    #     instance.native_place = validated_data.get('native_place', instance.native_place)
    #     # 还有头像




class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['releaser', 'title','money', 'threshold_value', 'description']
        depth = 1

class Task_ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_Context
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = '__all__'

