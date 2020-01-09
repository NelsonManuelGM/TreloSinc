"""module for save the board data"""
from TreloSincApp.models.board import Board
from TreloSincApp.services.core import CoreService


# pylint: disable=too-few-public-methods
class SaveBoard(CoreService):
    """Class to save board data"""

    @staticmethod
    def execute(data: list) -> None:
        """
        Save a board
        :param data: list
        :return: None
        """
        for item in data:
            board_obj = Board()
            board_obj.fill(item)
            board_obj.save()
