# from django.cont/rib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home")
]
