from . import views
from django.urls import path


urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customuser/', views.customuser),
]  