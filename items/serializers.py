from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_name(self, value):
        """Ensure the name is unique and not empty."""
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty or just whitespace.")
        if Item.objects.filter(name=value).exists():
            raise serializers.ValidationError("An item with this name already exists.")
        return value