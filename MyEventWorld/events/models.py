import uuid

from django.db import models
from django.core.validators import MinLengthValidator

from cloudinary.models import CloudinaryField

from MyEventWorld.accounts.models import EventProfile
from MyEventWorld.core.helpers.event_types import Events


class Event(models.Model):
    TITLE_MIN_LEN = 3
    TITLE_MAX_LEN = 90
    TITLE_LEN_MESSAGE = f"Title must be at least {TITLE_MIN_LEN} characters long"

    EVENT_DESCRIPTION_MIN_LEN = 3
    EVENT_DESCRIPTION_MAX_LEN = 2500
    EVENT_DESCRIPTION_LEN_MESSAGE = f"Description must be at least {EVENT_DESCRIPTION_MIN_LEN} characters long"
    # Default messages will be used for: TITLE_MAX_LEN & EVENT_DESCRIPTION_MAX_LEN Validations

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
        validators=(MinLengthValidator(TITLE_MIN_LEN, TITLE_LEN_MESSAGE),),
        null=False,
        blank=False,
        verbose_name="Event title",
    )
    event_description = models.TextField(
        max_length=EVENT_DESCRIPTION_MAX_LEN,
        validators=(MinLengthValidator(EVENT_DESCRIPTION_MIN_LEN, EVENT_DESCRIPTION_LEN_MESSAGE),),
        null=False,
        blank=False,
        verbose_name="Event description",
    )
    event_category = models.CharField(
        max_length=Events.max_length(), choices=Events.choices()
    )
    creator = models.ForeignKey(
        EventProfile,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Event creator",
    )
    event_picture = CloudinaryField(
        null=True,
        blank=True,
        verbose_name="Event picture",
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    class Meta:
        ordering = ["-created", "-updated"]

    @property
    def get_event_avatar(self):
        if self.event_picture:
            return self.event_picture.url
        else:
            return "/static/images/events/default.png"

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list("review_creator__pk", flat=True)
        return queryset

    def __str__(self):
        return self.title


class Review(models.Model):
    REVIEW_TITLE_MIN_LEN = 2
    REVIEW_TITLE_MAX_LEN = 15

    REVIEW_TEXT_MIN_LEN = 5
    REVIEW_TEXT_MAX_LEN = 2500

    review_creator = models.ForeignKey(
        EventProfile,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Review creator",
    )
    review_for = models.ForeignKey(
        Event, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Event"
    )
    review_title = models.CharField(
        max_length=REVIEW_TITLE_MAX_LEN,
        validators=(MinLengthValidator(REVIEW_TITLE_MIN_LEN, ),),
        null=False,
        blank=False,
        verbose_name="Review title",
    )
    review_text = models.TextField(
        max_length=REVIEW_TEXT_MAX_LEN,
        validators=(MinLengthValidator(REVIEW_TEXT_MIN_LEN, ),),
        null=False,
        blank=False,
        help_text="Keep in mind this is one-time review and you wont be able to edit it!",
        verbose_name="Review text",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    class Meta:
        unique_together = [["review_creator", "review_for"]]

    def __str__(self):
        return self.review_title
