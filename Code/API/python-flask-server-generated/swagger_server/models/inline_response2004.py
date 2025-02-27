# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2004(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, message_id: int=None, content: str=None, timestamp: datetime=None):  # noqa: E501
        """InlineResponse2004 - a model defined in Swagger

        :param message_id: The message_id of this InlineResponse2004.  # noqa: E501
        :type message_id: int
        :param content: The content of this InlineResponse2004.  # noqa: E501
        :type content: str
        :param timestamp: The timestamp of this InlineResponse2004.  # noqa: E501
        :type timestamp: datetime
        """
        self.swagger_types = {
            'message_id': int,
            'content': str,
            'timestamp': datetime
        }

        self.attribute_map = {
            'message_id': 'message_id',
            'content': 'content',
            'timestamp': 'timestamp'
        }
        self._message_id = message_id
        self._content = content
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2004':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_4 of this InlineResponse2004.  # noqa: E501
        :rtype: InlineResponse2004
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message_id(self) -> int:
        """Gets the message_id of this InlineResponse2004.


        :return: The message_id of this InlineResponse2004.
        :rtype: int
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id: int):
        """Sets the message_id of this InlineResponse2004.


        :param message_id: The message_id of this InlineResponse2004.
        :type message_id: int
        """

        self._message_id = message_id

    @property
    def content(self) -> str:
        """Gets the content of this InlineResponse2004.


        :return: The content of this InlineResponse2004.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content: str):
        """Sets the content of this InlineResponse2004.


        :param content: The content of this InlineResponse2004.
        :type content: str
        """

        self._content = content

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this InlineResponse2004.


        :return: The timestamp of this InlineResponse2004.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this InlineResponse2004.


        :param timestamp: The timestamp of this InlineResponse2004.
        :type timestamp: datetime
        """

        self._timestamp = timestamp
