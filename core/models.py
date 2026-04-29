from django.contrib.auth.models import AbstractUser  
from django.db import models  
from django.conf import settings

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

class LostItem(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('matched', 'Matched'),
        ('claimed', 'Claimed'),
        ('resolved', 'Resolved'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lost_items')
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    date_lost = models.DateField()
    image = models.ImageField(upload_to='lost_items/', null=True, blank=True)
    email = models.EmailField(unique=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class FoundItem(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('matched', 'Matched'),
        ('returned', 'Returned'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='found_items')
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    date_found = models.DateField()
    image = models.ImageField(upload_to='found_items/', null=True, blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
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
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lost_item = models.ForeignKey(LostItem, on_delete=models.CASCADE, related_name='comments')

    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user}"