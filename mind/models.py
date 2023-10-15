from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    human = models.TextField()
    mind_bot = models.TextField()
    def __str__(self):
        return self.user.username
    

class Secret(models.Model):
    name = models.CharField(max_length=100)
    secret = models.TextField()
    def __str__(self):
        return self.name