from rest_framework import serializers
from .models import Category, StorageUnit, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class StorageUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageUnit
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ('created_by',)

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        return super().create(validated_data)
