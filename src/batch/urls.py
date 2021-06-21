from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('import/batch', views.BatchView)
router.register('import/batch-integrity', views.BatchIntegrityView)
router.register('import/batch-tstx', views.TimestampTransactionView)

urlpatterns = [
    path('', include(router.urls)),
    path('import/batch/new/', views.BatchView.as_view({'get': 'require_integrity'}))
]
