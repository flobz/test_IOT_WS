# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from TimeSeriesIoT.models.base_model_ import Model
from TimeSeriesIoT import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, date=None, value=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI

        :param date: The date of this InlineResponse200.  # noqa: E501
        :type date: date
        :param value: The value of this InlineResponse200.  # noqa: E501
        :type value: float
        """
        self.openapi_types = {
            'date': date,
            'value': float
        }

        self.attribute_map = {
            'date': 'date',
            'value': 'value'
        }

        self._date = date
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def date(self):
        """Gets the date of this InlineResponse200.


        :return: The date of this InlineResponse200.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this InlineResponse200.


        :param date: The date of this InlineResponse200.
        :type date: date
        """

        self._date = date

    @property
    def value(self):
        """Gets the value of this InlineResponse200.

        sensor value  # noqa: E501

        :return: The value of this InlineResponse200.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InlineResponse200.

        sensor value  # noqa: E501

        :param value: The value of this InlineResponse200.
        :type value: float
        """

        self._value = value