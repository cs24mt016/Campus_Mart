# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ListingsListingIdBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, title: str=None, description: str=None, price: float=None):  # noqa: E501
        """ListingsListingIdBody - a model defined in Swagger

        :param title: The title of this ListingsListingIdBody.  # noqa: E501
        :type title: str
        :param description: The description of this ListingsListingIdBody.  # noqa: E501
        :type description: str
        :param price: The price of this ListingsListingIdBody.  # noqa: E501
        :type price: float
        """
        self.swagger_types = {
            'title': str,
            'description': str,
            'price': float
        }

        self.attribute_map = {
            'title': 'title',
            'description': 'description',
            'price': 'price'
        }
        self._title = title
        self._description = description
        self._price = price

    @classmethod
    def from_dict(cls, dikt) -> 'ListingsListingIdBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The listings_listing_id_body of this ListingsListingIdBody.  # noqa: E501
        :rtype: ListingsListingIdBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self) -> str:
        """Gets the title of this ListingsListingIdBody.


        :return: The title of this ListingsListingIdBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this ListingsListingIdBody.


        :param title: The title of this ListingsListingIdBody.
        :type title: str
        """

        self._title = title

    @property
    def description(self) -> str:
        """Gets the description of this ListingsListingIdBody.


        :return: The description of this ListingsListingIdBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ListingsListingIdBody.


        :param description: The description of this ListingsListingIdBody.
        :type description: str
        """

        self._description = description

    @property
    def price(self) -> float:
        """Gets the price of this ListingsListingIdBody.


        :return: The price of this ListingsListingIdBody.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price: float):
        """Sets the price of this ListingsListingIdBody.


        :param price: The price of this ListingsListingIdBody.
        :type price: float
        """

        self._price = price
