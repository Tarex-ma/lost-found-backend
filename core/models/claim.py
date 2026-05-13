from django.contrib.auth.models import AbstractUser  
from django.db import models  
from django.conf import settings

from core.models.item import FoundItem, LostItem

User = settings.AUTH_USER_MODEL
 
class ClaimRequest(models.Model):
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='claims')

    lost_item = models.ForeignKey(LostItem, on_delete=models.CASCADE, related_name='claims')
    found_item = models.ForeignKey(FoundItem, on_delete=models.CASCADE, related_name='claims')

    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} → {self.lost_item}"
    class Meta:
        unique_together = ('user', 'lost_item', 'found_item')