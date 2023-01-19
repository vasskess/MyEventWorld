from django.urls import path, include
from MyEventWorld.accounts.views import *

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
)

from .signals import *
