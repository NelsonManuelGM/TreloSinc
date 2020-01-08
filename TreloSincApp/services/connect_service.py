"""module manage the connection with trello"""
import inject
import requests
from django.conf import settings

from TreloSincApp.services.core import CoreService
from TreloSincApp.services.get_board_service import ListBoard
from TreloSincApp.services.save_board_service import SaveBoard

# pylint: disable=too-few-public-methods
class TrelloConnection(CoreService):
    """Class to manage the connection with trello.com"""

    @staticmethod
    @inject.autoparams()
    def get_board(save_board_srv: SaveBoard, list_board_srv: ListBoard):
        """
        get boards from trello.com
        :param save_board_srv: SaveBoard
        :param list_board_srv: ListBoard
        :return:
        """

        # TRELLO_BOARD_PATH = TRELLO_URL + \
        #                     f'1/boards/{1}?key={API_KEY}&token={TOKEN}'
        # TRELLO_BOARD_PATH = TRELLO_URL + \
        #                     f'1/boards/{1}'
        # params = {
        #     'limit': '2',
        #     'fields': 'name',
        #     'members': 'true',
        #     'member_fields': 'fullName',
        #     'key': API_KEY,
        #     'token': TOKEN
        # }

        # connetion = requests.get(TRELLO_BOARD_PATH, params=params)

        # https://api.trello.com/1/members/me/boards?fields=name,url&key={apiKey}&token={apiToken}
        board_path = settings.TRELLO_URL + '1/members/me/boards'

        params = {
            'fields': 'name,url',
            'key': settings.API_KEY,
            'token': settings.TOKEN
        }

        connetion = requests.get(board_path, params=params)
        board_data = connetion.json()
        save_board_srv.execute(board_data)

        # board_list = list_board_srv.execute()

        return board_data
