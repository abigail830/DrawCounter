# Generated by Django 2.0.7 on 2018-07-24 02:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_auto_20180724_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='last_update_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Last Update Date'),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='The date joined as member'),
        ),
    ]
