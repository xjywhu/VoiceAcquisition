# Generated by Django 3.0.3 on 2020-07-02 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200630_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='context',
            name='finished_time',
            field=models.IntegerField(default=0, verbose_name='完成次数'),
        ),
        migrations.AddField(
            model_name='context',
            name='token',
            field=models.IntegerField(default=1, max_length=200, verbose_name='分词'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='context',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='TaskFinish',
            fields=[
                ('uid', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('quality', models.IntegerField(default=0, verbose_name='匹配度')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Context', verbose_name='完成的句子')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User', verbose_name='任务完成者')),
            ],
        ),
        migrations.RemoveField(
            model_name='context',
            name='required_times',
        ),
        migrations.RemoveField(
            model_name='context',
            name='task',
        ),
        migrations.RemoveField(
            model_name='context',
            name='total_times',
        ),
    ]