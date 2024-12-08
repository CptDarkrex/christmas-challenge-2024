from django.urls import path

from . import views
from .views import (LandingPage, LoginView, SignUpView, LogoutView)

urlpatterns = [
    path("", LandingPage.as_view(), name="home"),

    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]