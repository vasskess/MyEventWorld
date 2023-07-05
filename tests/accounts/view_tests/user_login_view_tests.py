from django.test import TestCase

from django.contrib.auth import get_user_model, get_user
from django.urls import reverse

User = get_user_model()


class UserLoginViewTest(TestCase):
    def setUp(self):
        self.username = 'test_email@example.com'
        self.password = '11qwerty11'
        self.user = User.objects.create_user(
            email=self.username,
            password=self.password
        )

    def test_user_is_logged_in(self):
        url = reverse('login')
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(url, data)

        self.assertRedirects(response, reverse('events-list'))

        logged_user = get_user(self.client)

        self.assertTrue(logged_user.is_authenticated)
        self.assertEqual(logged_user, self.user)

    def test_user_not_logged_in(self):
        response = self.client.get(reverse('logout'))

        self.assertRedirects(response, reverse('login'))

        session_user = get_user(self.client)

        self.assertTrue(session_user.is_anonymous)
