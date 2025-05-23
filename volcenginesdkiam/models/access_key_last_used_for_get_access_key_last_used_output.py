# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AccessKeyLastUsedForGetAccessKeyLastUsedOutput(object):
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
        'region': 'str',
        'request_time': 'str',
        'service': 'str'
    }

    attribute_map = {
        'region': 'Region',
        'request_time': 'RequestTime',
        'service': 'Service'
    }

    def __init__(self, region=None, request_time=None, service=None, _configuration=None):  # noqa: E501
        """AccessKeyLastUsedForGetAccessKeyLastUsedOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._region = None
        self._request_time = None
        self._service = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if request_time is not None:
            self.request_time = request_time
        if service is not None:
            self.service = service

    @property
    def region(self):
        """Gets the region of this AccessKeyLastUsedForGetAccessKeyLastUsedOutput.  # noqa: E501


        :return: The region of this AccessKeyLastUsedForGetAccessKeyLastUsedOutput.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AccessKeyLastUsedForGetAccessKeyLastUsedOutput.


        :param region: The region of this AccessKeyLastUsedForGetAccessKeyLastUsedOutput.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def request_time(self):
        """Gets the request_time of this AccessKeyLastUsedForGetAccessKeyLastUsedOutput.  # noqa: E501


        :return: The request_time of this AccessKeyLastUsedForGetAccessKeyLastUsedOutput.  # noqa: E501
        :rtype: str
        """
        return self._request_time

    @request_time.setter
    def request_time(self, request_time):
        """Sets the request_time of this AccessKeyLastUsedForGetAccessKeyLastUsedOutput.


        :param request_time: The request_time of this AccessKeyLastUsedForGetAccessKeyLastUsedOutput.  # noqa: E501
        :type: str
        """

        self._request_time = request_time

    @property
    def service(self):
        """Gets the service of this AccessKeyLastUsedForGetAccessKeyLastUsedOutput.  # noqa: E501


        :return: The service of this AccessKeyLastUsedForGetAccessKeyLastUsedOutput.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this AccessKeyLastUsedForGetAccessKeyLastUsedOutput.


        :param service: The service of this AccessKeyLastUsedForGetAccessKeyLastUsedOutput.  # noqa: E501
        :type: str
        """

        self._service = service

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
        if issubclass(AccessKeyLastUsedForGetAccessKeyLastUsedOutput, dict):
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
        if not isinstance(other, AccessKeyLastUsedForGetAccessKeyLastUsedOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessKeyLastUsedForGetAccessKeyLastUsedOutput):
            return True

        return self.to_dict() != other.to_dict()
