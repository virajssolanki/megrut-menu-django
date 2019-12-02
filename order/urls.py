from django.urls import path
from . import views


urlpatterns = [
    path('', views.order_home, name='order_home'),
    path('support/', views.support, name='support'),
    path('numbers/', views.numbers, name='numbers'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback_join/', views.feedback_join, name='feedback_join'),
    path('feedback_res/', views.feedback_res, name='feedback_res'),
] 