from django.urls import path
from sites import views

urlpatterns = [
    # path('sites/', views.ProfileList.as_view()),
    path('sites/<str:slug>/', views.SiteDetail.as_view()),
]
