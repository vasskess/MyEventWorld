from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from MyEventWorld.accounts.views import (
    UserPasswordReset,
    UserPasswordResetDone,
    UserPasswordConfirmation,
    UserPasswordResetComplete,
)

urlpatterns = [
    path("my_event_world_admins/", admin.site.urls),
    path("", include("MyEventWorld.events.urls")),
    path("users/", include("MyEventWorld.accounts.urls")),
    path("common/", include("MyEventWorld.common_stuff.urls")),
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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
