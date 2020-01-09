"""Module to manage Trello Synchronisation"""
import inject
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from TreloSincApp.services.connection_service import TrelloConnection


class TrelloSincView(APIView):
    """View for get data from trello.com"""

    @inject.autoparams()
    def get(self, request, trello_connection: TrelloConnection):
        """
        override get method
        :param trello_connection: TrelloConnection
        :param request:
        :return:
        """
        trello_connection.sync_board()

        trello_connection.sync_card()

        return Response(data={'Synchronisation': 'DONE!'},
                        status=status.HTTP_200_OK)
