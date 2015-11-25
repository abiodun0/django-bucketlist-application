# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlists', '0004_auto_20151122_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlist',
            name='color',
            field=models.CharField(default='success', max_length=100),
            preserve_default=False,
        ),
    ]
