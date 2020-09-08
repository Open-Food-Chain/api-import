from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('batch', views.BatchView)
router.register('new', views.BatchNullIntegrity.as_view())
router.register('integrity', views.IntegrityView)

urlpatterns = [
    path('', include(router.urls))
]
