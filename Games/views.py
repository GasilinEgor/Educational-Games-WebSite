import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SpeedScoreRecords
from datetime import date
from users.views import upgrade_points
from users.models import Player


def index(request):
    if request.user.pk is not None:
        player = Player.objects.get(username=request.user.username)
        context = {'user_id': player.pk}
    else:
        context = {}
    return render(request, 'index.html', context)


def game_list(request):
    player = Player.objects.get(username=request.user.username)
    context = {'user_id': player.pk}
    return render(request, 'Games/gameList.html', context)


def speed_score(request):
    try:
        records = SpeedScoreRecords.objects.order_by('-score')
    except:
        records = None
    context = {'task': "Реши как можно больше задач!",
               'records': records,
               }
    player = Player.objects.get(username=request.user.username)
    context['user_id'] = player.pk
    return render(request, 'Games/speedScore.html', context)

def tic_tac_toe(request):
    player = Player.objects.get(username=request.user.username)
    context = {'user_id': player.pk,
               'task': "Победи своего друга!"}
    return render(request, 'Games/tic.html', context)

def circle_img(request):
    return render(request, 'static/Educational-Games-WebSite/js/circle.png')
def close_img(request):
    return render(request, 'Games/Tic-tac-toe/close.png')
@csrf_exempt
def speed(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_value = data.get('value')
        level = data.get('game_level')
        upgrade_points(username=request.user.username, points=int(new_value), k=5, game_level=int(level))
        try:
            record = SpeedScoreRecords.objects.filter(username=request.user.username).first()
            if int(record.score) < int(new_value):
                SpeedScoreRecords.objects.filter(username=request.user.username).delete()
                new_record = SpeedScoreRecords(username=request.user.username, score=int(new_value), date=date.today())
                new_record.save()
        except:
            new_record = SpeedScoreRecords(username=request.user.username, score=int(new_value), date=date.today())
            new_record.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
