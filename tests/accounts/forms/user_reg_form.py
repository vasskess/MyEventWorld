from django.contrib.auth import get_user_model
from MyEventWorld.accounts.forms import ProfileCreationForm
from tests.accounts.base_test_case import BaseTestCase

UserModel = get_user_model()


class UserRegistrationFormTests(BaseTestCase):
    AGE_MIN_VALUE = 18
    AGE_MAX_VALUE = 122

    VALID_USER_REGISTER_DATA = {
        "email": "test_email@example.com",
        "age": 18,
        "gender": "Male",
        "password1": "11qwerty11",
        "password2": "11qwerty11",
    }

    INVALID_USER_REGISTER_DATA = {
        "email": "test_email@",
        "age": 17,
        "gender": "Female",
        "password1": "11qwerty11",
        "password2": "11qwerty22",
    }

    def test_profile_creation_form_when_form_valid_is_True(self):
        form = ProfileCreationForm(data=self.VALID_USER_REGISTER_DATA)
        self.assertTrue(form.is_valid())

    def test_profile_creation_form_with_email_already_exist(self):
        self._create_user(self.VALID_USER_REGISTER_DATA)

        form = ProfileCreationForm(data=self.VALID_USER_REGISTER_DATA)

        self.assertFalse(form.is_valid())
        self.assertEquals(
            form.errors["email"], ["User with that email already exist !"]
        )

    def test_profile_creation_form_when_email_is_invalid(self):
        form = ProfileCreationForm(data=self.INVALID_USER_REGISTER_DATA)
        self.assertEquals(form.errors["email"], ["Enter a valid email address."])

    def test_profile_creation_form_when_age_is_invalid(self):
        form = ProfileCreationForm(data=self.INVALID_USER_REGISTER_DATA)
        self.assertEquals(
            form.errors["age"],
            [f"Age must be between {self.AGE_MIN_VALUE} and {self.AGE_MAX_VALUE}!"],
        )

    def test_profile_creation_form_when_passwords_mismatch(self):
        form = ProfileCreationForm(data=self.INVALID_USER_REGISTER_DATA)

        self.assertFalse(form.is_valid())
        self.assertEquals(
            form.errors["password2"], ["Passwords confirmation does not match"]
        )
