from django.urls import path
from . import views


urlpatterns = [
    path('', views.order_home, name='order_home'),
    path('numbers/', views.numbers, name='numbers'),
    path('feedback/', views.feedback, name='feedback'),
] 