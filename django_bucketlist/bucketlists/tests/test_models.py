""" Test cases for bucketlist models """

from django.test import TestCase
from bucketlists.models import BucketList
from django.contrib.auth.models import User


class BucketListTestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='inioluwafageyinbo', password='codango')
        self.bucketlist = BucketList.objects.create(
            name='test bucket',
            owner=self.user,
            description='help file'
        )

    def tearDown(self):
        User.objects.all().delete()
        BucketList.objects.all().delete()

    def test_can_get_bucketlist(self):
        bucketlist = str(self.bucketlist)
        self.assertIsNotNone(bucketlist)
