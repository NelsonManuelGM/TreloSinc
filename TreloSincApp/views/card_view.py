"""Module to manage Cards"""
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from TreloSincApp.models.card import Card
from TreloSincApp.serializers.card_serializer import CardSerializer


class CardView(ListAPIView):
    """
    View for manage cards model
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list(self, request, *args, **kwargs):
        """
        Return a list of cards or a card if there is
        a board_id in query_params

        e.g: .../cards?board_id=5e15454878cd062c1acdb8a8

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        board_id = request.query_params['board_id'] \
            if 'board_id' in request.query_params else ''
        data = self.get_queryset()
        if board_id:
            data = data.filter(board_id=board_id)

        serializer = self.get_serializer(data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
