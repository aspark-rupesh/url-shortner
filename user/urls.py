from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path

from user.views import UserRegisterView, logout_user

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),


]