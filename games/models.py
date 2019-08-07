from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Score(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
