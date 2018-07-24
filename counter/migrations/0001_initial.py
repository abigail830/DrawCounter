# Generated by Django 2.0.7 on 2018-07-24 02:11

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_count', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Avaiable Counts')),
                ('last_update_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Last Update Date')),
                ('remark', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered start with'+' & Up to 15 digits allowed.", regex='^\\+?1?\\d{8,15}$')])),
                ('join_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='The date joined as member')),
                ('remark', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='counter',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counts', related_query_name='count', to='counter.Member'),
        ),
    ]
