from django.shortcuts import render
from django.http import HttpResponseNotFound
# Create your views here.
from .models import Topic

def topics(request, topic_name):
    try:
        topic = Topic.objects.get(url=topic_name)
    except Topic.DoesNotExist:
        return HttpResponseNotFound("Topic not found")
    repos = topic.repos.all()
    return render(request, 'projects/topics.html', {'topic': topic, 'repos': repos, 'first': repos[0]})