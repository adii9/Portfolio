
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.Home, name='Home'),
]
