from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm

from MyEventWorld.core.helpers.gender_types import Genders

from MyEventWorld.accounts.models import EventProfile
from MyEventWorld.core.mixins.form_fields_mixin import DisabledFieldsMixin

UserModel = get_user_model()


class ProfileCreationForm(UserCreationForm):
    AGE_MIN_VALUE = 18
    AGE_MAX_VALUE = 122
    AGE_VALIDATION_MESSAGE = f"Age must be between {AGE_MIN_VALUE} and {AGE_MAX_VALUE}!"

    age = forms.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE, message=AGE_VALIDATION_MESSAGE),
            MaxValueValidator(AGE_MAX_VALUE, message=AGE_VALIDATION_MESSAGE),
        )
    )

    gender = forms.CharField(
        widget=forms.RadioSelect(choices=Genders.choices()),
        initial=Genders.Unpicked.name,
        required=True,
    )

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)

    def clean_email(self):
        data = self.cleaned_data["email"]
        return data.lower()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = EventProfile(
            age=self.cleaned_data["age"],
            gender=self.cleaned_data["gender"],
            user=user,
        )
        if commit:
            profile.save()

        return user


class ProfileEditForm(ModelForm):
    gender = forms.CharField(
        widget=forms.RadioSelect(choices=Genders.choices()),
        initial=Genders.Unpicked.name,
        required=True,
    )

    class Meta:
        model = EventProfile
        exclude = ("user",)


class ProfileDeleteForm(DisabledFieldsMixin, ModelForm):
    class Meta:
        model = EventProfile
        fields = "__all__"


class UserLoginForm(AuthenticationForm):
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            if not UserModel.objects.filter(email=username):
                raise forms.ValidationError("Username is not valid")

            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("Password is incorrect")

        return super().clean()
