from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("Kategoriya", max_length=100)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return str(self.name)

class Brand(models.Model):
    name = models.CharField("Brend", max_length=100)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return str(self.name)        


class Color(models.Model):
    name = models.CharField("Tovar rangi", max_length=150)
    
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField("Brend", max_length=100)
    slug = models.SlugField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="brand_products")
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField("Necha foiz chegirma ?", default=0)
    added = models.DateTimeField(auto_now_add=True)
    top = models.BooleanField(default=False)
    description = models.TextField()
    views = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.name)

class ProductImages(models.Model):
    product = models.ForeignKey(Product,
        default=None,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='product_images')
    image = models.ImageField("Tovarning alohida rasmlari", 
        upload_to='product_images/',
        blank=True, null=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Tovarning rasmlari'  
        verbose_name_plural = 'Tovarning rasmlari'    

class Contact(models.Model):
    first_name = models.CharField(max_length=50)                      
    last_name = models.CharField(max_length=50)                      
    email = models.EmailField(max_length=50)                      
    phone = models.CharField(max_length=50)                      
    message = models.TextField()

    def __str__(self):
        return self.first_name                      