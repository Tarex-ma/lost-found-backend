from rest_framework import serializers 
from .models import MatchHistory, User
from .models import LostItem, FoundItem
from .models import ClaimRequest

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
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

class ClaimRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimRequest
        fields = '__all__'
        read_only_fields = ['user', 'status', 'created_at']

    def validate(self, data):
        lost_item = data['lost_item']
        found_item = data['found_item']

        # Prevent claiming resolved items
        if lost_item.status == 'resolved':
            raise serializers.ValidationError("This lost item is already resolved.")

        if found_item.status == 'returned':
            raise serializers.ValidationError("This found item is already returned.")

        return data

class MatchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchHistory
        fields = '__all__'