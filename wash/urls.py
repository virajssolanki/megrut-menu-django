from django.urls import path
from . import views


urlpatterns = [
    path('', views.wash, name='wash'),
] 