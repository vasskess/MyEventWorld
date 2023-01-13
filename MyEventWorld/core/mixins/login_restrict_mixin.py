from django.shortcuts import redirect


class NotLoginRequiredMixin:
    """
    This will not let user to manually access signin/login and register pages once its logged in
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("events-list")
        return super().dispatch(request, *args, **kwargs)
