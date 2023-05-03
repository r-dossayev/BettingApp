# from django.cont/rib import admin
from django.urls import path

from .views import *
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('', index, name="home"),
    path('leagues', football, name="football"),
    path('leagues/<slug:slug>/', league, name="league"),
    path('leagues/<slug:slug>/games/', games, name="games"),
    path('leagues/<slug:slug>/games/<slug:gameSlug>', game, name="game"),
    path('contact/', cache_page(120)(ContactFormView.as_view()), name='contact'),
    path('profile', profileView, name='profile'),
    # path('leagues/<slug:slug>/<slug:club>', league, name="club"),
    path('betting', BettingPage.as_view(), name="bet"),

]
