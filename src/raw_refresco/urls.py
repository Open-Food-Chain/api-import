from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('raw/refresco', views.RawRefrescoView)
router.register('raw/refresco/integrity', views.RawRefrescoIntegrityView)

urlpatterns = [
    path('', include(router.urls)),
    path('raw/refresco/new/', views.BatchView.as_view({'get': 'require_integrity'}))
]
