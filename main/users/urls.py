from django.urls import path, include

from .views import profile, Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('profile/', profile, name='profile'),
]
