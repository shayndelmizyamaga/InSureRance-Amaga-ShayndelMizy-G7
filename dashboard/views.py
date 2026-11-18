
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse

from accounts.models import CustomUser


class DashboardRedirectView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        if request.user.role == CustomUser.Role.ADMIN:
            return redirect("admin_dashboard")

        return redirect("user_dashboard")


class UserDashboardView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    template_name = "dashboard/user_dashboard.html"

    def test_func(self):
        return self.request.user.role == CustomUser.Role.USER

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["member_count"] = CustomUser.objects.count()
        return context


class AdminDashboardView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    template_name = "dashboard/admin_dashboard.html"

    def test_func(self):
        return self.request.user.role == CustomUser.Role.ADMIN

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["member_count"] = CustomUser.objects.count()
        context["user_count"] = CustomUser.objects.filter(
            role=CustomUser.Role.USER
        ).count()
        return context
