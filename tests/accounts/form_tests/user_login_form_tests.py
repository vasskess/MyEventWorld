from django.contrib.auth import get_user_model

from django.urls import reverse

from MyEventWorld.accounts.forms import UserLoginForm
from django.test import TestCase

User = get_user_model()


class UserLoginFormTests(TestCase):
    def setUp(self):
        self.valid_username = "test_email@example.com"
        self.invalid_username = "vaskes@example.com"
        self.valid_password = "11qwerty11"
        self.invalid_password = "11qwert22"
        self.user = User.objects.create_user(
            email=self.valid_username, password=self.valid_password
        )

    def test_invalid_login_invalid_username(self):
        url = reverse("login")
        data = {"username": self.invalid_username, "password": self.valid_password}
        form = UserLoginForm(data=data)
        response = self.client.post(url, data=form.data)
        self.assertFormError(response, "form", None, "Username is not valid")

    def test_invalid_login_invalid_password(self):
        url = reverse("login")
        data = {"username": self.valid_username, "password": self.invalid_password}
        form = UserLoginForm(data=data)
        response = self.client.post(url, data=form.data)
        self.assertFormError(response, "form", None, "Password is incorrect")
