# coding: utf-8

"""
    Engine api

    Engine APIs  # noqa: E501

    OpenAPI spec version: 1.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SourceEndPoint(object):
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
        'id': 'str',
        'user_id': 'str',
        'updated': 'datetime',
        'created': 'datetime',
        'etag': 'str',
        'links': 'Links',
        'name': 'str',
        'source_list': 'list[SourceEndPointSourceList]',
        'start_time_stamp': 'int',
        'end_time_stamp': 'int',
        'snaps': 'list[EvidenceConfig]',
        'clips': 'list[EvidenceConfig]',
        'schedule': 'list[list[ScheduleSource]]'
    }

    attribute_map = {
        'id': '_id',
        'user_id': 'userId',
        'updated': 'updated',
        'created': 'created',
        'etag': 'etag',
        'links': 'links',
        'name': 'name',
        'source_list': 'sourceList',
        'start_time_stamp': 'startTimeStamp',
        'end_time_stamp': 'endTimeStamp',
        'snaps': 'snaps',
        'clips': 'clips',
        'schedule': 'schedule'
    }

    def __init__(self, id=None, user_id=None, updated=None, created=None, etag=None, links=None, name=None, source_list=None, start_time_stamp=None, end_time_stamp=None, snaps=None, clips=None, schedule=None):  # noqa: E501
        """SourceEndPoint - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._user_id = None
        self._updated = None
        self._created = None
        self._etag = None
        self._links = None
        self._name = None
        self._source_list = None
        self._start_time_stamp = None
        self._end_time_stamp = None
        self._snaps = None
        self._clips = None
        self._schedule = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if etag is not None:
            self.etag = etag
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if source_list is not None:
            self.source_list = source_list
        if start_time_stamp is not None:
            self.start_time_stamp = start_time_stamp
        if end_time_stamp is not None:
            self.end_time_stamp = end_time_stamp
        if snaps is not None:
            self.snaps = snaps
        if clips is not None:
            self.clips = clips
        if schedule is not None:
            self.schedule = schedule

    @property
    def id(self):
        """Gets the id of this SourceEndPoint.  # noqa: E501


        :return: The id of this SourceEndPoint.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SourceEndPoint.


        :param id: The id of this SourceEndPoint.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this SourceEndPoint.  # noqa: E501


        :return: The user_id of this SourceEndPoint.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SourceEndPoint.


        :param user_id: The user_id of this SourceEndPoint.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def updated(self):
        """Gets the updated of this SourceEndPoint.  # noqa: E501


        :return: The updated of this SourceEndPoint.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this SourceEndPoint.


        :param updated: The updated of this SourceEndPoint.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this SourceEndPoint.  # noqa: E501


        :return: The created of this SourceEndPoint.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SourceEndPoint.


        :param created: The created of this SourceEndPoint.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def etag(self):
        """Gets the etag of this SourceEndPoint.  # noqa: E501


        :return: The etag of this SourceEndPoint.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this SourceEndPoint.


        :param etag: The etag of this SourceEndPoint.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def links(self):
        """Gets the links of this SourceEndPoint.  # noqa: E501


        :return: The links of this SourceEndPoint.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SourceEndPoint.


        :param links: The links of this SourceEndPoint.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this SourceEndPoint.  # noqa: E501

        Logical name of multiple video source URLS  # noqa: E501

        :return: The name of this SourceEndPoint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SourceEndPoint.

        Logical name of multiple video source URLS  # noqa: E501

        :param name: The name of this SourceEndPoint.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def source_list(self):
        """Gets the source_list of this SourceEndPoint.  # noqa: E501


        :return: The source_list of this SourceEndPoint.  # noqa: E501
        :rtype: list[SourceEndPointSourceList]
        """
        return self._source_list

    @source_list.setter
    def source_list(self, source_list):
        """Sets the source_list of this SourceEndPoint.


        :param source_list: The source_list of this SourceEndPoint.  # noqa: E501
        :type: list[SourceEndPointSourceList]
        """

        self._source_list = source_list

    @property
    def start_time_stamp(self):
        """Gets the start_time_stamp of this SourceEndPoint.  # noqa: E501

        Process the source types FROM this unix timestamp  # noqa: E501

        :return: The start_time_stamp of this SourceEndPoint.  # noqa: E501
        :rtype: int
        """
        return self._start_time_stamp

    @start_time_stamp.setter
    def start_time_stamp(self, start_time_stamp):
        """Sets the start_time_stamp of this SourceEndPoint.

        Process the source types FROM this unix timestamp  # noqa: E501

        :param start_time_stamp: The start_time_stamp of this SourceEndPoint.  # noqa: E501
        :type: int
        """

        self._start_time_stamp = start_time_stamp

    @property
    def end_time_stamp(self):
        """Gets the end_time_stamp of this SourceEndPoint.  # noqa: E501

        Process the source types TILL this unix timestamp  # noqa: E501

        :return: The end_time_stamp of this SourceEndPoint.  # noqa: E501
        :rtype: int
        """
        return self._end_time_stamp

    @end_time_stamp.setter
    def end_time_stamp(self, end_time_stamp):
        """Sets the end_time_stamp of this SourceEndPoint.

        Process the source types TILL this unix timestamp  # noqa: E501

        :param end_time_stamp: The end_time_stamp of this SourceEndPoint.  # noqa: E501
        :type: int
        """

        self._end_time_stamp = end_time_stamp

    @property
    def snaps(self):
        """Gets the snaps of this SourceEndPoint.  # noqa: E501


        :return: The snaps of this SourceEndPoint.  # noqa: E501
        :rtype: list[EvidenceConfig]
        """
        return self._snaps

    @snaps.setter
    def snaps(self, snaps):
        """Sets the snaps of this SourceEndPoint.


        :param snaps: The snaps of this SourceEndPoint.  # noqa: E501
        :type: list[EvidenceConfig]
        """

        self._snaps = snaps

    @property
    def clips(self):
        """Gets the clips of this SourceEndPoint.  # noqa: E501


        :return: The clips of this SourceEndPoint.  # noqa: E501
        :rtype: list[EvidenceConfig]
        """
        return self._clips

    @clips.setter
    def clips(self, clips):
        """Sets the clips of this SourceEndPoint.


        :param clips: The clips of this SourceEndPoint.  # noqa: E501
        :type: list[EvidenceConfig]
        """

        self._clips = clips

    @property
    def schedule(self):
        """Gets the schedule of this SourceEndPoint.  # noqa: E501


        :return: The schedule of this SourceEndPoint.  # noqa: E501
        :rtype: list[list[ScheduleSource]]
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this SourceEndPoint.


        :param schedule: The schedule of this SourceEndPoint.  # noqa: E501
        :type: list[list[ScheduleSource]]
        """

        self._schedule = schedule

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
        if issubclass(SourceEndPoint, dict):
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
        if not isinstance(other, SourceEndPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
