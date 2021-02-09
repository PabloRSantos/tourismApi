from django.conf import settings
from django.conf.urls.static import static
# get images while the development
from django.contrib import admin
from django.urls import path, include
from api.router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
