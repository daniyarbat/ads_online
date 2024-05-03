from django.urls import include, path
from rest_framework import routers

from .apps import SalesConfig
from .views import AdViewSet, AdListAPIView

app_name = SalesConfig.name

router = routers.DefaultRouter()
router.register(r'ads', AdViewSet, basename='объявления')


urlpatterns = [
    path('ads/me/', AdListAPIView.as_view(), name='мои объявления')
] + router.urls
