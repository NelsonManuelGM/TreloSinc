"""module for save the board data"""
import inject

from TreloSincApp.models.board import Board
from TreloSincApp.services.board.get_board_service import ListBoard
from TreloSincApp.services.core import CoreService


# pylint: disable=too-few-public-methods
class SaveBoard(CoreService):
    """Class to save board data"""

    @staticmethod
    @inject.autoparams()
    def execute(data: list, srv_list_board: ListBoard) -> None:
        """
        Save a board
        :param srv_list_board: ListBoard
        :param data: list
        :return: None
        """
        boards = srv_list_board.execute()
        for item in data:
            if boards.filter(id=item['id']):
                continue
            board_obj = Board()
            board_obj.fill(item)
            board_obj.save()
