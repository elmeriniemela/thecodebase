
from .models import Topic


# Enabled in settings/TEMPLATES/OPTIONS/context_processors

def default_context(request):
    return {
        'background_image': 'main/images/cave_header.jpg',
        'page_title': 'The Codebase'
    }



def topics(request):
    return {
        'topics': Topic.objects.all(),
    }