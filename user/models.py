from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,null=True, blank=True, on_delete=models.SET_NULL)
    text=models.TextField()
    creation_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(null=True)

    def __str__(self):
        return self.text[:20]


