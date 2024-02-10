from django.contrib import admin
from . models import carList

# Register your models here.

class Car_listModelAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(carList,Car_listModelAdmin)