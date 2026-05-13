from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from ..models.item import FoundItem
from core.tasks import process_matches


class FoundItemMatchView(APIView):
    def get(self, request, pk):
        found_item = get_object_or_404(FoundItem, pk=pk)

        # 🚀 FIRE AND FORGET
        process_matches.delay(found_item.id)

        return Response({
            "message": "Match processing started in background"
        })