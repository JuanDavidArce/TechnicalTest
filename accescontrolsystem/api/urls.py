# Rest framework
from rest_framework.routers import DefaultRouter

# Django
from django.conf.urls import include
from django.urls import path

# Views 
from api.views import ApiAccessControlViewSet


router = DefaultRouter()
router.register(r'api',ApiAccessControlViewSet,basename='api')

urlpatterns = [
    path('',include(router.urls)),
 
]