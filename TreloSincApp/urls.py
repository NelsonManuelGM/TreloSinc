"""TrelloSincApp url module"""

from django.urls import path

from TreloSincApp.views.trello_sinc_view import TrelloSincView

# pylint: disable=invalid-name
urlpatterns = [
    path('trello_sinc', TrelloSincView.as_view(), name='trellosinc')
]