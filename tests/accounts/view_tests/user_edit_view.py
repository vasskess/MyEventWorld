from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.urls import reverse

from tests.accounts.base_test_case import BaseTestCase

User = get_user_model()


class UserEditTests(BaseTestCase):
    def setUp(self):
        self.username = 'testuser@example.com'
        self.password = 'password123'
        self.user = User.objects.create_user(
            email=self.username,
            password=self.password
        )

    def test_authenticated_user_is_owner(self):
        self.client.login(email='testuser@example.com', password='password')

        url = reverse('profile-details', kwargs={'pk': self.user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_is_not_owner(self):
        other_user = User.objects.create_user(
            email='otheruser@example.com',
            password='password'
        )

        self.client.login(email='otheruser@example.com', password='password')

        url = reverse('profile-details', kwargs={'pk': self.user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)
        self.assertRaises(PermissionDenied)

