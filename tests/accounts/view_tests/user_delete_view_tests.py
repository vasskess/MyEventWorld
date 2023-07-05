from django.contrib.auth import get_user_model
from django.urls import reverse

from MyEventWorld.accounts.models import EventProfile
from tests.accounts.base_test_case import BaseTestCase

User = get_user_model()


class UserProfileDeleteTest(BaseTestCase):
    def setUp(self):
        self.username = 'test_email@example.com'
        self.password = '11qwerty11'
        self.user = User.objects.create_user(
            email=self.username,
            password=self.password
        )

    def test_profile_deletion_when_user_is_owner(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.post('/users/' + str(self.user.pk) + '/delete/')

        self.assertRedirects(response, reverse('login'))
        self.assertFalse(EventProfile.objects.filter(user=self.user).exists())

    def test_profile_deletion_when_user_is_not_owner(self):
        other_user = User.objects.create_user(
            email='other_email@example.com',
            password='11qwerty11'
        )

        self.client.login(email='other_email@example.com', password='11qwerty11')

        url = reverse('profile-delete', kwargs={'pk': self.user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, 'error_403_template.html')
