from django.urls import path
from . import views

app_name = "sheets"

urlpatterns = [
    path('', views.base, name='base'),
]