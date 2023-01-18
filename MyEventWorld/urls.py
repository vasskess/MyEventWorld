from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("MyEventWorld.events.urls")),
    path("users/", include("MyEventWorld.accounts.urls")),
    path("common/", include("MyEventWorld.common_stuff.urls")),
]
