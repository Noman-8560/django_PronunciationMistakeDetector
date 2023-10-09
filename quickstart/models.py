from django.db import models
from django.contrib.auth.models import User


class Recording(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_data = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recording by {self.user.username}"