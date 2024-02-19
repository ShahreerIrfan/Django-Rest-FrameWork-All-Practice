from django.shortcuts import render
from. import models
from .api_file.serializers import CarSerializer,ShowRoomSerializer,ReviewSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins,generics
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,DjangoModelPermissions
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
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
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
class ShowRoomDetailsView(APIView):
    def get(self,request,pk):
        try:
            showroom = models.ShowRoom.objects.get(pk=pk)
        except models.ShowRoom.DoesNotExist:
            return Response({'error':'showroom not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = ShowRoomSerializer(showroom)
        return Response(serializer.data)
        
    def put(self,request,pk):
        showroom = models.ShowRoom.objects.get(pk=pk)
        serializer = ShowRoomSerializer(showroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        showroom = models.ShowRoom.objects.get(pk=pk)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Review_view(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = models.Review.objects.all()
    # Shudu matro stuff user edit delete korte parbe
    serializer_class = ReviewSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

class ReviewtDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = models.Review.objects.all()
    serializer_class = ReviewSerializer
    

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


            

        


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
