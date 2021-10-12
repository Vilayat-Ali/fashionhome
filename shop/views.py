from django.shortcuts import render
from .models import product

# Create your views here.
def shopPage(request):
    context = {
        'products': product.objects.all(), 
        'title': 'FashionHome | Shop',
        'keywords': 'shopping, buy online cheap clothes, cash on delivery, fast delivery, meesho',
        'description': 'FashionHome brings you the biggest haul of lastest fashion trend at prices too good to be true! Shop at fashionhome to avail excciting offers and discounts!'

    }
    return render(request, 'shop/index.html', context)