from django.shortcuts import render
from product.models import Product

def base(request):
    products=Product.objects.all().filter(is_avilable=True)
    return render(request, 'index.html',context={
        "products": products
    })
    