# Generated by Django 3.0.3 on 2020-07-14 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20200714_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='token')),
                ('finish_times', models.IntegerField(default=0, verbose_name='完成次数')),
            ],
        ),
    ]
