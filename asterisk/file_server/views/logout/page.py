from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import View


class LogoutView(View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect('login')