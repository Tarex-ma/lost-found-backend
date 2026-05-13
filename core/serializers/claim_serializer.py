from rest_framework import serializers 
from ..models.claim import ClaimRequest

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