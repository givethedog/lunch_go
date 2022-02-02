from django.urls import path
from . import views

app_name = 'lunch_go'

urlpatterns = [
    path('', views.index, name='index')
]