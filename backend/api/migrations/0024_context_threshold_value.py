# Generated by Django 3.0.3 on 2020-07-02 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20200702_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='context',
            name='threshold_value',
            field=models.IntegerField(default=90, verbose_name='阈值'),
        ),
    ]
