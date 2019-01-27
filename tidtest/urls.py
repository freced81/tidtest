from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profil', user_views.profiles, name='profil'),
    path('', include('tid_rapport.urls', namespace='tid_rapport')),
    path('admin/', admin.site.urls, name='admin')
]
