"""module for save the card data"""
import inject

from TreloSincApp.models.card import Card
from TreloSincApp.services.card.get_card_service import ListCard
from TreloSincApp.services.core import CoreService


# pylint: disable=too-few-public-methods
class SaveCard(CoreService):
    """Class to save card data"""

    @staticmethod
    @inject.autoparams()
    def execute(data: list, srv_list_card: ListCard, **kwargs) -> None:
        """Save a card"""
        board_obj = kwargs['board']
        cards = srv_list_card.execute()
        for item in data:
            if cards.filter(id=item['id']):
                continue
            card_obj = Card()
            card_obj.fill(item)
            setattr(card_obj, 'board', board_obj)
            card_obj.save()
