from django.forms import ModelForm

from MyEventWorld.events.models import *


class BaseEventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            "title",
            "event_description",
            "event_picture",
            "event_category",
        )


class CreateEventForm(BaseEventForm):
    pass


class EditEventForm(BaseEventForm):
    pass


class DeleteEventForm(BaseEventForm):
    pass


class CreateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["review_title", "review_text"]
