"""module for save the card data"""
from TreloSincApp.models.card import Card
from TreloSincApp.services.core import CoreService


# pylint: disable=too-few-public-methods
class SaveCard(CoreService):
    """Class to save card data"""

    @staticmethod
    def execute(data: list, **kwargs) -> None:
        """Save a card"""
        board_obj = kwargs['board']
        for item in data:
            card_obj = Card()
            card_obj.fill(item)
            setattr(card_obj, 'board', board_obj)
            card_obj.save()
