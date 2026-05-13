from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Comment
from core.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    queryset = Comment.objects.all().order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)