"""This controls the model of the bucketlist"""
from django.db import models
from django.contrib import auth


class BucketList(models.Model):
    owner = models.ForeignKey(auth.models.User, related_name='bucketlists')
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=100, null=False)
    color = models.CharField(max_length=100, null=False, default="default")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_modified']

    def __str__(self):
        return self.name
