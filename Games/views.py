from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def game_list(request):
    return render(request, 'Games/gameList.html', {})


def speed_score(request):
    context = {'task': "Реши как можно больше задач!"}
    return render(request, 'Games/speedScore.html', context)
