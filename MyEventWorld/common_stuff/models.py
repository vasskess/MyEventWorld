import uuid

from django.db import models
from django.core.validators import MinLengthValidator

from MyEventWorld.accounts.models import EventProfile


class Interest(models.Model):
    TITLE_MIN_LEN = 2
    TITLE_MAX_LEN = 30
    TITLE_LEN_MESSAGE = f"Title must be at least {TITLE_MIN_LEN} characters long"

    DESCRIPTION_MIN_LEN = 2
    DESCRIPTION_MAX_LEN = 2500
    DESCRIPTION_LEN_MESSAGE = (
        f"Description must be at least {DESCRIPTION_MIN_LEN} characters long"
    )

    interest_creator = models.ForeignKey(
        EventProfile,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Interest creator",
    )
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        validators=(MinLengthValidator(TITLE_MIN_LEN, TITLE_LEN_MESSAGE),),
        null=False,
        blank=False,
        verbose_name="Interest title",
    )
    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
        validators=(MinLengthValidator(DESCRIPTION_MIN_LEN, DESCRIPTION_LEN_MESSAGE),),
        null=True,
        blank=True,
        verbose_name="Interest description",
    )
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )

    def __str__(self):
        return self.title


class Message(models.Model):
    TOPIC_MIN_LEN = 2
    TOPIC_MAX_LEN = 200
    TOPIC_LEN_MESSAGE = f"Topic must contain at least {TOPIC_MIN_LEN} characters"

    TEXT_MIN_LEN = 2
    TEXT_MAX_LEN = 2500
    TEXT_LEN_MESSAGE = f"Field must contain at least {TEXT_MIN_LEN} characters"

    sender = models.ForeignKey(
        EventProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Message sender",
    )
    receiver = models.ForeignKey(
        EventProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="messages",
        verbose_name="Message receiver",
    )

    topic = models.CharField(
        max_length=TOPIC_MAX_LEN,
        validators=(MinLengthValidator(TOPIC_MIN_LEN, message=TOPIC_LEN_MESSAGE),),
        null=False,
        blank=False,
        verbose_name="Message topic",
    )
    message_text = models.TextField(
        max_length=TEXT_MAX_LEN,
        validators=(MinLengthValidator(TEXT_MIN_LEN, message=TEXT_LEN_MESSAGE),),
        null=False,
        blank=False,
        verbose_name="Message text",
    )
    read = models.BooleanField(default=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ["read", "-date_created"]
