from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Scarlett-home'),
    path('404/', views.dash, name='Scarlett-dash'),
    path('get-response/', views.get_response),
]
