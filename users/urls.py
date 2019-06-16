from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add_new_mess@123/', user_views.register, name='register'),
    path('edit_profile/<username>/', user_views.edit_profile, name='edit_profile'),
    path('mess_profile/<username>/', user_views.mess_profile, name='mess_profile'),
    path('mymess/<username>/', user_views.mymess, name='mymess'),
    path('close_mess/<username>/', user_views.close_mess, name='close_mess'),
    path('open_mess/<username>/', user_views.open_mess, name='open_mess'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/home.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
] 

