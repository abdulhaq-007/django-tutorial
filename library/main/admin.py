from django.contrib import admin
from .models import Book, Category, Author

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    prepopulated_fields = {'slug': ('name',)}
       
admin.site.register(Author)      