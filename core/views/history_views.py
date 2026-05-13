from core.serializers.match_history_serializer import MatchHistorySerializer

from ..models.match_history import MatchHistory
from rest_framework import generics, permissions
from ..serializers.match_history_serializer import  MatchHistorySerializer
from rest_framework.permissions import IsAuthenticated 
class MatchHistoryListView(generics.ListAPIView):
    serializer_class = MatchHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MatchHistory.objects.filter(
            lost_item__user=self.request.user
        )