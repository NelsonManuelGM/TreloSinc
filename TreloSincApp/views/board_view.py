"""Module to manage Boards"""
from rest_framework import status
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.response import Response

from TreloSincApp.models.board import Board
from TreloSincApp.serializers.board_serializer import BoardSerializer


# pylint: disable=too-many-ancestors
class BoardView(ListAPIView, DestroyAPIView):
    """
    View for manage Boards model
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def delete(self, request, *args, **kwargs):
        """
        Re-implementation of the delete method is for a testing goal,
        if there is neccesity to clean the DB.

        Cards has a CASCADE deletion asociated to the Boards,
        that's why we only need to delete de Boards

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.get_queryset().delete()

        return Response(data={'Clean DB': 'DONE!'},
                        status=status.HTTP_200_OK)
