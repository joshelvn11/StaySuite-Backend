from django.urls import path
from accommodation import views

urlpatterns = [
    path('accommodation/list/', views.AccommodationList.as_view()),
    path('accommodation/detail/<str:accom_slug>/', views.AccommodationDetail.as_view())
]
