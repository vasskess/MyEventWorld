from django.core.exceptions import PermissionDenied
from django.views.generic import DetailView


class UserOwnershipMixin(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["is_owner"] = self.request.user.pk == self.object.pk
        if not context["is_owner"]:
            raise PermissionDenied
        return context
