# coding: utf-8

"""
    vepfs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class NodeTypeInfoForDescribeMountServiceNodeTypesOutput(object):
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
        'description_cn': 'str',
        'description_en': 'str',
        'node_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'description_cn': 'DescriptionCN',
        'description_en': 'DescriptionEN',
        'node_type': 'NodeType',
        'status': 'Status'
    }

    def __init__(self, description_cn=None, description_en=None, node_type=None, status=None, _configuration=None):  # noqa: E501
        """NodeTypeInfoForDescribeMountServiceNodeTypesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description_cn = None
        self._description_en = None
        self._node_type = None
        self._status = None
        self.discriminator = None

        if description_cn is not None:
            self.description_cn = description_cn
        if description_en is not None:
            self.description_en = description_en
        if node_type is not None:
            self.node_type = node_type
        if status is not None:
            self.status = status

    @property
    def description_cn(self):
        """Gets the description_cn of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.  # noqa: E501


        :return: The description_cn of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description_cn

    @description_cn.setter
    def description_cn(self, description_cn):
        """Sets the description_cn of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.


        :param description_cn: The description_cn of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.  # noqa: E501
        :type: str
        """

        self._description_cn = description_cn

    @property
    def description_en(self):
        """Gets the description_en of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.  # noqa: E501


        :return: The description_en of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        """Sets the description_en of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.


        :param description_en: The description_en of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.  # noqa: E501
        :type: str
        """

        self._description_en = description_en

    @property
    def node_type(self):
        """Gets the node_type of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.  # noqa: E501


        :return: The node_type of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.


        :param node_type: The node_type of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.  # noqa: E501
        :type: str
        """

        self._node_type = node_type

    @property
    def status(self):
        """Gets the status of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.  # noqa: E501


        :return: The status of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.


        :param status: The status of this NodeTypeInfoForDescribeMountServiceNodeTypesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(NodeTypeInfoForDescribeMountServiceNodeTypesOutput, dict):
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
        if not isinstance(other, NodeTypeInfoForDescribeMountServiceNodeTypesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeTypeInfoForDescribeMountServiceNodeTypesOutput):
            return True

        return self.to_dict() != other.to_dict()
