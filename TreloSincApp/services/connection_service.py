"""module manage the connection with trello"""
import inject
import requests
from django.conf import settings

from TreloSincApp.services.card.save_card_service import SaveCard
from TreloSincApp.services.core import CoreService
from TreloSincApp.services.board.get_board_service import ListBoard
from TreloSincApp.services.board.save_board_service import SaveBoard


# pylint: disable=too-few-public-methods
class TrelloConnection(CoreService):
    """Class to manage the connection with trello.com"""

    @staticmethod
    @inject.autoparams()
    def sync_board(save_board_srv: SaveBoard) -> None:
        """
        get boards from trello.com
        :param save_board_srv: SaveBoard
        :return: None
        """
        board_path = settings.TRELLO_URL + '1/members/me/boards'
        params = {
            'fields': 'name,url',
            'key': settings.API_KEY,
            'token': settings.TOKEN
        }

        connection = requests.get(board_path, params=params)
        board_data = connection.json()
        save_board_srv.execute(board_data)

    @staticmethod
    @inject.autoparams()
    def sync_card(list_board_srv: ListBoard, save_card_srv: SaveCard) -> None:
        """
        get boards from trello.com
        :param save_card_srv: SaveCard
        :param list_board_srv: ListBoard
        :return: None
        """
        params = {
            'fields': 'name,pos,shortUrl',
            'key': settings.API_KEY,
            'token': settings.TOKEN
        }

        board_list = list_board_srv.execute()

        for board in board_list:
            card_per_board_path = settings.TRELLO_URL + \
                                  f'1/boards/{board.id}/cards/'
            connection = requests.get(card_per_board_path, params=params)
            data = connection.json()
            save_card_srv.execute(data, board=board)

