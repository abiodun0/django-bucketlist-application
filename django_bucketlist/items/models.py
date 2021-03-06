"""This controls the model for the Item App"""
from django.db import models
from bucketlists.models import BucketList


class Item(models.Model):
    bucketlist = models.ForeignKey(BucketList, related_name='items')
    description = models.TextField(null=False, blank=False)
    name = models.TextField(null=False, blank=False)
    done = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_modified']

    def __str__(self):
        return self.name
