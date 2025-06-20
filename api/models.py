from django.db import models
from django.contrib.auth.models import User

class TelegramUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    chat_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
