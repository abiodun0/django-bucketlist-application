from django.test.utils import setup_test_environment
setup_test_environment()
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse

from bucketlists.models import BucketList
from items.models import Item
from rest_framework.authtoken.models import Token


class ApiViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='user',
            password='user'
        )
        self.bucket = BucketList.objects.create(
            name='test_bucketlist', owner=self.user)

        self.item = Item.objects.create(name='bucket list item', description='this is an optional bucket list',
                                        bucketlist=self.bucket, done=False)

        # generate token for the user
        token = Token.objects.get(user_id=self.user.id)
        # Include appropriate 'Authorization:' header on al request
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def tearDown(self):
        User.objects.all().delete()
        BucketList.objects.all().delete()

    def test_get_user_profile(self):
        url = reverse("api_profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_new_user(self):
        url = reverse("api_profile")
        data = {'username': "Abiodun", "password": "abiodun",
                "email": "abbey@yahoo.com"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_get_bucketlist(self):
        url = reverse("api_bucketlist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bucketlist(self):
        url = reverse("api_bucketlist")
        data = {'name': 'This is a test bucketlist'}
        data2 = {'noname': "noname"}
        response = self.client.post(url, data)
        response2 = self.client.post(url, data2)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response2.status_code, 400)

    def test_get_single_bucketlist(self):
        url = reverse("api_edit_bucketlist", kwargs={'id': self.bucket.id})
        data = {"name": "Edited bucketlist"}
        data2 = {"noname": "ladi"}
        response = self.client.get(url)
        response2 = self.client.put(url, data)
        response3 = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 201)
        self.assertEqual(response3.status_code, 200)

    def test_create_an_item(self):
        url = reverse("api_bucketlist_items", kwargs={'id': self.bucket.id})
        data = {"name": "New bucketlist items",
                "description": "just another one"
                }
        data2 = {"surname": "New bucketlist items"
                 }
        response = self.client.post(url, data)
        response2 = self.client.post(url, data2)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response2.status_code, 400)

    def test_create_edit_item(self):
        url = reverse("api_edit_bucketlist_items", kwargs={
                      'id': self.bucket.id, 'item_id': self.item.id})
        data = {"name": "New bucketlist items"}

        response = self.client.put(url, data)
        response2 = self.client.delete(url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response2.status_code, 200)
