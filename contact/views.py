from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        mnumber = request.POST['mnumber']
        message = request.POST['message']
        send_mail(
            'Contact Us', #title
            message, #message
            'settings.EMAIL_HOST_USER',
            ['siam.macos@gmail.com'], #receiver email
            fail_silently = False
        )
    return render(request, 'contactus.html')