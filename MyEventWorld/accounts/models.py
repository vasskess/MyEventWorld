import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

from cloudinary.models import CloudinaryField

from MyEventWorld.accounts.managers import EventUserManager
from MyEventWorld.core.helpers.gender_types import Genders


class EventUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_ERROR = "User with that email already exist !"

    email = models.EmailField(
        unique=True, null=False, blank=False, verbose_name="Email",
        error_messages={"unique": USERNAME_ERROR}
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(
        default=False, null=False, blank=False, verbose_name="Staff status"
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    USERNAME_FIELD = "email"

    objects = EventUserManager()


class EventProfile(models.Model):
    FIRST_NAME_MIN_LEN = 3
    FIRST_NAME_MAX_LEN = 20
    FIRST_NAME_MIN_LEN_MESSAGE = f"First name must be at least {FIRST_NAME_MIN_LEN} characters long"

    LAST_NAME_MIN_LEN = 3
    LAST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN_MESSAGE = f"Last name must be at least {LAST_NAME_MIN_LEN} characters long"

    LOCATION_MIN_LEN = 3
    LOCATION_MAX_LEN = 55
    LOCATION_MIN_LEN_MESSAGE = f"Location must be at least {LOCATION_MIN_LEN} characters long"

    ABOUT_ME_MAX_LEN = 2500
    '''
        Default messages will be used for:
        FIRST_NAME_MAX_LEN, LAST_NAME_MAX_LEN, LOCATION_MAX_LEN & ABOUT_ME_MAX_LEN Validations
    '''

    AGE_MIN_VALUE = 18
    AGE_MAX_VALUE = 122
    AGE_VALIDATION_MESSAGE = f"Age must be between {AGE_MIN_VALUE} and {AGE_MAX_VALUE}!"

    user = models.OneToOneField(
        EventUser,
        primary_key=True,
        on_delete=models.CASCADE,
        verbose_name="User email",
    )

    profile_avatar = CloudinaryField(
        null=True,
        blank=True,
        verbose_name="Profile avatar",
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(MinLengthValidator(FIRST_NAME_MIN_LEN, FIRST_NAME_MIN_LEN_MESSAGE),),
        null=True,
        blank=True,
        verbose_name="First Name",
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(MinLengthValidator(LAST_NAME_MAX_LEN, LAST_NAME_MIN_LEN_MESSAGE),),
        null=True,
        blank=True,
        verbose_name="Last Name",
    )
    location = models.CharField(
        max_length=LOCATION_MAX_LEN,
        validators=(MinLengthValidator(LOCATION_MIN_LEN, LOCATION_MIN_LEN_MESSAGE),),
        null=True,
        blank=True,
        verbose_name="Location",
    )
    about_me = models.TextField(
        max_length=ABOUT_ME_MAX_LEN, null=True, blank=True, verbose_name="About me"
    )
    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE, message=AGE_VALIDATION_MESSAGE),
            MaxValueValidator(AGE_MAX_VALUE, message=AGE_VALIDATION_MESSAGE),
        ),
        null=True,
        blank=True,
        verbose_name="Age",
    )
    gender = models.CharField(
        choices=Genders.choices(),
        max_length=Genders.max_length(),
        default=Genders.Unpicked.name,
        null=True,
        blank=True,
        verbose_name="Gender",
    )

    class Meta:
        ordering = ["-user"]

    @property
    def get_profile_avatar(self):
        if self.profile_avatar:
            return self.profile_avatar.url
        else:
            return "/static/images/profiles/default_avatar.png"

    @property
    def get_user_username(self):
        return self.user.email.split("@")[0].capitalize()

    def __str__(self):
        return self.get_user_username
