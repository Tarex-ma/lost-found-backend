from ..serializers import ClaimRequestSerializer
from ..models import ClaimRequest
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

class ClaimRequestCreateView(generics.CreateAPIView):
    queryset = ClaimRequest.objects.all()
    serializer_class = ClaimRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ApproveClaimView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        claim = get_object_or_404(ClaimRequest, pk=pk)

        if not request.user.is_staff:
            return Response({"error": "Not authorized"}, status=403)

        if claim.status != 'pending':
            return Response({"error": "Already processed"}, status=400)

        if not claim.lost_item or not claim.found_item:
            return Response({"error": "Invalid claim data"}, status=400)

        claim.status = 'approved'
        claim.save()

        claim.lost_item.status = 'resolved'
        claim.found_item.status = 'returned'

        claim.lost_item.save()
        claim.found_item.save()

        return Response({"message": "Claim approved successfully"})


class RejectClaimView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        claim = get_object_or_404(ClaimRequest, pk=pk)

        if not request.user.is_staff:
            return Response({"error": "Not authorized"}, status=403)

        if claim.status != 'pending':
            return Response({"error": "Already processed"}, status=400)

        claim.status = 'rejected'
        claim.save()

        return Response({"message": "Claim rejected"})