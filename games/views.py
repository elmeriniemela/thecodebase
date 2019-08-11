

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import (
    HttpResponseNotFound,
    JsonResponse,
)

from .models import Game

# Create your views here.


def home(request):
    context = {
        'games': Game.objects.all(),
        'background_image': 'games/images/gaming_header.jpg',
        'page_title': 'Games',
    }
    return render(request, 'games/home.html', context)


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
        'background_image': 'games/images/gaming_header.jpg',
        'page_title': game.title,

    }
    return render(request, 'games/phaser-game.html', context)


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
