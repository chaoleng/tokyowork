# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-12-30 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20181230_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.IntegerField(default=0)),
                ('card_update', models.DateTimeField(verbose_name='date published')),
                ('card_time', models.DateTimeField(verbose_name='date published')),
                ('create_id', models.CharField(max_length=50)),
                ('create_name', models.CharField(max_length=50)),
                ('card_state', models.CharField(max_length=30)),
                ('card_title', models.CharField(max_length=30)),
                ('card_content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('user_name', models.CharField(max_length=30)),
                ('user_register_time', models.DateTimeField(verbose_name='date published')),
                ('user_place', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]