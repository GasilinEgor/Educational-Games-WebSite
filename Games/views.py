import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html', {})


def game_list(request):
    return render(request, 'Games/gameList.html', {})


def speed_score(request):
    context = {'task': "Реши как можно больше задач!"}
    return render(request, 'Games/speedScore.html', context)


@csrf_exempt
def speed(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        new_value = data.get('value')
        print(new_value)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
