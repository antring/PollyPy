# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PollyUpload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesub',
            name='path',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='tvsub',
            name='path',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
