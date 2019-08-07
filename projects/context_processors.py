
from .models import Topic

def topics(request):
    return {
            'topics': Topic.objects.all(),
        }