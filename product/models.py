from django.db import models
from category.models import CategoryModel
from django.urls import reverse
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
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)
    
    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)


variation_category_choice=(
    ('color','color'),
    ('size','size'),
    
)


class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category=models.CharField(max_length=100,choices=variation_category_choice)
    variation_value=models.CharField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    
    objects=VariationManager()
    
    def __unicode__(self):
        return self.product
    
