from django.urls import path, include
from MyEventWorld.common_stuff.views import *

urlpatterns = (
    path("interest/create/", InterestCreate.as_view(), name="interest-create"),
    path(
        "<str:pk>/",
        include(
            [
                path("update/", InterestUpdate.as_view(), name="interest-update"),
                path("delete/", InterestDelete.as_view(), name="interest-delete"),
            ]
        ),
    ),
    path("inbox/<str:pk>/", MessageInbox.as_view(), name="message-inbox"),
    path("message/<str:pk>/", ReadMessage.as_view(), name="message-read"),
    path("create-message/<str:pk>/", CreateMessage.as_view(), name="message-create"),
    path("delete-message/<str:pk>/", DeleteMessage.as_view(), name="message-delete"),
)
