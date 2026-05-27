from django.contrib.auth import views as auth_views
from django.urls import path

from .views import DashboardView, HomeView, ProductsView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="/"),
        name="logout",
    ),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("products/", ProductsView.as_view(), name="products"),
]
