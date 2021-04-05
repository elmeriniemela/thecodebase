
import os

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.http import HttpResponseNotFound, JsonResponse
from django.conf import settings

from .models import Topic
from .models import Game

# Create your views here.


def games_home(request):
    context = {
        'games': Game.objects.all(),
        'background_image': 'main/images/gaming_header.jpg',
        'page_title': 'Games',
    }
    return render(request, 'main/games.html', context)


@login_required
def play_game(request, game_name):
    try:
        game = Game.objects.get(url=game_name)
    except Game.DoesNotExist:
        return HttpResponseNotFound("Game not found")
    files = game.javascriptfile_set.all()
    context = {
        'phaser_game': game,
        'phaser_game_files': files[1:],
        'conf_file': files[0],
        'background_image': 'main/images/gaming_header.jpg',
        'page_title': game.title,

    }
    return render(request, 'main/phaser-game.html', context)


@login_required
def post_score(request, game_name):
    try:
        game = Game.objects.get(url=game_name)
    except Game.DoesNotExist:
        return HttpResponseNotFound("Game not found")
    game.score_set.create(
        user=request.user,
        score=request.POST['score'],
    )
    all_scores = game.score_set.all()
    data_list = []
    for score_obj in all_scores[:10]:
        data_list.append([
            score_obj.user.username.replace('ä', 'a').replace('ö', 'o'),
            score_obj.score,
            score_obj.time.strftime('%Y-%m-%d'),
        ])
    return JsonResponse(data_list, safe=False)




class myUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(myUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def about_me(request):
    context = {
        'background_image': 'main/images/glider_header.jpg',
        'page_title': 'About Me'

    }
    return render(request, 'main/about_me.html', context)

def my_server(request):
    context = {
        'background_image': 'main/images/programming_header.jpg',
        'page_title': 'My Server',
    }
    return render(request, 'main/my_server.html', context)

def download_cv(request):
    path = os.path.join(settings.BASE_DIR, 'main', 'media', 'cv_elmeri.pdf')
    return FileResponse(open(path, 'rb'), content_type='application/pdf')


def register(request):
    if request.method == 'POST':
        form = myUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main/home')
    else:
        form = myUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



def topics(request, topic_name):
    try:
        topic = Topic.objects.get(url=topic_name)
    except Topic.DoesNotExist:
        return HttpResponseNotFound("Topic not found")
    repos = topic.repos.all()
    context = {
        'topic': topic,
        'repos': repos,
        'first': repos[0],
        'background_image': 'main/images/programming_header.jpg',
        'page_title': 'Projects',
    }
    return render(request, 'main/projects.html', context)
