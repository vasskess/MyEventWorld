from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth import admin as auth_admin

from MyEventWorld.accounts.forms import ProfileCreationForm
from MyEventWorld.accounts.models import EventProfile

UserModel = get_user_model()


@admin.register(UserModel)
class EventUserAdmin(auth_admin.UserAdmin):
    EVENT_USERS_PER_PAGE = 50

    list_display = (
        "email",
        "date_joined",
        "last_login",
        "is_superuser",
        "is_staff",
    )
    list_filter = ("date_joined",)
    ordering = ("-is_superuser",)
    search_fields = (
        "is_superuser",
        "is_staff",
    )
    sortable_by = (
        "email",
        "last_login",
    )
    readonly_fields = ["date_joined"]
    add_form = ProfileCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.

    fieldsets = (
        (None, {"fields": ()}),
        ("Personal info", {"fields": ("email",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "age",
                    "is_staff",
                ),
            },
        ),
    )
    list_per_page = EVENT_USERS_PER_PAGE


@admin.register(EventProfile)
class MyUserAdmin(admin.ModelAdmin):
    USERS_PER_PAGE = 50

    list_display = (
        "user",
        "first_name",
        "last_name",
        "age",
        "gender",
    )
    list_filter = (
        "first_name",
        "last_name",
    )
    search_fields = (
        "user",
        "first_name",
        "last_name",
    )
    sortable_by = (
        "user",
        "first_name",
        "last_name",
    )
    list_per_page = USERS_PER_PAGE
