# Generated by Django 3.0.3 on 2020-06-25 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200625_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='releaser_wx_number',
            new_name='releaser',
        ),
    ]
