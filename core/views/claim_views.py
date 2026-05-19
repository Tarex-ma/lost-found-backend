from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.models.claim import ClaimRequest

from core.serializers.claim_serializer import ClaimRequestSerializer


class ClaimListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = ClaimRequestSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return ClaimRequest.objects.filter(
            user=self.request.user
        ).order_by("-created_at")

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)