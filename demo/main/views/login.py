from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'login.html', )

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')



        try:
            # user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'you are now logged in')
                if request.user.is_superuser:
                    return redirect('/admin/')
                else:
                    return redirect('main:index')
            else:
                messages.warning(request, 'user does not Exist,Please create an aacount.')
                return redirect('login')
        except:
            messages.warning(request, 'Something went wrong,Please try again later.')
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you have been logged out')
        return redirect('index')