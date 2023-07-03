from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class BaseTestCase(TestCase):
    def _create_user(self, user_data):
        response = self.client.post(
            reverse("register"),
            data=user_data,
        )
        user = response.wsgi_request.user
        return user
