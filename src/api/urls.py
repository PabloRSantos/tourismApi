from django.conf import settings
from django.conf.urls.static import static
# get images while the development
from django.contrib import admin
from django.urls import path, include
from api.router import router
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
