from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from catalog import views


router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='catalog')

urlpatterns = [
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('',
         RedirectView.as_view(url='/admin/', permanent=False)),
    path('admin/',
         admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include('rest_framework.urls'))
]
