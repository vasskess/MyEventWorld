from django.contrib.auth import get_user_model
from django.urls import reverse

from django.test import TestCase

User = get_user_model()


class UserEditTests(TestCase):
    def setUp(self):
        self.username = 'test_email@example.com'
        self.password = '11qwerty11'
        self.user = User.objects.create_user(
            email=self.username,
            password=self.password
        )

    def test_authenticated_user_is_owner(self):
        self.client.login(email=self.username, password=self.password)

        url = reverse('profile-details', kwargs={'pk': self.user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_is_not_owner(self):
        other_user = User.objects.create_user(
            email='other_email@example.com',
            password='11qwerty11'
        )

        self.client.login(email='other_email@example.com', password='11qwerty11')

        url = reverse('profile-details', kwargs={'pk': self.user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, 'error_403_template.html')

