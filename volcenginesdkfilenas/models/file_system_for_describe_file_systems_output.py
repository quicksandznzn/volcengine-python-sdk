# coding: utf-8

"""
    filenas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class FileSystemForDescribeFileSystemsOutput(object):
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
        'cache_performance': 'CachePerformanceForDescribeFileSystemsOutput',
        'capacity': 'CapacityForDescribeFileSystemsOutput',
        'charge_type': 'str',
        'create_time': 'str',
        'description': 'str',
        'file_system_id': 'str',
        'file_system_name': 'str',
        'file_system_type': 'str',
        'project_name': 'str',
        'protocol_type': 'str',
        'region_id': 'str',
        'snapshot_count': 'int',
        'status': 'str',
        'storage_type': 'str',
        'tags': 'list[TagForDescribeFileSystemsOutput]',
        'update_time': 'str',
        'version': 'str',
        'zone_id': 'str',
        'zone_name': 'str'
    }

    attribute_map = {
        'cache_performance': 'CachePerformance',
        'capacity': 'Capacity',
        'charge_type': 'ChargeType',
        'create_time': 'CreateTime',
        'description': 'Description',
        'file_system_id': 'FileSystemId',
        'file_system_name': 'FileSystemName',
        'file_system_type': 'FileSystemType',
        'project_name': 'ProjectName',
        'protocol_type': 'ProtocolType',
        'region_id': 'RegionId',
        'snapshot_count': 'SnapshotCount',
        'status': 'Status',
        'storage_type': 'StorageType',
        'tags': 'Tags',
        'update_time': 'UpdateTime',
        'version': 'Version',
        'zone_id': 'ZoneId',
        'zone_name': 'ZoneName'
    }

    def __init__(self, cache_performance=None, capacity=None, charge_type=None, create_time=None, description=None, file_system_id=None, file_system_name=None, file_system_type=None, project_name=None, protocol_type=None, region_id=None, snapshot_count=None, status=None, storage_type=None, tags=None, update_time=None, version=None, zone_id=None, zone_name=None, _configuration=None):  # noqa: E501
        """FileSystemForDescribeFileSystemsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cache_performance = None
        self._capacity = None
        self._charge_type = None
        self._create_time = None
        self._description = None
        self._file_system_id = None
        self._file_system_name = None
        self._file_system_type = None
        self._project_name = None
        self._protocol_type = None
        self._region_id = None
        self._snapshot_count = None
        self._status = None
        self._storage_type = None
        self._tags = None
        self._update_time = None
        self._version = None
        self._zone_id = None
        self._zone_name = None
        self.discriminator = None

        if cache_performance is not None:
            self.cache_performance = cache_performance
        if capacity is not None:
            self.capacity = capacity
        if charge_type is not None:
            self.charge_type = charge_type
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if file_system_id is not None:
            self.file_system_id = file_system_id
        if file_system_name is not None:
            self.file_system_name = file_system_name
        if file_system_type is not None:
            self.file_system_type = file_system_type
        if project_name is not None:
            self.project_name = project_name
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if region_id is not None:
            self.region_id = region_id
        if snapshot_count is not None:
            self.snapshot_count = snapshot_count
        if status is not None:
            self.status = status
        if storage_type is not None:
            self.storage_type = storage_type
        if tags is not None:
            self.tags = tags
        if update_time is not None:
            self.update_time = update_time
        if version is not None:
            self.version = version
        if zone_id is not None:
            self.zone_id = zone_id
        if zone_name is not None:
            self.zone_name = zone_name

    @property
    def cache_performance(self):
        """Gets the cache_performance of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The cache_performance of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: CachePerformanceForDescribeFileSystemsOutput
        """
        return self._cache_performance

    @cache_performance.setter
    def cache_performance(self, cache_performance):
        """Sets the cache_performance of this FileSystemForDescribeFileSystemsOutput.


        :param cache_performance: The cache_performance of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: CachePerformanceForDescribeFileSystemsOutput
        """

        self._cache_performance = cache_performance

    @property
    def capacity(self):
        """Gets the capacity of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The capacity of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: CapacityForDescribeFileSystemsOutput
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this FileSystemForDescribeFileSystemsOutput.


        :param capacity: The capacity of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: CapacityForDescribeFileSystemsOutput
        """

        self._capacity = capacity

    @property
    def charge_type(self):
        """Gets the charge_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The charge_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this FileSystemForDescribeFileSystemsOutput.


        :param charge_type: The charge_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def create_time(self):
        """Gets the create_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The create_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this FileSystemForDescribeFileSystemsOutput.


        :param create_time: The create_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The description of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FileSystemForDescribeFileSystemsOutput.


        :param description: The description of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file_system_id(self):
        """Gets the file_system_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The file_system_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """Sets the file_system_id of this FileSystemForDescribeFileSystemsOutput.


        :param file_system_id: The file_system_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._file_system_id = file_system_id

    @property
    def file_system_name(self):
        """Gets the file_system_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The file_system_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._file_system_name

    @file_system_name.setter
    def file_system_name(self, file_system_name):
        """Sets the file_system_name of this FileSystemForDescribeFileSystemsOutput.


        :param file_system_name: The file_system_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._file_system_name = file_system_name

    @property
    def file_system_type(self):
        """Gets the file_system_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The file_system_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._file_system_type

    @file_system_type.setter
    def file_system_type(self, file_system_type):
        """Sets the file_system_type of this FileSystemForDescribeFileSystemsOutput.


        :param file_system_type: The file_system_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._file_system_type = file_system_type

    @property
    def project_name(self):
        """Gets the project_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The project_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this FileSystemForDescribeFileSystemsOutput.


        :param project_name: The project_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def protocol_type(self):
        """Gets the protocol_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The protocol_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this FileSystemForDescribeFileSystemsOutput.


        :param protocol_type: The protocol_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._protocol_type = protocol_type

    @property
    def region_id(self):
        """Gets the region_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The region_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this FileSystemForDescribeFileSystemsOutput.


        :param region_id: The region_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def snapshot_count(self):
        """Gets the snapshot_count of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The snapshot_count of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_count

    @snapshot_count.setter
    def snapshot_count(self, snapshot_count):
        """Sets the snapshot_count of this FileSystemForDescribeFileSystemsOutput.


        :param snapshot_count: The snapshot_count of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: int
        """

        self._snapshot_count = snapshot_count

    @property
    def status(self):
        """Gets the status of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The status of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FileSystemForDescribeFileSystemsOutput.


        :param status: The status of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def storage_type(self):
        """Gets the storage_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The storage_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this FileSystemForDescribeFileSystemsOutput.


        :param storage_type: The storage_type of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._storage_type = storage_type

    @property
    def tags(self):
        """Gets the tags of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The tags of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: list[TagForDescribeFileSystemsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FileSystemForDescribeFileSystemsOutput.


        :param tags: The tags of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: list[TagForDescribeFileSystemsOutput]
        """

        self._tags = tags

    @property
    def update_time(self):
        """Gets the update_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The update_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this FileSystemForDescribeFileSystemsOutput.


        :param update_time: The update_time of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def version(self):
        """Gets the version of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The version of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FileSystemForDescribeFileSystemsOutput.


        :param version: The version of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def zone_id(self):
        """Gets the zone_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The zone_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this FileSystemForDescribeFileSystemsOutput.


        :param zone_id: The zone_id of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

    @property
    def zone_name(self):
        """Gets the zone_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501


        :return: The zone_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this FileSystemForDescribeFileSystemsOutput.


        :param zone_name: The zone_name of this FileSystemForDescribeFileSystemsOutput.  # noqa: E501
        :type: str
        """

        self._zone_name = zone_name

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
        if issubclass(FileSystemForDescribeFileSystemsOutput, dict):
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
        if not isinstance(other, FileSystemForDescribeFileSystemsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileSystemForDescribeFileSystemsOutput):
            return True

        return self.to_dict() != other.to_dict()
