# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-22 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=256, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=256, unique=True)),
                ('body', models.TextField(max_length=600)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='public.Article')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
