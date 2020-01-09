"""module for list the card data"""
from TreloSincApp.models.card import Card
from TreloSincApp.services.core import CoreService
from django.db.models import QuerySet


# pylint: disable=too-few-public-methods
class ListCard(CoreService):
    """Class to list board data"""

    @staticmethod
    def execute() -> QuerySet:
        """list a board"""

        return Card.objects.all()
