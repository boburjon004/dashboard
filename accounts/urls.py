from . import views
from django.urls import path


urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('customuser/', views.customuser),
]  