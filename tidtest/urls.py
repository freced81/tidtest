from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('tid_rapport.urls', namespace='tid_rapport')),
    path('admin/', admin.site.urls, name='admin')
]
