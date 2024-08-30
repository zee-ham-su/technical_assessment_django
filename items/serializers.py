from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

def validate(self, data):
        if Item.objects.filter(name=data.get('name')).exists():
            raise serializers.ValidationError({"name": "Item with this name already exists."})
        return data