# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieSub',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('year', models.IntegerField()),
                ('lang', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='TvSub',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('season', models.IntegerField()),
                ('episode', models.IntegerField()),
                ('lang', models.CharField(max_length=2)),
            ],
        ),
    ]
