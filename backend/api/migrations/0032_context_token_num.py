# Generated by Django 3.0.3 on 2020-07-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_context_base_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='context',
            name='token_num',
            field=models.IntegerField(default=1, verbose_name='token的个数'),
        ),
    ]
