from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from bucketlists.models import BucketList
from items.models import Item


class BucketListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test',
            password='test'
        )
        self.user.set_password('test')
        self.user.save()
        self.login = self.client.login(
            username='test', password='test')
        self.bucketlist = BucketList.objects.create(
            name='test_bucketlist', description='desc', color='green', owner=self.user)

        self.item = Item.objects.create(
            name='test items', bucketlist=self.bucketlist, description='a new desc', done=False)

    def tearDown(self):
        User.objects.all().delete()
        BucketList.objects.all().delete()
        Item.objects.all().delete()

    def test_item_can_be_done_or_undone(self):
        response = self.client.post(
            reverse('item_done', kwargs={'id': self.item.id}))
        response2 = self.client.post(
            reverse('item_done', kwargs={'id': self.item.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response2.status_code, 302)

    def test_item_can_be_deleted(self):
        response = self.client.post(
            reverse('item_delete', kwargs={'id': self.item.id}))
        
        self.assertEqual(response.status_code, 302)

    def test_item_can_be_edited(self):
        response = self.client.post(
            reverse('item_edit', kwargs={'id': self.item.id}),{'name':'edited item','description':'edited description'})
        
        self.assertEqual(response.status_code, 302)
