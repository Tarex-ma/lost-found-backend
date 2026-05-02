from rest_framework import generics 
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import LostItem, FoundItem, MatchHistory
from .serializers import LostItemSerializer, FoundItemSerializer
from .models import ClaimRequest
from .serializers import ClaimRequestSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .utils import find_matches, send_match_notification
from .serializers import MatchHistorySerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_auth(request):
    return Response({"message": "You are authenticated"})

class LostItemListCreateView(generics.ListCreateAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class LostItemDetailView(generics.RetrieveAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class FoundItemListCreateView(generics.ListCreateAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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

        # Only admin can approve
        if request.user.role != 'admin':
            return Response({"error": "Not authorized"}, status=403)

        if claim.status != 'pending':
            return Response({"error": "Already processed"}, status=400)

        # Update claim
        claim.status = 'approved'
        claim.save()

        # Update related items
        lost_item = claim.lost_item
        found_item = claim.found_item

        lost_item.status = 'resolved'
        found_item.status = 'returned'

        lost_item.save()
        found_item.save()

        return Response({"message": "Claim approved successfully"})
    

class RejectClaimView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        claim = get_object_or_404(ClaimRequest, pk=pk)

        if request.user.role != 'admin':
            return Response({"error": "Not authorized"}, status=403)

        if claim.status != 'pending':
            return Response({"error": "Already processed"}, status=400)

        claim.status = 'rejected'
        claim.save()
        

        return Response({"message": "Claim rejected"})
    
class FoundItemMatchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        found_item = get_object_or_404(FoundItem, pk=pk)

        matches = find_matches(found_item)

        # 🔥 Send notifications
        for lost_item in matches:
            MatchHistory.objects.get_or_create(
              lost_item=lost_item,
              found_item=found_item,
              defaults={"confidence_score": 0.8}
       )
        if lost_item.user.email:
            send_match_notification(
                lost_item.user.email,
                lost_item,
                found_item
            )

        serializer = LostItemSerializer(matches, many=True)
        return Response(serializer.data)
    
class MatchHistoryListView(generics.ListAPIView):
    queryset = MatchHistory.objects.all()
    serializer_class = MatchHistorySerializer
    permission_classes = [IsAuthenticated]