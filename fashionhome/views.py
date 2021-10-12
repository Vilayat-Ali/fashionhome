from django.shortcuts import render
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from .forms import contactForm

def home(request):
    return render(request, './home/index.html')

def about(request):
    return render(request, './about/index.html')

def contact(request):
    if(request.method == 'POST'):
        submittedForm = contactForm(request.POST)
        if(submittedForm.is_valid()):
            messengers_info = { "name" : request.POST.get('name'),
                                "email" : request.POST.get('email'),
                                "subject" : request.POST.get('subject'),
                                "message" : "From: "+submittedForm.cleaned_data['name']+"\n"+"\n"+submittedForm.cleaned_data["message"]+"\n"+"\n"+"Sender's Email: "+submittedForm.cleaned_data["email"]
                              }
            print(messengers_info["name"])
            send_mail(
                messengers_info["subject"],
                messengers_info["message"],
                messengers_info["email"], # from
                ['customers.fashionhome@gmail.com'], # to
                fail_silently=False,
            )
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/contact")
        
    return render(request, './contact/index.html')