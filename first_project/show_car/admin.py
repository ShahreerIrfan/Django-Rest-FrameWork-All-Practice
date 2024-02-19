from django.contrib import admin
from . models import carList,ShowRoom,Review,CarSpecification

# Register your models here.

class Car_listModelAdmin(admin.ModelAdmin):
    list_display = ['name']
class ShowRoomModelAdmin(admin.ModelAdmin):
    list_display=['name','location']
# class ReviewModelAdmin(admin.ModelAdmin):
#     list_display= ['ratings']

admin.site.register(carList,Car_listModelAdmin)
admin.site.register(ShowRoom,ShowRoomModelAdmin)
admin.site.register(Review)
admin.site.register(CarSpecification)