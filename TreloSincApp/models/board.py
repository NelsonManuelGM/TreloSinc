"""Board class to represent a database table"""
from django.db import models

from TreloSincApp.models.core import CoreModel


class Board(CoreModel):
    """Board model class"""

    id = models.CharField('board id', primary_key=True, max_length=100)
    name = models.CharField('board name', max_length=30)
    url = models.URLField('board url')

    fillables = ['id', 'name', 'url']

    # pylint: disable=too-few-public-methods
    class Meta:
        """Metaclass"""
        ordering = ['name']
