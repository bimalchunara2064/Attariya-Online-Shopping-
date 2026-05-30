from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

class CategoryView(View):
    def get(self, request):
        return render(request,'category.html')