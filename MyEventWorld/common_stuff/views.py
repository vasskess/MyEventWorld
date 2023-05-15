from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)

from MyEventWorld.core.mixins.ownership_mixins import InterestOwnershipMixin, MessageOwnershipMixin
from MyEventWorld.common_stuff.forms import *
from MyEventWorld.common_stuff.models import *


class InterestCreate(LoginRequiredMixin, CreateView):
    model = Interest
    form_class = CreateInterestForm
    template_name = "common_stuff/interest_create.html"

    def form_valid(self, form):
        form.instance.interest_creator = EventProfile.objects.get(
            user_id=self.request.user.pk
        )
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Interest created successfully")
        return reverse_lazy(
            "profile-details",
            kwargs={
                "pk": self.request.user.pk,
            },
        )


class InterestUpdate(LoginRequiredMixin, InterestOwnershipMixin, UpdateView):
    model = Interest
    form_class = EditInterestForm
    template_name = "common_stuff/interest_update.html"

    def get_success_url(self):
        messages.success(self.request, "Interest updated successfully")
        return reverse_lazy(
            "profile-details",
            kwargs={
                "pk": self.request.user.pk,
            },
        )


class InterestDelete(LoginRequiredMixin, InterestOwnershipMixin, DeleteView):
    model = Interest
    form_class = DeleteInterestForm
    template_name = "common_stuff/interest_delete.html"

    def get_success_url(self):
        messages.success(self.request, "Interest deleted successfully")
        return reverse_lazy(
            "profile-details",
            kwargs={
                "pk": self.request.user.pk,
            },
        )


class MessageInbox(LoginRequiredMixin, ListView):
    model = Message
    template_name = "common_stuff/inbox.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["receiver"] = EventProfile.objects.get(pk=self.request.user.pk)
        context["messages_received"] = Message.objects.filter(
            receiver_id=self.request.user.pk
        ).all()
        context["unread"] = Message.objects.filter(
            receiver_id=self.request.user.pk, read=False
        ).count()
        return context


class CreateMessage(LoginRequiredMixin, CreateView):
    model = Message
    form_class = CreateMessageForm
    template_name = "common_stuff/message_create.html"

    def form_valid(self, form):
        form.instance.sender = EventProfile.objects.get(user_id=self.request.user.pk)
        form.instance.receiver = EventProfile.objects.get(user_id=self.kwargs["pk"])
        if form.instance.sender == form.instance.receiver:
            # This will not let user manually access its pk and send message to its self
            raise PermissionDenied
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Message sent successfully")
        return reverse_lazy("users-list")


class ReadMessage(LoginRequiredMixin, MessageOwnershipMixin, DetailView):
    model = Message
    context_object_name = "message"
    template_name = "common_stuff/messages.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages_received"] = Message.objects.filter(
            id=self.kwargs["pk"]
        ).get()
        context["unread"] = Message.objects.filter(id=self.kwargs["pk"]).update(
            read=True
        )
        return context


class DeleteMessage(LoginRequiredMixin, MessageOwnershipMixin, DeleteView):
    model = Message
    form_class = DeleteMessageForm
    context_object_name = "message"
    template_name = "common_stuff/message_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message_to_delete"] = Message.objects.filter(
            id=self.kwargs["pk"]
        ).get()
        return context

    def get_success_url(self):
        messages.success(self.request, "Message deleted successfully")
        return reverse_lazy(
            "message-inbox",
            kwargs={
                "pk": self.request.user.pk,
            },
        )
