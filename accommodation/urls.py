from django.urls import path
from accommodation import views

urlpatterns = [
    path('accommodation/list/', views.AccommodationList.as_view())
]
