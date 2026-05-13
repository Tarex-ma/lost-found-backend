from rest_framework import serializers 
from ..models.comment import   Comment

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["user"]