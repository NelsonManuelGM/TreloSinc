"""board serializer module"""
from rest_framework.serializers import ModelSerializer

from TreloSincApp.models.board import Board


class BoardSerializer(ModelSerializer):
    """Board serializer"""

    # pylint: disable=too-few-public-methods
    class Meta:
        """meta class"""
        model = Board
        fields = ['id', 'name', 'url']
