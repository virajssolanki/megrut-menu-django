from django.urls import path
from . import views


urlpatterns = [
    path('', views.website, name='website'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
] 