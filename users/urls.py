from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import UserProfileView, Register

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
]
