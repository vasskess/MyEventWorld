from django.urls import path, include
from MyEventWorld.accounts.views import (
    UsersList,
    UserCreate,
    UserLogin,
    UserLogout,
    UserDetails,
    UserProfile,
    UserProfileEdit,
    UserProfileDelete,
    UserPasswordReset,
    UserPasswordResetDone,
    UserPasswordConfirmation,
    UserPasswordResetComplete,
)

urlpatterns = (
    path("", UsersList.as_view(), name="users-list"),
    path("register/", UserCreate.as_view(), name="register"),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path(
        "<str:pk>/",
        include(
            [
                path("creator/", UserDetails.as_view(), name="user-details"),
                path("profile/", UserProfile.as_view(), name="profile-details"),
                path("edit/", UserProfileEdit.as_view(), name="profile-edit"),
                path("delete/", UserProfileDelete.as_view(), name="profile-delete"),
            ]
        ),
    ),
    path(
        "reset_password/",
        UserPasswordReset.as_view(),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        UserPasswordResetDone.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        UserPasswordConfirmation.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        UserPasswordResetComplete.as_view(),
        name="password_reset_complete",
    ),
)

from .signals import *
