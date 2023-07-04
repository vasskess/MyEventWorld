from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.urls import reverse

from MyEventWorld.accounts.models import EventProfile
from tests.accounts.base_test_case import BaseTestCase

User = get_user_model()


class UserProfileDeleteTest(BaseTestCase):
    def setUp(self):
        self.username = 'testuser@example.com'
        self.password = 'password123'
        self.user = User.objects.create_user(
            email=self.username,
            password=self.password
        )

    def test_profile_deletion_when_user_is_owner(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.post('/users/' + str(self.user.pk) + '/delete/')

        self.assertRedirects(response, reverse('login'))
        self.assertFalse(EventProfile.objects.filter(user=self.user).exists())

