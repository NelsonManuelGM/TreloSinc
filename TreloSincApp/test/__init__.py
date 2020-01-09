"""core test module"""
import inject
from rest_framework.test import APITestCase, APIClient
from django.test import TestCase

from TreloSinc.inject import config_inject


class TestAPICase(APITestCase, TestCase):
    """Base Test case for all api test application"""

    # pylint: disable=too-few-public-methods
    class Meta:
        """NotificationService class Meta"""
        abstract = True

    def setUp(self) -> None:
        super().setUp()
        inject.configure_once(config_inject)
        self.client = APIClient()
