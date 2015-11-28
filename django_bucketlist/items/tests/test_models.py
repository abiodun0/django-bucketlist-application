"""Test Cases for the model items test """

from django.test import TestCase
from bucketlists.models import BucketList
from items.models import Item
from django.contrib.auth.models import User


class ItemModelsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='inioluwafageyinbo', password='codango')
        self.bucketlist = BucketList.objects.create(
            name='test bucket',
            owner=self.user,
            description='help file'
        )
        self.item = Item.objects.create(
            name='test item', bucketlist=self.bucketlist, description="one on one bucket", done=False)

    def tearDown(self):
        User.objects.all().delete()
        BucketList.objects.all().delete()
        Item.objects.all().delete()

    def test_can_get_bucketlist(self):
        item = str(self.item)
        self.assertIsNotNone(item)
