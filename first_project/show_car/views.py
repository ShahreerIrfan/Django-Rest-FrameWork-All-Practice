from django.shortcuts import render
from. import models
from django.http import JsonResponse
from django.http import HttpResponse
import json

# Create your views here.

def show_car_list(request):
    cars = models.carList.objects.all()
    data = {
        'cars': list(cars.values()),
    }

    # return JsonResponse(data)
    data_json = json.dumps(data)
    return HttpResponse(data_json,content_type = "application/json")

def car_details_view(request,pk):
    car = models.carList.objects.get(pk=pk)
    data = {
        'name':car.name,
        'description':car.description,
        'active': car.active
    }
    return JsonResponse(data)