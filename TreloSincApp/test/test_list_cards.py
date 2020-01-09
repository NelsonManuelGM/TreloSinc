"""Module to test the de app"""
import inject
from django.urls import reverse
from rest_framework import status

from TreloSinc.inject import config_inject
from TreloSincApp.services.board.get_board_service import ListBoard
from TreloSincApp.services.board.save_board_service import SaveBoard
from TreloSincApp.services.card.get_card_service import ListCard
from TreloSincApp.services.card.save_card_service import SaveCard
from TreloSincApp.test import TestAPICase

# Enable autoinject function
inject.configure_once(config_inject)


class TestListCard(TestAPICase):
    """TestCase Class"""

    # pylint: disable=arguments-differ
    @inject.autoparams()
    def setUp(self, create_card_srv: SaveCard, create_board_srv: SaveBoard,
              get_board_srv: ListBoard) -> None:
        """
        Preparing data for test
        >> Create boards
        >> Create cards

        :param get_board_srv: ListBoard
        :param create_board_srv: SaveBoard
        :param create_card_srv: SaveCard
        :return:
        """
        super().setUp()
        self.url_name = 'cards'
        self.boards = [
            {
                "id": "5e154555234324555",
                "name": "Board 1",
                "url": "https://test.com/miboard1"
            },
            {
                "id": "3423432432324324443",
                "name": "Board 2",
                "url": "https://test.com/miboard2"
            }
        ]
        create_board_srv.execute(self.boards)

        self.cards = [
            {
                "id": "5e16048977b0ae18af60ed27",
                "board": '5e154555234324555',
                "name": "A3 - Work on Get Card",
                "pos": 262143,
                "shortUrl": "https://trello.com/c/SgPDRJi7"
            },
            {
                "id": "5e160491665ecc188267b71b",
                "board": '5e154555234324555',
                "name": "A4 - Dokerize the application",
                "pos": 327679,
                "shortUrl": "https://trello.com/c/sFDNsnKe"
            },
            {
                "id": "5e1533c828431e53ae814a70",
                "board": '3423432432324324443',
                "name": "Activity 2",
                "pos": 65539,
                "shortUrl": "https://trello.com/c/i4FGXH5j"
            },
            {
                "id": "5e1533c817381e40adca2053",
                "board": '3423432432324324443',
                "name": "Activity 3",
                "pos": 131075,
                "shortUrl": "https://trello.com/c/zY5x3Qgl"
            }
        ]

        boards_obj_list = get_board_srv.execute()

        for board in boards_obj_list:
            auxiliary_card_list = []
            for card in self.cards:
                if card['board'] == board.id:
                    card['board'] = board
                    auxiliary_card_list.append(card)
            create_card_srv.execute(auxiliary_card_list, board=board)

    def test_list_cards(self):
        """
        Test the list cards feature

        >> Request url
        >> Check for status code
        >> Check for items quantity

        :return: None
        """
        cards_url = reverse(self.url_name)

        response = self.client.get(cards_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data.__len__(), self.cards.__len__())

    @inject.autoparams()
    def test_get_card_by_board_id(self, get_board_srv: ListBoard,
                                  get_card_srv: ListCard) -> None:
        """
        Test the get cards bu board id feature

        >> Request url
        >> Check for status code
        >> Check for items quantity

        :return: None
        """
        board_list = get_board_srv.execute()

        for board in board_list:
            cards_url = reverse(self.url_name)

            response = self.client.get(cards_url,
                                       data={'board_id': board.id})

            self.assertEqual(response.status_code, status.HTTP_200_OK)

            cards_quantity = get_card_srv.execute(). \
                filter(board_id=board.id).count()
            self.assertEqual(response.data.__len__(), cards_quantity)
