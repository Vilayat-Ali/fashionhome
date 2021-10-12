from django.shortcuts import render
from .models import product

# Create your views here.
def shopPage(request):
    return render(request, 'shop/index.html', context={'products': product.objects.all()})