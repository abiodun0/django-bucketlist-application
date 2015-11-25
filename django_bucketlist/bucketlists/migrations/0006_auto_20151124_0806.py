# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlists', '0005_bucketlist_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bucketlist',
            options={'ordering': ['-date_modified']},
        ),
        migrations.AlterField(
            model_name='bucketlist',
            name='color',
            field=models.CharField(default=b'default', max_length=100),
        ),
    ]
