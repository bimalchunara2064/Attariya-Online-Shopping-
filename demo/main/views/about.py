from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')