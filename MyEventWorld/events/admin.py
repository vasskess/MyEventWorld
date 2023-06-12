from django.contrib import admin

from MyEventWorld.events.models import Event, Review


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    EVENTS_PER_PAGE = 3

    list_display = (
        "title",
        "event_category",
        "creator",
        "created",
        "updated",
    )
    list_filter = (
        "created",
        "updated",
    )
    ordering = ("-updated",)
    search_fields = ("title", "creator")
    sortable_by = (
        "title",
        "creator",
        "event_category",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "creator",
                    "title",
                    "event_description",
                    "event_category",
                    "event_picture",
                ),
            },
        ),
    )
    list_per_page = EVENTS_PER_PAGE


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    REVIEWS_PER_PAGE = 15

    list_display = (
        "review_title",
        "review_creator",
        "review_for",
        "date_created",
    )
    list_filter = ("date_created",)
    ordering = ("-date_created",)
    search_fields = (
        "review_title",
        "review_creator",
    )
    sortable_by = ("review_title",)
    list_per_page = REVIEWS_PER_PAGE
