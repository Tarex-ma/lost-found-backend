from django.contrib.auth.models import AbstractUser  
from django.db import models  
from django.conf import settings

User = settings.AUTH_USER_MODEL
  
  
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lost_item = models.ForeignKey("LostItem", on_delete=models.CASCADE, null=True, blank=True)
    found_item = models.ForeignKey("FoundItem", on_delete=models.CASCADE, null=True, blank=True)

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:30]