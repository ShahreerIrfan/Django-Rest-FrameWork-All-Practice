from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.show_car_list,name="list"),
    path('<int:pk>', views.car_details_view,name="car_details_view"),
]
