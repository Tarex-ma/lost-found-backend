from django.contrib.auth.models import AbstractUser  
from django.db import models  
from django.conf import settings

User = settings.AUTH_USER_MODEL
    
class Notification(models.Model):

    NOTIFICATION_TYPES = (
        ("match", "Match"),
        ("claim", "Claim"),
        ("comment", "Comment"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES
    )

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.notification_type}"