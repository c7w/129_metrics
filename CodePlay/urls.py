from . import views
from django.urls import path, include
from django.contrib.staticfiles import views as vv

urlpatterns = [
    path('start', views.start),
    path('result', views.result),
]
