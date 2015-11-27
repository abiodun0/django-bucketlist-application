"""Test for the bucketlist views"""

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

    def test_can_reach_bucketlist_page(self):
        response = self.client.get(
            reverse('edit_bucketlist', kwargs={'id': self.bucketlist.id}))
        self.assertEqual(response.status_code, 200)

    def test_can_reach_max_page(self):
        response = self.client.get(
            reverse('edit_bucketlist', kwargs={'id': self.bucketlist.id}) + '?page=200')

        self.assertEqual(response.status_code, 200)

    def test_can_create_bucketlist(self):
        data = {'name': 'abiodun', 'description': 'olx', 'color': 'blue'}
        url = reverse('bucketlists')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_user_can_edit_bucketlist_collections(self):
        data = {'name': 'abiodun', 'description': 'olx', 'color': 'blue'}
        url = reverse('edit_bucketlist', kwargs={'id': self.bucketlist.id})
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_user_can_add_item_to_bucketlist(self):
        data = {'name': 'abiodun', 'description': 'olx'}
        url = reverse('add_item', kwargs={'id': self.bucketlist.id})
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_user_can_deletebucketlist(self):
        url = reverse('delete_bucketlist', kwargs={'id': self.bucketlist.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
