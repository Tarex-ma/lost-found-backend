from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class LostItem(models.Model):

    STATUS_CHOICES = (
        ('open', 'Open'),
        ('matched', 'Matched'),
        ('claimed', 'Claimed'),
        ('resolved', 'Resolved'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='lost_items'
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    date_lost = models.DateField()

    image = models.ImageField(
        upload_to='lost_items/',
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='open'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FoundItem(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='found_items'
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    category = models.CharField(max_length=100, default="unknown")

    location = models.CharField(max_length=255)

    image = models.ImageField(
        upload_to='found_items/',
        blank=True,
        null=True
    )

    is_claimed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title