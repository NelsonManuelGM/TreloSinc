"""Card class to represent a database table"""
from django.db import models

from TreloSincApp.models.board import Board
from TreloSincApp.models.core import CoreModel


class Card(CoreModel):
    """Card model class"""

    id = models.CharField('card id', primary_key=True, max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE,
                              related_name='board_related')
    name = models.CharField('card name', max_length=100, blank=True, null=True)
    pos = models.IntegerField('card pos', default=0)
    shortUrl = models.URLField('short url', blank=True, null=True)

    fillables = ['id', 'board', 'name', 'pos', 'shortUrl']

    # pylint: disable=too-few-public-methods
    class Meta:
        """meta class"""
        ordering = ['name']
