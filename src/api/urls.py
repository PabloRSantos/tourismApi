from django.conf import settings
from django.conf.urls.static import static
# get images while the development
from django.contrib import admin
from django.urls import path, include
from api.router import router
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='0.1.0',
        description='API de pontos turisticos'
    ),
    public=False,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('docs', schema_view.with_ui('swagger', cache_timeout=0))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
