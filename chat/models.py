from django.db import models


class Chat(models.Model):
    content = models.CharField(max_length=10000)
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey
