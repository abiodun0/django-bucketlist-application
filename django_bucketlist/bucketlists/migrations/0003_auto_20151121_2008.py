# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlists', '0002_auto_20151121_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlist',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 21, 20, 8, 37, 175960, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bucketlist',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
