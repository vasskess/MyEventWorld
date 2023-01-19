from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as password_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("MyEventWorld.events.urls")),
    path("users/", include("MyEventWorld.accounts.urls")),
    path("common/", include("MyEventWorld.common_stuff.urls")),
    path(
        "reset_password/",
        password_views.PasswordResetView.as_view(template_name="reset_password.html"),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        password_views.PasswordResetDoneView.as_view(
            template_name="reset_password_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        password_views.PasswordResetConfirmView.as_view(template_name="reset.html"),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        password_views.PasswordResetCompleteView.as_view(
            template_name="reset_password_complete.html"
        ),
        name="password_reset_complete",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
