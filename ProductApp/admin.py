from django.contrib import admin

# Register your models here.
from ProductApp.models import ProductModel


@admin.register(ProductModel)
class ProductListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url',)