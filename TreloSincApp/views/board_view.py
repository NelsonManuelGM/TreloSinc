"""Module to manage Boards"""
from rest_framework.generics import ListAPIView

from TreloSincApp.models.board import Board
from TreloSincApp.serializers.board_serializer import BoardSerializer


class BoardView(ListAPIView):
    """
    View for manage Boards model
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
