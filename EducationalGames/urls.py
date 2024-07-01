"""
URL configuration for EducationalGames project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Games import views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('registration/', users_views.registration),
    path('login/', users_views.login_page),
    path('logout/', users_views.logout_page),
    path('Games/', views.game_list),
    path('Games/SpeedScore/', views.speed_score),
    path('Games/Tic-tac-toe/', views.tic_tac_toe),
    path('Games/Tic-tac-toe/close/', views.close_img),
    path('Games/Tic-tac-toe/circle/', views.circle_img),
    path('Account/', users_views.account_information),
    path('Games/SpeedScore/ajax', views.speed),
    path('Groups/', users_views.create_group_page),
]
