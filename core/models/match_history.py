from django.contrib.auth.models import AbstractUser  
from django.db import models  
from django.conf import settings

from ..models.item import FoundItem, LostItem

User = settings.AUTH_USER_MODEL
    
class MatchHistory(models.Model):
    lost_item = models.ForeignKey(LostItem, on_delete=models.CASCADE)
    found_item = models.ForeignKey(FoundItem, on_delete=models.CASCADE)
    confidence_score = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)