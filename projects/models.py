
from django.db import models
from django.shortcuts import render

# Create your models here.



class Repo(models.Model):
    name = models.CharField(max_length=150)
    display_name = models.CharField(max_length=150)
    readme_html = models.TextField()
    sequence = models.IntegerField(default=100)
    update_date = models.DateTimeField(auto_now_add=True)
    no_update = models.BooleanField(default=False)

   

    class Meta:
        ordering = ('sequence', 'name',)
        constraints = [
            models.UniqueConstraint(fields=['name'], name="name-unique")
        ]



class Topic(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    image_url = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    repos = models.ManyToManyField(Repo)
    sequence = models.IntegerField(default=100)

    class Meta:
        ordering = ('sequence', 'title',)
        constraints = [
            models.UniqueConstraint(fields=['url'], name="url-unique")
        ]
