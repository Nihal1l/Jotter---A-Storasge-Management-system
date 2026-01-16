from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, StorageUnitViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'storage-units', StorageUnitViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
