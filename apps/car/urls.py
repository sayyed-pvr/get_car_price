from django.urls import path, include
from . import views

app_name = 'car'
urlpatterns = [
    path('prices/', views.prices, name='prices'),
]