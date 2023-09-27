from rest_framework.authtoken import views
from .views import MenuModelViewSet, OrderModelViewSet, SectionModelViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = 'api'
router = DefaultRouter()
router.register(r'menu', MenuModelViewSet)
router.register(r'orders', OrderModelViewSet)
router.register(r'section', SectionModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("auth/auth-token", views.obtain_auth_token),
]