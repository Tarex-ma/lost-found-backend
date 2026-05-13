from ..models.item import LostItem, FoundItem
from rest_framework import serializers

class LostItemSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = LostItem
        fields = [
            'id',
            'title',
            'description',
            'category',
            'location',
            'date_lost',
            'image',
            'status',
            'created_at',
            'user',
            'user_email'
        ]
        read_only_fields = ['user', 'status', 'created_at']

class FoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundItem
        fields = '__all__'
        read_only_fields = ['user', 'status', 'created_at']     