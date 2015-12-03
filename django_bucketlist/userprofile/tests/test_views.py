""" Testcases for the user profile """
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
        """ Test logged in user can reach the dashboard 
        """
        response = self.client.get(
            reverse('index'))
        self.assertEqual(response.status_code, 302)

    def test_user_can_reach_index_page_logout(self):
        """ Test Guest directed to the home page 
        """
        self.client.logout()
        response = self.client.get(
            reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_user_can_reach_singup_page_logout(self):
        """ Test guest can reach signup page layout 
        """
        self.client.logout()
        response = self.client.get(
            reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_user_can_login(self):
        """ Test authenticated user can login 
        """
        self.client.logout()
        data = {'username': 'test', 'password': 'test'}
        url = reverse('index')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_user_can_not_login_with_wrong_details(self):
        """ Test for wrong credentials can not login
        """
        self.client.logout()
        data = {'username': 'test', 'password': 'testa'}
        url = reverse('index')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_user_cant_login_with_wrong_validation(self):
        """ Test wrong validation message cannot login 
        """
        self.client.logout()
        data = {'username_one': 'test', 'passworda': 'testa'}
        url = reverse('index')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_user_can_not_signup_with_the_same_username(self):
        """ Test for uniqueness of username email and password validation 
        """
        self.client.logout()
        data = {'username': 'test', 'password': 'testa', 'email':
                'abb@yahoo.com', 'first_name': 'abbbey', 'last_name': 'kidna'}
        data2 = {'username': 'test', 'password': 'testa', 'password_conf': 'test',
                 'email': 'abb@yahoo.com', 'first_name': 'abbbey', 'last_name': 'kidna'}
        url = reverse('signup')
        response = self.client.post(url, data=data)
        response2 = self.client.post(url, data=data2)
        self.assertEqual(response.status_code, 200)

    def test_user_can_sign_up(self):
        """ User can signup with unique email, and valid password combination
        """
        self.client.logout()
        data = {'username': 'testa', 'password': 'testa', 'password_conf': 'testa',
                'email': 'abbb@yahoo.com', 'first_name': 'abbbey', 'last_name': 'kidna'}
        url = reverse('signup')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_user_can_reach_dashboard(self):
        """Authenticated user can reach the dashboard
        Test for max page returns the last page 
        """
        url = reverse('dashboard')
        response = self.client.get(url)
        response2 = self.client.get(url + "?page=200")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 200)

    def test_user_can_reach_profile_page(self):
        """ Authenticated user can reach the profile edit page 
        """
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_can_not__edit_profile_with_wrong_details(self):
        """ User cannot change password with wrong password combination
        """
        data = {'password': 'testa', 'email': 'abb@yahoo.com',
                'first_name': 'abbbey', 'last_name': 'kidna'}
        data2 = {'password': 'testa', 'password_conf': 'test', 'email':
                 'abb@yahoo.com', 'first_name': 'abbbey', 'last_name': 'kidna'}
        url = reverse('profile')
        response = self.client.post(url, data)
        response2 = self.client.post(url, data2)
        self.assertEqual(response.status_code, 200)

    def test_user_can_edit_profile(self):
        """ User can edit profile with valid password combination
        """
        data = {'password': 'testa', 'password_conf': 'testa', 'email':
                'abb@yahoo.com', 'first_name': 'abbbey', 'last_name': 'kidna','username':'test'}
        url = reverse('profile')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
