from django.contrib import admin
from .models import Vehicles

# Register your models here.

class AdminDisplay(admin.ModelAdmin):
    list_display = [
        'vehicle', 'description', 'produce_year', 'price', 'horsepower', 'new_old','image']

    search_fields = ['vehicle', 'description', 'produce_year', 'price', 'horsepower', 'new_old']
    list_filter = ['vehicle', 'description', 'produce_year', 'price', 'horsepower', 'new_old']
    ordering = ['produce_year', 'price', 'horsepower', 'new_old']

admin.site.register(Vehicles, AdminDisplay)