from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from django.conf import settings
from core import views, urls

urlpatterns = [
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('organigramas/', include('organigramas.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)

