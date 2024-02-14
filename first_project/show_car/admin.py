from django.contrib import admin
from . models import carList,ShowRoom

# Register your models here.

class Car_listModelAdmin(admin.ModelAdmin):
    list_display = ['name']
class ShowRoomModelAdmin(admin.ModelAdmin):
    list_display=['name','location']

admin.site.register(carList,Car_listModelAdmin)
admin.site.register(ShowRoom,ShowRoomModelAdmin)