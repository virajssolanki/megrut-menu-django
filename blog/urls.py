from django.urls import path
from . import views


urlpatterns = [
    path('', views.menulist, name='blog-home'),
    path('post/new/', views.add_menu, name='post-create'),
    path('post/<int:pk>/update', views.update_menu, name='post-update'),
    path('post/<int:pk>/delete', views.delete_menu, name='post-delete'),
    path('post/<int:pk>/activate', views.activate, name='activate'),
] 