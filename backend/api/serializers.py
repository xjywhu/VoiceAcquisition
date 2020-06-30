from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('wx_number','nickName','score','native_place', 'image')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['releaser','title','money','threshold_value','description']
        depth = 1

class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Context
        fields = ['task','sentence','required_times','finish_times']
        depth = 2

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = '__all__'

