from rest_framework import serializers 
from ..models.match_history import MatchHistory

class MatchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchHistory
        fields = '__all__'
