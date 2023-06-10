from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("my_event_world_admins/", admin.site.urls),
    path("", include("MyEventWorld.events.urls")),
    path("users/", include("MyEventWorld.accounts.urls")),
    path("common/", include("MyEventWorld.common_stuff.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
