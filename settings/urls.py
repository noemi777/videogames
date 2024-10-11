"""
URL configuration for settings project.

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
from videogames.views import CreateGame, ReadGamesId, ReadListGames, UpdateGame, DeleteGame, DeleteGameAll

urlpatterns = [
    path('admin/', admin.site.urls),
    path('read/list/', ReadListGames.as_view(), name='Read List'), 
    path('create/', CreateGame.as_view(), name='Create videogame'), 
    path('read/<int:id>', ReadGamesId.as_view(), name='Read by id'),
    path('update/<int:id>', UpdateGame.as_view(), name= 'Update game'),
    path('delete/<int:id>', DeleteGame.as_view(), name='Delete videogame'),
    path('delete', DeleteGameAll.as_view(), name='Delete all videogames')

]
