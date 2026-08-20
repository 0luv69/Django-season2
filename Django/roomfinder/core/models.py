from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    """Room Finder model"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available = models.BooleanField(default=True)



    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title