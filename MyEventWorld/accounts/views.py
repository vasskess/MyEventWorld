from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages

from MyEventWorld.accounts.mixins.account_mixins import UserOwnershipMixin
from MyEventWorld.accounts.mixins.login_restrict_mixin import NotLoginRequiredMixin

from MyEventWorld.accounts.forms import (
    ProfileCreationForm,
    ProfileEditForm,
    ProfileDeleteForm,
    UserLoginForm,
)
from MyEventWorld.accounts.models import EventProfile
from MyEventWorld.core.mixins.context_mixin import ContextMixin


class UsersList(ListView):
    model = EventProfile
    context_object_name = "profiles"
    template_name = "accounts/event_creators.html"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("search", None)

        if query:
            queryset = EventProfile.objects.distinct().filter(
                Q(user__email__icontains=query)
                | Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
                | Q(gender__icontains=query)
                | Q(location__icontains=query)
                | Q(about_me__icontains=query)
                | Q(interest__title__icontains=query)
            )
        return queryset


class UserDetails(ContextMixin, DetailView):
    model = EventProfile
    template_name = "accounts/profile_details.html"


class UserProfile(LoginRequiredMixin, UserOwnershipMixin, ContextMixin, DetailView):
    model = EventProfile
    template_name = "accounts/profile.html"


class UserCreate(NotLoginRequiredMixin, CreateView):
    template_name = "accounts/login_register.html"
    form_class = ProfileCreationForm

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        messages.error(
            self.request,
            "Welcome! Manage your profile from MyProfile",
        )
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "register"
        return context

    def get_success_url(self):
        return reverse_lazy("events-list")


class UserProfileEdit(LoginRequiredMixin, UserOwnershipMixin, UpdateView):
    model = EventProfile
    form_class = ProfileEditForm
    template_name = "accounts/profile_edit.html"

    def get_success_url(self):
        return reverse_lazy(
            "profile-details",
            kwargs={
                "pk": self.request.user.pk,
            },
        )


class UserProfileDelete(LoginRequiredMixin, UserOwnershipMixin, DeleteView):
    model = EventProfile
    form_class = ProfileDeleteForm
    template_name = "accounts/profile_delete.html"

    def get_success_url(self):
        messages.success(self.request, "Profile was deleted successfully")
        return reverse_lazy("login")


class UserLogin(NotLoginRequiredMixin, LoginView):
    template_name = "accounts/login_register.html"
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "login"
        return context

    def get_success_url(self):
        return reverse_lazy("events-list")


class UserLogout(LogoutView):
    def get_success_url(self):
        return reverse_lazy("login")


class UserPasswordReset(PasswordResetView):
    template_name = "reset_password.html"


class UserPasswordResetDone(PasswordResetDoneView):
    template_name = "reset_password_sent.html"


class UserPasswordConfirmation(PasswordResetConfirmView):
    template_name = "reset_confirmation.html"


class UserPasswordResetComplete(PasswordResetCompleteView):
    template_name = "reset_password_complete.html"
