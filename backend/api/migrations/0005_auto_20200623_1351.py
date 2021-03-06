# Generated by Django 3.0.3 on 2020-06-23 05:51

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200623_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to=api.models.wrapper),
        ),
        migrations.AlterField(
            model_name='user',
            name='native_place',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='籍贯'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickName',
            field=models.CharField(max_length=50, null=True, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0, null=True, verbose_name='积分'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.BooleanField(null=True, verbose_name='性别'),
        ),
    ]
