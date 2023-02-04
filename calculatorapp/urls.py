from django.urls import path
from . import views

app_name = 'calculatorapp'

urlpatterns = [
    path('', views.calculate, name='calculate'),
]
