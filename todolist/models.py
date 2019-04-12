from django.db import models


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    context = models.TextField()
    priority = models.IntegerField(default=0)
    expired = models.DateTimeField(null=True)

    class Meta:
        ordering = ('created',)
