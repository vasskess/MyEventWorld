from django.shortcuts import redirect


class NotLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("events-list")
        return super().dispatch(request, *args, **kwargs)
