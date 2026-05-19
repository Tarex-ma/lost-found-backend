from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.models.comment import Comment
from core.serializers.comment_serializer import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    queryset = Comment.objects.all().order_by(
        "-created_at"
    )

    def get_queryset(self):

        queryset = Comment.objects.all()

        item_id = self.request.query_params.get(
            "item"
        )

        if item_id:
            queryset = queryset.filter(
                item=item_id
            )

        return queryset

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )

    # ✅ ONLY OWNER CAN DELETE
    def destroy(self, request, *args, **kwargs):

        comment = self.get_object()

        if comment.user != request.user:

            from rest_framework.response import Response
            from rest_framework import status

            return Response(
                {
                    "error":
                    "Not allowed"
                },
                status=status.HTTP_403_FORBIDDEN
            )

        return super().destroy(
            request,
            *args,
            **kwargs
        )