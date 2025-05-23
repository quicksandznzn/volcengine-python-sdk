# coding: utf-8

"""
    vod20250101

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ConvertVisionForGetExecutionOutput(object):
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
        'content': 'str',
        'duration': 'float',
        'model': 'ConvertModelForGetExecutionOutput',
        'snapshots_number': 'int'
    }

    attribute_map = {
        'content': 'Content',
        'duration': 'Duration',
        'model': 'Model',
        'snapshots_number': 'SnapshotsNumber'
    }

    def __init__(self, content=None, duration=None, model=None, snapshots_number=None, _configuration=None):  # noqa: E501
        """ConvertVisionForGetExecutionOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._content = None
        self._duration = None
        self._model = None
        self._snapshots_number = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if duration is not None:
            self.duration = duration
        if model is not None:
            self.model = model
        if snapshots_number is not None:
            self.snapshots_number = snapshots_number

    @property
    def content(self):
        """Gets the content of this ConvertVisionForGetExecutionOutput.  # noqa: E501


        :return: The content of this ConvertVisionForGetExecutionOutput.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ConvertVisionForGetExecutionOutput.


        :param content: The content of this ConvertVisionForGetExecutionOutput.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def duration(self):
        """Gets the duration of this ConvertVisionForGetExecutionOutput.  # noqa: E501


        :return: The duration of this ConvertVisionForGetExecutionOutput.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ConvertVisionForGetExecutionOutput.


        :param duration: The duration of this ConvertVisionForGetExecutionOutput.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def model(self):
        """Gets the model of this ConvertVisionForGetExecutionOutput.  # noqa: E501


        :return: The model of this ConvertVisionForGetExecutionOutput.  # noqa: E501
        :rtype: ConvertModelForGetExecutionOutput
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ConvertVisionForGetExecutionOutput.


        :param model: The model of this ConvertVisionForGetExecutionOutput.  # noqa: E501
        :type: ConvertModelForGetExecutionOutput
        """

        self._model = model

    @property
    def snapshots_number(self):
        """Gets the snapshots_number of this ConvertVisionForGetExecutionOutput.  # noqa: E501


        :return: The snapshots_number of this ConvertVisionForGetExecutionOutput.  # noqa: E501
        :rtype: int
        """
        return self._snapshots_number

    @snapshots_number.setter
    def snapshots_number(self, snapshots_number):
        """Sets the snapshots_number of this ConvertVisionForGetExecutionOutput.


        :param snapshots_number: The snapshots_number of this ConvertVisionForGetExecutionOutput.  # noqa: E501
        :type: int
        """

        self._snapshots_number = snapshots_number

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
        if issubclass(ConvertVisionForGetExecutionOutput, dict):
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
        if not isinstance(other, ConvertVisionForGetExecutionOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConvertVisionForGetExecutionOutput):
            return True

        return self.to_dict() != other.to_dict()
