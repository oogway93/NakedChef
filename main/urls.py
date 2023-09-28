from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  path('', include('menu.urls', namespace='menu')),
                  path('users/', include('users.urls', namespace='users')),
                  path('order/', include('orders.urls', namespace='orders')),
                  path('api/', include('api.urls', namespace='api')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
