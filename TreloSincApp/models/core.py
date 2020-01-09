"""Core model to represent a Parent for all models"""
from django.db import models


class CoreModel(models.Model):
    """Parent class for all Models class"""

    created_at = models.DateTimeField('date created',
                                      auto_now_add=True,
                                      editable=False)
    updated_at = models.DateTimeField('date updated',
                                      auto_now=True,
                                      editable=False)

    fillables = []

    # pylint: disable=too-few-public-methods
    class Meta:
        """CoreModel class Meta"""
        abstract = True

    def get_fillables(self) -> []:
        """
        Return fillable fields
        :return: []
        """
        return self.fillables

    def fill(self, attributes: {}) -> None:
        """
        Set specified values on current instance
        :param attributes: Dict
        :return: None
        """
        for attr_name in attributes:
            fillables = self.get_fillables()
            if not fillables:
                raise NotImplementedError(
                    "There is not specified any field as fillable.")

            if attr_name in fillables:
                value = attributes[attr_name]
                setattr(self, attr_name, value)
