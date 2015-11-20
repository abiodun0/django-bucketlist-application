# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BucketList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('name', models.TextField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(related_name='bucketlists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
