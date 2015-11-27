
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from bucketlists.models import BucketList
from items.models import Item



class UserViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test',
            password='test',
            email='abb@yahoo.com'
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

    def test_user_can_reach_index_page_login(self):
        response = self.client.get(
            reverse('index'))
        self.assertEqual(response.status_code, 302)

    def test_user_can_reach_index_page_logout(self):
        self.client.logout()
        response = self.client.get(
            reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_user_can_reach_index_page_logout(self):
        self.client.logout()
        response = self.client.get(
            reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_user_can_login(self):
        self.client.logout()
        data = {'username':'test','password':'test'}
        url = reverse('index')
        response = self.client.post(url,data=data)
        self.assertEqual(response.status_code, 302)

    def test_user_can_not_login_with_wrong_details(self):
        self.client.logout()
        data = {'username':'test','password':'testa'}
        url = reverse('index')
        response = self.client.post(url,data=data)
        self.assertEqual(response.status_code, 302)

    def test_user_cant_login_with_wrong_validation(self):
        self.client.logout()
        data = {'username_one':'test','passworda':'testa'}
        url = reverse('index')
        response = self.client.post(url,data=data)
        self.assertEqual(response.status_code, 200)

    def test_user_can_not_signup_with_the_same_username(self):
        self.client.logout()
        data = {'username':'test','password':'testa','email':'abb@yahoo.com','first_name':'abbbey','last_name':'kidna'}
        data2 = {'username':'test','password':'testa','password_conf':'test','email':'abb@yahoo.com','first_name':'abbbey','last_name':'kidna'}
        url = reverse('signup')
        response = self.client.post(url,data=data)
        response2 = self.client.post(url,data=data2)
        self.assertEqual(response.status_code, 200)
    def test_user_can_sign_up(self):
        self.client.logout()
        data = {'username':'testa','password':'testa','password_conf':'testa','email':'abbb@yahoo.com','first_name':'abbbey','last_name':'kidna'}
        url = reverse('signup')
        response = self.client.post(url,data=data)
        self.assertEqual(response.status_code, 302)

    def test_user_can_reach_dashboard(self):
        url = reverse('dashboard')
        response = self.client.get(url)
        response2 = self.client.get(url + "?page=200")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 200)

    def test_user_can_reach_profile_page(self):
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_can_not__edit_profile_with_wrong_details(self):
        data = {'password':'testa','email':'abb@yahoo.com','first_name':'abbbey','last_name':'kidna'}
        data2 = {'password':'testa','password_conf':'test','email':'abb@yahoo.com','first_name':'abbbey','last_name':'kidna'}
        url = reverse('profile')
        response = self.client.post(url,data)
        response2 = self.client.post(url,data2)
        self.assertEqual(response.status_code, 200)


    def test_user_can_eidt_profile(self):
        data = {'password':'testa','password_conf':'testa','email':'abb@yahoo.com','first_name':'abbbey','last_name':'kidna'}
        url = reverse('profile')
        response = self.client.post(url,data=data)
        self.assertEqual(response.status_code, 302)







