# Generated by Django 3.0.3 on 2020-07-14 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20200702_1159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='context',
            old_name='token_baidu',
            new_name='token',
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file',
            field=models.FileField(max_length=200, upload_to='temp'),
        ),
    ]
