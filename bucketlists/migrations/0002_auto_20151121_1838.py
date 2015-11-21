# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bucketlist',
            old_name='user',
            new_name='owner',
        ),
    ]
