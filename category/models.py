from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    img=models.ImageField(upload_to='category_images')
    description=models.TextField()
    
    
    class Meta:
        db_table='Category'
        verbose_name='Category'
        verbose_name_plural='Categories'
    
    
    def __str__(self):
        return self.category_name