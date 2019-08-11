from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    image_url = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    sequence = models.IntegerField(default=100)

    class Meta:
        ordering = ('sequence', 'title',)
        constraints = [
            models.UniqueConstraint(fields=['url'], name="game-url-unique")
        ]

class JavaScriptFile(models.Model):
    path = models.CharField(max_length=200)
    sequence = models.IntegerField(default=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.path

    class Meta:
        ordering = ('sequence',)


class Score(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()

    class Meta:
        ordering = ('-score', '-time',)
