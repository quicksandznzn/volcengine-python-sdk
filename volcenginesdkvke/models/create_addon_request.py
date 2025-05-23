# coding: utf-8

"""
    vke

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateAddonRequest(object):
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
        'client_token': 'str',
        'cluster_id': 'str',
        'config': 'str',
        'deploy_mode': 'str',
        'deploy_node_type': 'str',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'cluster_id': 'ClusterId',
        'config': 'Config',
        'deploy_mode': 'DeployMode',
        'deploy_node_type': 'DeployNodeType',
        'name': 'Name',
        'version': 'Version'
    }

    def __init__(self, client_token=None, cluster_id=None, config=None, deploy_mode=None, deploy_node_type=None, name=None, version=None, _configuration=None):  # noqa: E501
        """CreateAddonRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._cluster_id = None
        self._config = None
        self._deploy_mode = None
        self._deploy_node_type = None
        self._name = None
        self._version = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        self.cluster_id = cluster_id
        if config is not None:
            self.config = config
        if deploy_mode is not None:
            self.deploy_mode = deploy_mode
        if deploy_node_type is not None:
            self.deploy_node_type = deploy_node_type
        self.name = name
        if version is not None:
            self.version = version

    @property
    def client_token(self):
        """Gets the client_token of this CreateAddonRequest.  # noqa: E501


        :return: The client_token of this CreateAddonRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateAddonRequest.


        :param client_token: The client_token of this CreateAddonRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateAddonRequest.  # noqa: E501


        :return: The cluster_id of this CreateAddonRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateAddonRequest.


        :param cluster_id: The cluster_id of this CreateAddonRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cluster_id is None:
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def config(self):
        """Gets the config of this CreateAddonRequest.  # noqa: E501


        :return: The config of this CreateAddonRequest.  # noqa: E501
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this CreateAddonRequest.


        :param config: The config of this CreateAddonRequest.  # noqa: E501
        :type: str
        """

        self._config = config

    @property
    def deploy_mode(self):
        """Gets the deploy_mode of this CreateAddonRequest.  # noqa: E501


        :return: The deploy_mode of this CreateAddonRequest.  # noqa: E501
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        """Sets the deploy_mode of this CreateAddonRequest.


        :param deploy_mode: The deploy_mode of this CreateAddonRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Managed", "Unmanaged"]  # noqa: E501
        if (self._configuration.client_side_validation and
                deploy_mode not in allowed_values):
            raise ValueError(
                "Invalid value for `deploy_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(deploy_mode, allowed_values)
            )

        self._deploy_mode = deploy_mode

    @property
    def deploy_node_type(self):
        """Gets the deploy_node_type of this CreateAddonRequest.  # noqa: E501


        :return: The deploy_node_type of this CreateAddonRequest.  # noqa: E501
        :rtype: str
        """
        return self._deploy_node_type

    @deploy_node_type.setter
    def deploy_node_type(self, deploy_node_type):
        """Sets the deploy_node_type of this CreateAddonRequest.


        :param deploy_node_type: The deploy_node_type of this CreateAddonRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Node", "VirtualNode", "EdgeNode"]  # noqa: E501
        if (self._configuration.client_side_validation and
                deploy_node_type not in allowed_values):
            raise ValueError(
                "Invalid value for `deploy_node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deploy_node_type, allowed_values)
            )

        self._deploy_node_type = deploy_node_type

    @property
    def name(self):
        """Gets the name of this CreateAddonRequest.  # noqa: E501


        :return: The name of this CreateAddonRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAddonRequest.


        :param name: The name of this CreateAddonRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this CreateAddonRequest.  # noqa: E501


        :return: The version of this CreateAddonRequest.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateAddonRequest.


        :param version: The version of this CreateAddonRequest.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(CreateAddonRequest, dict):
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
        if not isinstance(other, CreateAddonRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAddonRequest):
            return True

        return self.to_dict() != other.to_dict()
