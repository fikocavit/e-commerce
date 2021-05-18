from django.db import models
from category.models import CategoryModel
# Create your models here.



class Product(models.Model):
    product_name=models.CharField(max_length=50, unique=True)
    description=models.TextField(max_length=250)
    slug=models.SlugField(max_length=50, unique=True)
    images = models.ImageField(upload_to='products')
    price=models.IntegerField()
    is_avilable=models.BooleanField(default=True)
    stock=models.IntegerField()
    category = models.ForeignKey( CategoryModel , on_delete=models.CASCADE)
    created_date= models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.product_name