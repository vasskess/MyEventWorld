from django.test import TestCase
from MyEventWorld.accounts.models import EventProfile, EventUser


class GetUserUsernamePropertyTestCase(TestCase):
    def test_get_user_username_returns_correct_username(self):
        email = "vaskes@example.com"
        user = EventUser.objects.create(email=email)

        event_profile = EventProfile(user=user)

        expected_result = "Vaskes"
        self.assertEqual(event_profile.get_user_username, expected_result)

    def test_get_user_username_returns_incorrect_username(self):
        email = "vaskes@example.com"
        user = EventUser.objects.create(email=email)

        event_profile = EventProfile(user=user)

        expected_result = "vaskes"
        self.assertNotEqual(event_profile.get_user_username, expected_result)
