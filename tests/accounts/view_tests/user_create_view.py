from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.accounts.base_test_case import BaseTestCase

User = get_user_model()


class UserCreateViewTests(BaseTestCase):
    def setUp(self):
        self.username = 'testuser@example.com'
        self.password = 'password123'
        self.user = User.objects.create_user(
            email=self.username,
            password=self.password
        )

    def test_valid_login(self):
        url = reverse('login')
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(url, data)

        expected_status_code = 302

        self.assertRedirects(response, reverse('events-list'))

        self.assertEquals(response.status_code, expected_status_code)

