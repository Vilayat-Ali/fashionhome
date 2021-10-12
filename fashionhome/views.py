from django.shortcuts import render
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from .forms import contactForm

def home(request):
    context = {
        'title': 'FashionHome | Home',
        'keywords': 'shopping, buy online cheap clothes, cash on delivery, fast delivery, meesho, sanchit raj, instagram, reliable',
        'description': 'FashionHome is an independent fashion brand that sponsers big fashion brands at very affordable prices with cash on delivery!'

    }
    return render(request, './home/index.html', context)

def about(request):
    context = { 
        'title': 'FashionHome | About',
        'keywords': 'shopping, buy online cheap clothes, cash on delivery, fast delivery, meesho',
        'description': 'At Fashion Home, we are feulled by the dream of providing high standards of fashion at affordable prices to our lovely community. We are a dedicated team of fashion experts with years of experience, so you can trust our recommendations blindly! We feature hundreds of brands, with different fashion tastes to cater all your fashionable vims and desires. Our products are guarded by their actual fitting size and high-quality raw materials, meaning our products are of high-quality with easy returns.'

    }
    return render(request, './about/index.html', context)

def contact(request):
    context = {
    'title': 'FashionHome | Contact',
    'keywords': 'shopping, buy online cheap clothes, cash on delivery, fast delivery, meesho, sanchit raj, instagram, reliable',
    'description': 'Any queries? We are here to help you! Write to us at customers.fashionhome@gmail.com'

    }
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
        
    return render(request, './contact/index.html', context)