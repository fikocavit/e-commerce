from django.shortcuts import render,get_object_or_404
from product.models import Product
from category.models import CategoryModel
# Create your views here.

def store(request, category_slug=None):
    categories=None
    products= None
    
    if category_slug != None:
        categories=get_object_or_404(CategoryModel, slug=category_slug)
        products=Product.objects.filter(category=categories, is_avilable=True)
        product_count=products.count()
    else:
        products= Product.objects.all().filter(is_avilable=True)
        product_count=products.count()
    return render(request, 'store.html',context={
        'products': products,
        'product_count' : product_count
    })
def product_detail(request, category_slug, product_slug):
    try:
        single_product=Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product-detail.html',context={
        'single_product' : single_product
    })
    