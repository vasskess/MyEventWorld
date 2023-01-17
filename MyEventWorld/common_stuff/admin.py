from django.contrib import admin

from MyEventWorld.common_stuff.models import *


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    INTERESTS_PER_PAGE = 15

    list_display = (
        "title",
        "interest_creator",
        "description",
    )
    search_fields = (
        "title",
        "interest_creator",
    )
    sortable_by = ("title",)
    list_per_page = INTERESTS_PER_PAGE


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    MESSAGES_PER_PAGE = 50

    list_display = (
        "topic",
        "sender",
        "receiver",
        "message_text",
        "read",
    )
    ordering = ("-read",)
    sortable_by = (
        "topic",
        "sender",
        "receiver",
    )
    list_per_page = MESSAGES_PER_PAGE
