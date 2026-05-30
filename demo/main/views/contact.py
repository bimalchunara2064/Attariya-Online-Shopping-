from django.shortcuts import render
from django.views import View
from main.models.contact import Contact

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contact.objects.create(
            name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            message=message,
        )
        return render(request, 'contact.html', {
            'success_message': 'Your message has been sent successfully.',
        })

    