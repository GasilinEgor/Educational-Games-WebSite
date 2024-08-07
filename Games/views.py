import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SpeedScoreRecords
from datetime import date
from users.views import upgrade_points


def index(request):
    return render(request, 'index.html', {})


def game_list(request):
    return render(request, 'Games/gameList.html', {})


def speed_score(request):
    try:
        records = SpeedScoreRecords.objects.order_by('-score')
    except:
        records = None
    context = {'task': "Реши как можно больше задач!",
               'records': records,
               }
    return render(request, 'Games/speedScore.html', context)

def tic_tac_toe(request):
    context = {'task': "Победи своего друга!"}
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
