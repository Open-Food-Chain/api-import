from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('raw/refresco', views.RawRefrescoView)
router.register('raw/refresco-integrity', views.RawRefrescoIntegrityView)
router.register('raw/refresco-tstx', views.TimestampTransactionView)

urlpatterns = [
    path('', include(router.urls)),
    path('raw/refresco/new/', views.RawRefrescoView.as_view({'get': 'require_integrity'}))
]
