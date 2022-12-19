from django.db import models
from api.models import UserData

User = UserData


class Chat(models.Model):
    content = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
