from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, StorageUnit, Item
from .serializers import CategorySerializer, StorageUnitSerializer, ItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class StorageUnitViewSet(viewsets.ModelViewSet):
    queryset = StorageUnit.objects.all()
    serializer_class = StorageUnitSerializer
    permission_classes = [IsAuthenticated]

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Optionally filter items by user? Or show all?
        # Requirement says "Storage Management System" usually collaborative.
        # But let's filter by created_by if needed later. For now all items.
        return Item.objects.all()
