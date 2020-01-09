"""TrelloSincApp url module"""

from django.urls import path

from TreloSincApp.views.board_view import BoardView
from TreloSincApp.views.card_view import CardView
from TreloSincApp.views.trello_sinc_view import TrelloSincView

# pylint: disable=invalid-name
urlpatterns = [
    path('trello_sinc', TrelloSincView.as_view(), name='trello_sync'),
    path('boards', BoardView.as_view(), name='boards'),
    path('cards', CardView.as_view(), name='cards'),
]
