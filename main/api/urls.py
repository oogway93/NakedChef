from rest_framework.authtoken import views
from .views import MenuModelViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = 'api'
router = DefaultRouter()
router.register(r'menu', MenuModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("auth/auth-token", views.obtain_auth_token),
]