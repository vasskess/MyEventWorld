from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from MyEventWorld.core.mixins.ownership_mixins import EventOwnershipMixin
from MyEventWorld.events.forms import *
from MyEventWorld.events.models import *
from MyEventWorld.accounts.models import EventProfile


class EventsList(ListView):
    model = Event
    context_object_name = "events"
    template_name = "events/events.html"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("search", None)

        if query:
            queryset = Event.objects.distinct().filter(
                Q(title__icontains=query)
                | Q(event_description__icontains=query)
                | Q(event_category__icontains=query)
            )
        return queryset


class EventDetails(DetailView):
    model = Event
    template_name = "events/event_details.html"

    def post(self, request, *args, **kwargs):
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.review_for = Event.objects.get(id=self.kwargs["pk"])
            review.review_creator = EventProfile.objects.get(
                user_id=self.request.user.pk
            )
            review.save()
            return self.get(request, *args, **kwargs)
        messages.error(
            self.request,
            f"Review title must be at least {form.instance.__class__.REVIEW_TITLE_MIN_LEN} \
                and maximum {form.instance.__class__.REVIEW_TITLE_MAX_LEN} characters long ! \
                Review text must be at least {form.instance.__class__.REVIEW_TEXT_MIN_LEN} \
                and maximum {form.instance.__class__.REVIEW_TEXT_MAX_LEN} characters long !"
        )
        return redirect(request.META["HTTP_REFERER"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateReviewForm
        context["all_reviews"] = self.object.review_set.all
        return context


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    form_class = CreateEventForm
    context_object_name = "event"
    template_name = "events/event_create.html"

    def form_valid(self, form):
        form.instance.creator = EventProfile.objects.get(user_id=self.request.user.pk)
        form.instance.event_picture = form.cleaned_data["event_picture"]
        messages.error(
            self.request,
            "Event created successfully",
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "profile-details",
            kwargs={
                "pk": self.request.user.pk,
            },
        )


class EventUpdate(LoginRequiredMixin, EventOwnershipMixin, UpdateView):
    model = Event
    form_class = EditEventForm
    context_object_name = "event"
    template_name = "events/event_update.html"

    def get_success_url(self):
        return reverse_lazy(
            "profile-details",
            kwargs={
                "pk": self.request.user.pk,
            },
        )


class EventDelete(LoginRequiredMixin, EventOwnershipMixin, DeleteView):
    model = Event
    form_class = DeleteEventForm
    template_name = "events/event_delete.html"

    def get_success_url(self):
        return reverse_lazy(
            "profile-details",
            kwargs={
                "pk": self.request.user.pk,
            },
        )
