from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopPage, name="Shop Page"),
]