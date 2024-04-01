from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to='categories')


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='product_related')
    price = models.IntegerField()
    product_description = models.TextField()


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image_related')
    image = models.ImageField(upload_to='product')