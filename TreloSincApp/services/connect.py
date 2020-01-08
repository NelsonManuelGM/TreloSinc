"""module manage the connection with trello"""

import requests

from TreloSinc.settings import API_KEY
from TreloSinc.settings import TOKEN
from TreloSinc.settings import TRELLO_URL


class TrelloConection:
    """Class to manage the connection with trello.com"""

    @staticmethod
    def get_board():
        """get boards from trello.com"""

        # TRELLO_BOARD_PATH = TRELLO_URL + \
        #                     f'1/boards/{1}?key={API_KEY}&token={TOKEN}'
        # TRELLO_BOARD_PATH = TRELLO_URL + \
        #                     f'1/boards/{1}'
        # PARAMS = {
        #     'limit': '2',
        #     'fields': 'name',
        #     'members': 'true',
        #     'member_fields': 'fullName',
        #     'key': API_KEY,
        #     'token': TOKEN
        # }

        # connetion = requests.get(TRELLO_BOARD_PATH, params=PARAMS)

        # https://api.trello.com/1/members/me/boards?fields=name,url&key={apiKey}&token={apiToken}
        BOARD_PATH = TRELLO_URL + '1/members/me/boards'

        PARAMS = {
            'fields': 'name,url',
            'key': API_KEY,
            'token': TOKEN
        }

        connetion = requests.get(BOARD_PATH, params=PARAMS)

        request_data = connetion.json()

        return request_data
