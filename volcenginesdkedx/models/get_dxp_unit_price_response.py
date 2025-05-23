# coding: utf-8

"""
    edx

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetDXPUnitPriceResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'monthly_unit_price': 'float',
        'transmit_distance': 'str',
        'yearly_unit_price': 'float'
    }

    attribute_map = {
        'monthly_unit_price': 'MonthlyUnitPrice',
        'transmit_distance': 'TransmitDistance',
        'yearly_unit_price': 'YearlyUnitPrice'
    }

    def __init__(self, monthly_unit_price=None, transmit_distance=None, yearly_unit_price=None, _configuration=None):  # noqa: E501
        """GetDXPUnitPriceResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._monthly_unit_price = None
        self._transmit_distance = None
        self._yearly_unit_price = None
        self.discriminator = None

        if monthly_unit_price is not None:
            self.monthly_unit_price = monthly_unit_price
        if transmit_distance is not None:
            self.transmit_distance = transmit_distance
        if yearly_unit_price is not None:
            self.yearly_unit_price = yearly_unit_price

    @property
    def monthly_unit_price(self):
        """Gets the monthly_unit_price of this GetDXPUnitPriceResponse.  # noqa: E501


        :return: The monthly_unit_price of this GetDXPUnitPriceResponse.  # noqa: E501
        :rtype: float
        """
        return self._monthly_unit_price

    @monthly_unit_price.setter
    def monthly_unit_price(self, monthly_unit_price):
        """Sets the monthly_unit_price of this GetDXPUnitPriceResponse.


        :param monthly_unit_price: The monthly_unit_price of this GetDXPUnitPriceResponse.  # noqa: E501
        :type: float
        """

        self._monthly_unit_price = monthly_unit_price

    @property
    def transmit_distance(self):
        """Gets the transmit_distance of this GetDXPUnitPriceResponse.  # noqa: E501


        :return: The transmit_distance of this GetDXPUnitPriceResponse.  # noqa: E501
        :rtype: str
        """
        return self._transmit_distance

    @transmit_distance.setter
    def transmit_distance(self, transmit_distance):
        """Sets the transmit_distance of this GetDXPUnitPriceResponse.


        :param transmit_distance: The transmit_distance of this GetDXPUnitPriceResponse.  # noqa: E501
        :type: str
        """

        self._transmit_distance = transmit_distance

    @property
    def yearly_unit_price(self):
        """Gets the yearly_unit_price of this GetDXPUnitPriceResponse.  # noqa: E501


        :return: The yearly_unit_price of this GetDXPUnitPriceResponse.  # noqa: E501
        :rtype: float
        """
        return self._yearly_unit_price

    @yearly_unit_price.setter
    def yearly_unit_price(self, yearly_unit_price):
        """Sets the yearly_unit_price of this GetDXPUnitPriceResponse.


        :param yearly_unit_price: The yearly_unit_price of this GetDXPUnitPriceResponse.  # noqa: E501
        :type: float
        """

        self._yearly_unit_price = yearly_unit_price

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetDXPUnitPriceResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetDXPUnitPriceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetDXPUnitPriceResponse):
            return True

        return self.to_dict() != other.to_dict()
