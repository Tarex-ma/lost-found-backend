from rest_framework import generics, permissions
from ..models import LostItem, FoundItem
from core.serializers import LostItemSerializer, FoundItemSerializer
# @method_decorator(ratelimit(key='user', rate='5/m', method='POST'), name='dispatch') # type: ignore
# class LostItemListCreateView(Generic.ListCreateAPIView):


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