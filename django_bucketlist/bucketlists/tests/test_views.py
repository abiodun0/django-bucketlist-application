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
            name='test_bucketlist', owner=self.user)

    def tearDown(self):
        User.objects.all().delete()
        BucketList.objects.all().delete()

    def test_can_reach_bucketlist_page(self):
        self.assertEqual(self.login, True)
        response = self.client.get(
            reverse('edit_bucketlist', kwargs={'id': self.bucketlist.id}))
        self.assertEqual(response.status_code, 200)

    # def test_request_for_empty_bucketlist_page(self):
    #     response = self.client.get(
    #         '/bucketlist?page=100000')
    #     # returns the last page available
    #     self.assertEqual(response.status_code, 200)

    # def test_can_make_a_bucketlist(self):
    #     response = self.client.post(
    #         reverse('bucketlist'), {
    #             'name': 'A new bucketlist'
    #         })
    #     self.assertEqual(response.status_code, 302)