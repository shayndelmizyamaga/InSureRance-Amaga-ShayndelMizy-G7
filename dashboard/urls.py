
from django.urls import path

from .views import (
    DashboardRedirectView,
    UserDashboardView,
    AdminDashboardView,
)

urlpatterns = [
    path(
        "",
        DashboardRedirectView.as_view(),
        name="dashboard"
    ),
    path(
        "user-dashboard/",
        UserDashboardView.as_view(),
        name="user_dashboard"
    ),
    path(
        "admin-dashboard/",
        AdminDashboardView.as_view(),
        name="admin_dashboard"
    ),
]
