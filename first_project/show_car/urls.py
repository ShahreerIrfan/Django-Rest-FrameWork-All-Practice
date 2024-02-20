from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path("list/", views.car_list_view,name="list"),
    path('<int:pk>', views.car_details_view,name="car_details_view"),
    path('showroom/', views.Showroom_view.as_view(),name="showroom"),
    path('showroom/<int:pk>', views.ShowRoomDetailsView.as_view(),name="showroom"),
    path('review/', views.Review_view.as_view(),name="review"),
    path('review/<int:pk>', views.ReviewtDetail.as_view(),name="review-Details"),
    path('space/',views.CarSpecificationListView.as_view(),name='space'),
    path('space/<int:pk>',views.CarSpecificationDetailsView.as_view(),name='car-details')
]
