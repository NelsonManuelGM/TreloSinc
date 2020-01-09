"""Module to test the de app"""
import inject
from django.urls import reverse
from rest_framework import status

from TreloSinc.inject import config_inject
from TreloSincApp.services.board.save_board_service import SaveBoard
from TreloSincApp.test import TestAPICase

# Enable autoinject function
inject.configure_once(config_inject)


class TestListBoard(TestAPICase):
    """TestCase Class"""

    @inject.autoparams()
    # pylint: disable=arguments-differ
    def setUp(self, create_board_srv: SaveBoard) -> None:
        """
        Preparing data for test
        :param create_board_srv: SaveBoard
        :return:
        """
        super().setUp()
        self.url_name = 'boards'
        self.boards_url = reverse(self.url_name)
        self.boards = [
            {
                "id": "23432425465545453454",
                "name": "Board 1",
                "url": "https://test.com/miboard1"
            },
            {
                "id": "345345435456656765",
                "name": "Board 2",
                "url": "https://test.com/miboard2"
            }
        ]
        create_board_srv.execute(self.boards)

    def test_list_board(self):
        """
        Test the list board feature

        >> Request url
        >> Check for status code
        >> Check for items quantity

        :return: None
        """
        response = self.client.get(self.boards_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data.__len__(), self.boards.__len__())
