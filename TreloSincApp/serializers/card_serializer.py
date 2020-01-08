"""card serializer"""
from rest_framework.serializers import ModelSerializer

from TreloSincApp.models.card import Card


class CardSerializer(ModelSerializer):
    """Card serializer"""

    # pylint: disable=too-few-public-methods
    class Meta:
        """meta class"""
        model = Card
        fields = ['id', 'board', 'name', 'pos', 'shortUrl']
