class ContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_interests"] = self.object.interest_set.all()
        context["all_events"] = self.object.event_set.all()
        return context
