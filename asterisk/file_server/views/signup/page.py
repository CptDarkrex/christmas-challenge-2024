from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.db import IntegrityError
from django.contrib import messages


class SignUpView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name = 'file_server/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')  # Redirect to the home page

        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Authenticate and login the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page or dashboard
            else:
                # Return an 'invalid login' error message
                messages.error(request, 'Unable to log in with the provided credentials.')
        except IntegrityError:
            messages.error(request, 'Username already exists. Please choose a different one.')

        return render(request, self.template_name)