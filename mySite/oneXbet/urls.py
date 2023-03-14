# from django.cont/rib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('leagues', football, name="football"),
    path('leagues/<slug:slug>/', league, name="league"),
    path('leagues/<slug:slug>/game/<slug:gameSlug>', game, name="game"),
    path('contact', ContactFormView.as_view(), name='contact'),
    # path('leagues/<slug:slug>/<slug:club>', league, name="club"),
    path('betting', BettingPage.as_view(), name="bet"),
]
