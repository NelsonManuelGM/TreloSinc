"""Module to manage Trello Synchronisation"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from TreloSincApp.services.connect import TrelloConection


class TrelloSincView(APIView):
    """
    View for get data from trello.com

    """
    def get(self, request):
        """
        override get method
        :param request:
        :return:
        """
        request_data = TrelloConection.get_board()
        return Response(data=request_data,status=status.HTTP_200_OK)
