import json

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm, LoginForm, CreateGroupForm
from .models import Player, Group
from datetime import date


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            user = authenticate(username=username, password=password)
            login(request, user)
            user.is_active = True
            new_user = Player.objects.create(username=username, name=name, surname=surname,
                                             registration_date=date.today())
            new_user.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            Username = form.data['username']
            Password = form.data['password']
            user = authenticate(request, username=Username, password=Password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('/')


def account_information(request):
    player = Player.objects.filter(username=request.user.username).get()
    max_points = 1000 + int(player.level) * 500
    context = {'player': player,
               'max_points': max_points}
    return render(request, 'account.html', context)

#  Функция отрисовки страницы создания группы
def create_group_page(request):
    context={}
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            group_info = {'name': form.data['name'],
                          'slogan': form.data['slogan'],
                          'description': form.data['description'],
                          }
            player = Player.objects.filter(username=request.user.username).get()
            create_group(player, group_info)
            return redirect('/')
    else:
        form = CreateGroupForm()
    context['form'] = form
    return render(request, 'Groups/create_group.html', context)

#  Функция обработки страницы списка групп
def group_list_page(request):
    group = Group.objects.all()
    context = {'group': group}
    return render(request, 'Groups/group_list.html', context)

def group_info_page(request, group_id):
    group = Group.objects.get(id=group_id)
    player = Player.objects.filter(username=request.user.username).get()
    context = {'group': group}
    if player.group is not None:
        if player.group.pk == group_id:
            context['flag'] = True
        else:
            context['flag'] = False
    else:
        context['flag'] = False
    return render(request, 'Groups/group_info.html', context)


def group_add_member(request, group_id):
    player = Player.objects.filter(username=request.user.username).get()
    group = Group.objects.get(id=group_id)
    add_member_to_group(player, group)
    return redirect('/Groups/' + str(group_id) + '/')


def group_delete_member(request, group_id):
    player = Player.objects.filter(username=request.user.username).get()
    group = Group.objects.get(id=group_id)
    flag = delete_member_from_group(player, group)
    if flag:
        return redirect('/Groups/')
    else:
        return redirect('/Groups/' + str(group_id) + '/')


def upgrade_points(username, points, k=1, game_level=1):
    player = Player.objects.filter(username=username).get()
    level = player.level
    current_points = points * k * game_level + int(player.points)
    max_points = 1000 + int(player.level) * 500
    if max_points <= current_points:
        level += 1
        current_points -= max_points
    player.level = level
    player.points = current_points
    player.save()

#  Функции работы с группами
#  Создание группы
def create_group(player: Player, group_info: dict):
    group = Group.objects.create(name=group_info['name'], slogan=group_info['slogan'],
                                 description=group_info['description'], members_count=1, lieder=player)
    group.save()
    player.group = group
    player.save()

#  добавление пользователя в группу
def add_member_to_group(player: Player, group: Group):
    if player.group is None:
        player.group = group
        group.members_count += 1
        player.save()
        group.save()
        return True
    else:
        return False

#  Удаление пользователя из группы
def delete_member_from_group(player: Player, group: Group):
    if player != group.lieder:
        group.members_count -= 1
        player.group = None
        player.save()
        group.save()
        return True
    elif group.members_count == 1:
        player.group = None
        delete_group(group)
        return True
    else:
        return False

#  удаление группы
def delete_group(group: Group):
    group.delete()
