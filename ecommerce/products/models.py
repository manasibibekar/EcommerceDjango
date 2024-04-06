from django.db import models
from base.models import BaseModel
from django.utils.text import slugify


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to='categories')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class SizeVariant(BaseModel):
    size_name = models.CharField(max_length=10)
    size_price_delta = models.IntegerField(default=0)

    def __str__(self):
        return self.size_name


class ColorVariant(BaseModel):
    color_name = models.CharField(max_length=20)
    color_price_delta = models.IntegerField(default=0)

    def __str__(self):
        return self.color_name
    

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='product_related')
    price = models.IntegerField()
    product_description = models.TextField()
    color_variant = models.ManyToManyField(ColorVariant, blank=True)
    size_variant = models.ManyToManyField(SizeVariant, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name
    
    def get_product_price_by_size(self, size):
        return self.price + SizeVariant.objects.get(size_name=size).size_price_delta


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image_related')
    image = models.ImageField(upload_to='product')