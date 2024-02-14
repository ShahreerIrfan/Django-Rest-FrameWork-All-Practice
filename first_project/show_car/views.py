from django.shortcuts import render
from. import models
from .api_file.serializers import CarSerializer,ShowRoomSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# from django.http import JsonResponse
# from django.http import HttpResponse
# import json

# # Create your views here.

# def show_car_list(request):
#     cars = models.carList.objects.all()
#     data = {
#         'cars': list(cars.values()),
#     }

#     # return JsonResponse(data)
#     data_json = json.dumps(data)
#     return HttpResponse(data_json,content_type = "application/json")

# def car_details_view(request,pk):
#     car = models.carList.objects.get(pk=pk)
#     data = {
#         'name':car.name,
#         'description':car.description,
#         'active': car.active
#     }
#     return JsonResponse(data)

class Showroom_view(APIView):
    def get(self, request):
        showroom = models.ShowRoom.objects.all()
        serializer = ShowRoomSerializer(showroom,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShowRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','POST'])
def car_list_view(request):
    if request.method == 'GET':
        cars = models.carList.objects.all()
        serializer = CarSerializer(cars,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def car_details_view(request,pk):
    if request.method == 'GET':
        try:
            car = models.carList.objects.get(pk=pk)
        except:
            return Response({'Error':'car not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    if request.method == 'PUT':
        car = models.carList.objects.get(pk=pk)
        serializer = CarSerializer(car,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        car = models.carList.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# .....