# Generated by Django 4.1.5 on 2023-01-13 09:59

import MyEventWorld.accounts.managers
import MyEventWorld.core.validators.file_size_validator
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "unique": "User with that email already exist !"
                        },
                        max_length=254,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="Staff status"),
                ),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", MyEventWorld.accounts.managers.EventUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="EventProfile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User email",
                    ),
                ),
                (
                    "profile_avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_avatars/",
                        validators=[
                            MyEventWorld.core.validators.file_size_validator.validate_file_less_than_3mb
                        ],
                        verbose_name="Profile avatar",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                3, "First name must be at least 3 characters long"
                            )
                        ],
                        verbose_name="First Name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                3, "Last name must be at least 3 characters long"
                            )
                        ],
                        verbose_name="Last Name",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        max_length=55,
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                3, "Location must be at least 3 characters long"
                            )
                        ],
                        verbose_name="Location",
                    ),
                ),
                (
                    "about_me",
                    models.TextField(
                        blank=True, max_length=2500, null=True, verbose_name="About me"
                    ),
                ),
                (
                    "age",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                18, message="Age must be between 18 and 122!"
                            ),
                            django.core.validators.MaxValueValidator(
                                122, message="Age must be between 18 and 122!"
                            ),
                        ],
                        verbose_name="Age",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Unpicked", "Unpicked"),
                            ("Male", "Male"),
                            ("Female", "Female"),
                        ],
                        default="Unpicked",
                        max_length=8,
                        null=True,
                        verbose_name="Gender",
                    ),
                ),
            ],
            options={
                "ordering": ["-user"],
            },
        ),
    ]
