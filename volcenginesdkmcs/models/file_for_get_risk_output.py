# coding: utf-8

"""
    mcs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class FileForGetRiskOutput(object):
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
        'create_time_nano': 'int',
        'md5': 'str',
        'modified_time_nano': 'int',
        'owner': 'OwnerForGetRiskOutput',
        'path': 'str',
        'sha1': 'str',
        'sha256': 'str',
        'size': 'int',
        'type': 'str'
    }

    attribute_map = {
        'create_time_nano': 'CreateTimeNano',
        'md5': 'Md5',
        'modified_time_nano': 'ModifiedTimeNano',
        'owner': 'Owner',
        'path': 'Path',
        'sha1': 'Sha1',
        'sha256': 'Sha256',
        'size': 'Size',
        'type': 'Type'
    }

    def __init__(self, create_time_nano=None, md5=None, modified_time_nano=None, owner=None, path=None, sha1=None, sha256=None, size=None, type=None, _configuration=None):  # noqa: E501
        """FileForGetRiskOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time_nano = None
        self._md5 = None
        self._modified_time_nano = None
        self._owner = None
        self._path = None
        self._sha1 = None
        self._sha256 = None
        self._size = None
        self._type = None
        self.discriminator = None

        if create_time_nano is not None:
            self.create_time_nano = create_time_nano
        if md5 is not None:
            self.md5 = md5
        if modified_time_nano is not None:
            self.modified_time_nano = modified_time_nano
        if owner is not None:
            self.owner = owner
        if path is not None:
            self.path = path
        if sha1 is not None:
            self.sha1 = sha1
        if sha256 is not None:
            self.sha256 = sha256
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type

    @property
    def create_time_nano(self):
        """Gets the create_time_nano of this FileForGetRiskOutput.  # noqa: E501


        :return: The create_time_nano of this FileForGetRiskOutput.  # noqa: E501
        :rtype: int
        """
        return self._create_time_nano

    @create_time_nano.setter
    def create_time_nano(self, create_time_nano):
        """Sets the create_time_nano of this FileForGetRiskOutput.


        :param create_time_nano: The create_time_nano of this FileForGetRiskOutput.  # noqa: E501
        :type: int
        """

        self._create_time_nano = create_time_nano

    @property
    def md5(self):
        """Gets the md5 of this FileForGetRiskOutput.  # noqa: E501


        :return: The md5 of this FileForGetRiskOutput.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this FileForGetRiskOutput.


        :param md5: The md5 of this FileForGetRiskOutput.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def modified_time_nano(self):
        """Gets the modified_time_nano of this FileForGetRiskOutput.  # noqa: E501


        :return: The modified_time_nano of this FileForGetRiskOutput.  # noqa: E501
        :rtype: int
        """
        return self._modified_time_nano

    @modified_time_nano.setter
    def modified_time_nano(self, modified_time_nano):
        """Sets the modified_time_nano of this FileForGetRiskOutput.


        :param modified_time_nano: The modified_time_nano of this FileForGetRiskOutput.  # noqa: E501
        :type: int
        """

        self._modified_time_nano = modified_time_nano

    @property
    def owner(self):
        """Gets the owner of this FileForGetRiskOutput.  # noqa: E501


        :return: The owner of this FileForGetRiskOutput.  # noqa: E501
        :rtype: OwnerForGetRiskOutput
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this FileForGetRiskOutput.


        :param owner: The owner of this FileForGetRiskOutput.  # noqa: E501
        :type: OwnerForGetRiskOutput
        """

        self._owner = owner

    @property
    def path(self):
        """Gets the path of this FileForGetRiskOutput.  # noqa: E501


        :return: The path of this FileForGetRiskOutput.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FileForGetRiskOutput.


        :param path: The path of this FileForGetRiskOutput.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def sha1(self):
        """Gets the sha1 of this FileForGetRiskOutput.  # noqa: E501


        :return: The sha1 of this FileForGetRiskOutput.  # noqa: E501
        :rtype: str
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this FileForGetRiskOutput.


        :param sha1: The sha1 of this FileForGetRiskOutput.  # noqa: E501
        :type: str
        """

        self._sha1 = sha1

    @property
    def sha256(self):
        """Gets the sha256 of this FileForGetRiskOutput.  # noqa: E501


        :return: The sha256 of this FileForGetRiskOutput.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this FileForGetRiskOutput.


        :param sha256: The sha256 of this FileForGetRiskOutput.  # noqa: E501
        :type: str
        """

        self._sha256 = sha256

    @property
    def size(self):
        """Gets the size of this FileForGetRiskOutput.  # noqa: E501


        :return: The size of this FileForGetRiskOutput.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileForGetRiskOutput.


        :param size: The size of this FileForGetRiskOutput.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def type(self):
        """Gets the type of this FileForGetRiskOutput.  # noqa: E501


        :return: The type of this FileForGetRiskOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileForGetRiskOutput.


        :param type: The type of this FileForGetRiskOutput.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(FileForGetRiskOutput, dict):
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
        if not isinstance(other, FileForGetRiskOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileForGetRiskOutput):
            return True

        return self.to_dict() != other.to_dict()
