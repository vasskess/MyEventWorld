from django.urls import path, include

from MyEventWorld.events.views import *

urlpatterns = (
    path("", EventsList.as_view(), name="events-list"),
    path("event/create/", EventCreate.as_view(), name="event-create"),
    path(
        "<str:pk>/",
        include(
            [
                path("event/", EventDetails.as_view(), name="event-details"),
                path("update/", EventUpdate.as_view(), name="event-update"),
                path("delete/", EventDelete.as_view(), name="event-delete"),
            ]
        ),
    ),
)
