from django.core.exceptions import PermissionDenied
from django.views.generic import DetailView


class EventOwnershipMixin(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["is_owner"] = self.request.user.pk == self.object.creator.pk
        if not context["is_owner"]:
            raise PermissionDenied
        return context
