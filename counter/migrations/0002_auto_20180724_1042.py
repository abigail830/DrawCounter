# Generated by Django 2.0.7 on 2018-07-24 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
