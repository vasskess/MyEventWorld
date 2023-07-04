from django.contrib.auth import get_user_model

from django.urls import reverse

from MyEventWorld.accounts.forms import UserLoginForm
from tests.accounts.base_test_case import BaseTestCase

user = get_user_model()


class UserLoginFormTests(BaseTestCase):
    def setUp(self):
        self.username = "test_email@example.com"
        self.password = "11qwerty11"
        self.user = user.objects.create_user(
            email=self.username, password=self.password
        )

    def test_invalid_login_invalid_username(self):
        url = reverse("login")
        data = {"username": "vaskes@example.com", "password": self.password}
        form = UserLoginForm(data=data)
        response = self.client.post(url, data=form.data)
        self.assertFormError(response, "form", None, "Username is not valid")

    def test_invalid_login_invalid_password(self):
        url = reverse("login")
        data = {"username": self.username, "password": "11qwerty22"}
        form = UserLoginForm(data=data)
        response = self.client.post(url, data=form.data)
        self.assertFormError(response, "form", None, "Password is incorrect")
