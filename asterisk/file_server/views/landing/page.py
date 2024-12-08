from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View

class LandingPage(View):
    def get(self, request):
        return render(request, "file_server/landing.html")

