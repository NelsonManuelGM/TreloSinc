"""module for list the board data"""
from TreloSincApp.models.board import Board
from TreloSincApp.services.core import CoreService
from django.db.models import QuerySet


# pylint: disable=too-few-public-methods
class ListBoard(CoreService):
    """Class to list board data"""

    @staticmethod
    def execute() -> QuerySet:
        """list a board"""

        return Board.objects.all()
