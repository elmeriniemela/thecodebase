from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Game

# Create your views here.

def home(request):
    context = {
        'games': Game.objects.all(),
    }
    return render(request, 'games/home.html', context)

def games(request, game_name):
    try:
        game = Game.objects.get(url=game_name)
    except Game.DoesNotExist:
        return HttpResponseNotFound("Game not found")
    files = game.javascriptfile_set.all()
    context = {
        'phaser_game': game,
        'phaser_game_files': files[1:],
        'conf_file': files[0],
    }
    return render(request, 'games/phaser-game.html', context)

