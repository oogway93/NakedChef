from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('menu.urls')),
    path('users/', include('users.urls')),
]
