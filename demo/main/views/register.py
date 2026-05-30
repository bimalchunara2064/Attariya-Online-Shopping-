from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from main.form import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, 'register.html', context)


    def post(self, request):
        # username=request.POST.get['username']
        # username=username.split('@')
        # real_username=username[0]
        # print(real_name)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # data=form.save(commit=False)
            # data.username=real_username
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Hey {username},Your account created successfully.')

            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)

            if request.user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('index')
        else:
            username = request.POST['username']
            messages.error(request, f'Something went wrong with{username},unable to create user!')
            context = {
                'form': form
            }
            return render(request, 'register.html', context)
