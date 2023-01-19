from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import DetailView


class NotLoginRequiredMixin:
    """
        This will not let user to manually access signin/login and register pages once its logged in
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("events-list")
        return super().dispatch(request, *args, **kwargs)


class UserOwnershipMixin(DetailView):
    """
        This will not let user to manually access other user profiles urls and edit or delete it
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["is_owner"] = self.request.user.pk == self.object.pk
        if not context["is_owner"]:
            raise PermissionDenied
        return context


class EventOwnershipMixin(DetailView):
    """
        This will not let user to manually access other user profiles events urls and edit or delete it
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["is_owner"] = self.request.user.pk == self.object.creator.pk
        if not context["is_owner"]:
            raise PermissionDenied
        return context


class InterestOwnershipMixin(DetailView):
    """
        This will not let user to manually access other user profiles interests and edit or delete it
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["interest_owner"] = self.request.user.id == self.object.interest_creator.pk
        if not context["interest_owner"]:
            raise PermissionDenied
        return context


class MessageOwnershipMixin(DetailView):
    """
        This will not let user to manually access other user profiles messages and edit or delete it
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["is_owner"] = self.request.user.pk == self.object.receiver.pk
        if not context["is_owner"]:
            raise PermissionDenied
        return context
