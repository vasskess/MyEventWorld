from django.core.exceptions import PermissionDenied
from django.views.generic import DetailView


class UserOwnershipMixin(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["is_owner"] = self.request.user.pk == self.object.pk
        if not context["is_owner"]:
            raise PermissionDenied
        return context


class EventOwnershipMixin(DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["is_owner"] = self.request.user.pk == self.object.creator.pk
        if not context["is_owner"]:
            raise PermissionDenied
        return context


class InterestOwnershipMixin(DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["interest_owner"] = self.request.user.id == self.object.interest_creator.pk
        if not context["interest_owner"]:
            raise PermissionDenied
        return context


class MessageOwnershipMixin(DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["is_owner"] = self.request.user.pk == self.object.receiver.pk
        if not context["is_owner"]:
            raise PermissionDenied
        return context
