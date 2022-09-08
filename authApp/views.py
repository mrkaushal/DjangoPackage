from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.

class AuthLoginView(View):
    template_name = 'authApp/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homeApp:dashboard')


class AuthLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/auth')
