from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactFrom
from django.template.loader import render_to_string

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactFrom(request.POST)



        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            message = form.cleaned_data['message']
            
            html = render_to_string('contactform.html', {
                'name': name,
                'email': email,
                'mobile': mobile,
                'message': message
            })
            #print(form.cleaned_data['email'])
            #print("The form is valid")
            send_mail('The contact from the subject', 'This the message', 'siam.macos@gmail.com', ['siam.macos@gmail.com'], html_message=html) #macos@ is sender and khan8523@ is receiver

            return redirect('contact')
        
    else: 
        form = ContactFrom()

    return render(request, 'contactus.html', {
        'form': form
    })