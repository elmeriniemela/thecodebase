from django.shortcuts import render

# Create your views here.

def home(request):
    context = dict(
        name='elmeri'
    )
    return render(request, 'games/home.html', context)