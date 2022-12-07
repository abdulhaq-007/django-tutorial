from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return str(self.name)

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.SlugField(max_length=100)
    country = models.CharField( max_length=50)

    def __str__(self):
        return str(self.name) 

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

