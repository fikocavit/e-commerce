# Generated by Django 3.1 on 2021-05-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210521_0929'),
        ('carts', '0002_auto_20210519_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='product.Variation'),
        ),
    ]