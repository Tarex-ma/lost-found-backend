from rest_framework import serializers
from core.models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):

    user_username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    class Meta:

        model = Comment

        fields = [
            "id",
            "item",
            "user",
            "user_username",
            "text",
            "parent",
            "created_at",
        ]

        read_only_fields = [
            "user"
        ]