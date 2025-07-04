# coding: utf-8

"""
    Engine api

    Engine APIs  # noqa: E501

    OpenAPI spec version: 1.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ObjectIndirectProperties(object):
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
        'channel_id': 'int',
        'app_id': 'int',
        'frame_id': 'int',
        'time_stamp': 'int',
        'zone_id': 'int',
        'object_id': 'int',
        'track_id': 'int',
        'line_id': 'int',
        'point_id': 'int',
        'extra': 'str'
    }

    attribute_map = {
        'channel_id': 'channelId',
        'app_id': 'appId',
        'frame_id': 'frameId',
        'time_stamp': 'timeStamp',
        'zone_id': 'zoneId',
        'object_id': 'objectId',
        'track_id': 'trackId',
        'line_id': 'lineId',
        'point_id': 'pointId',
        'extra': 'extra'
    }

    def __init__(self, channel_id=None, app_id=None, frame_id=None, time_stamp=None, zone_id=-1, object_id=-1, track_id=-1, line_id=-1, point_id=-1, extra=None):  # noqa: E501
        """ObjectIndirectProperties - a model defined in Swagger"""  # noqa: E501
        self._channel_id = None
        self._app_id = None
        self._frame_id = None
        self._time_stamp = None
        self._zone_id = None
        self._object_id = None
        self._track_id = None
        self._line_id = None
        self._point_id = None
        self._extra = None
        self.discriminator = None
        if channel_id is not None:
            self.channel_id = channel_id
        if app_id is not None:
            self.app_id = app_id
        if frame_id is not None:
            self.frame_id = frame_id
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if zone_id is not None:
            self.zone_id = zone_id
        if object_id is not None:
            self.object_id = object_id
        if track_id is not None:
            self.track_id = track_id
        if line_id is not None:
            self.line_id = line_id
        if point_id is not None:
            self.point_id = point_id
        if extra is not None:
            self.extra = extra

    @property
    def channel_id(self):
        """Gets the channel_id of this ObjectIndirectProperties.  # noqa: E501


        :return: The channel_id of this ObjectIndirectProperties.  # noqa: E501
        :rtype: int
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this ObjectIndirectProperties.


        :param channel_id: The channel_id of this ObjectIndirectProperties.  # noqa: E501
        :type: int
        """

        self._channel_id = channel_id

    @property
    def app_id(self):
        """Gets the app_id of this ObjectIndirectProperties.  # noqa: E501


        :return: The app_id of this ObjectIndirectProperties.  # noqa: E501
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ObjectIndirectProperties.


        :param app_id: The app_id of this ObjectIndirectProperties.  # noqa: E501
        :type: int
        """

        self._app_id = app_id

    @property
    def frame_id(self):
        """Gets the frame_id of this ObjectIndirectProperties.  # noqa: E501


        :return: The frame_id of this ObjectIndirectProperties.  # noqa: E501
        :rtype: int
        """
        return self._frame_id

    @frame_id.setter
    def frame_id(self, frame_id):
        """Sets the frame_id of this ObjectIndirectProperties.


        :param frame_id: The frame_id of this ObjectIndirectProperties.  # noqa: E501
        :type: int
        """

        self._frame_id = frame_id

    @property
    def time_stamp(self):
        """Gets the time_stamp of this ObjectIndirectProperties.  # noqa: E501


        :return: The time_stamp of this ObjectIndirectProperties.  # noqa: E501
        :rtype: int
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this ObjectIndirectProperties.


        :param time_stamp: The time_stamp of this ObjectIndirectProperties.  # noqa: E501
        :type: int
        """

        self._time_stamp = time_stamp

    @property
    def zone_id(self):
        """Gets the zone_id of this ObjectIndirectProperties.  # noqa: E501


        :return: The zone_id of this ObjectIndirectProperties.  # noqa: E501
        :rtype: int
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ObjectIndirectProperties.


        :param zone_id: The zone_id of this ObjectIndirectProperties.  # noqa: E501
        :type: int
        """

        self._zone_id = zone_id

    @property
    def object_id(self):
        """Gets the object_id of this ObjectIndirectProperties.  # noqa: E501


        :return: The object_id of this ObjectIndirectProperties.  # noqa: E501
        :rtype: int
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this ObjectIndirectProperties.


        :param object_id: The object_id of this ObjectIndirectProperties.  # noqa: E501
        :type: int
        """

        self._object_id = object_id

    @property
    def track_id(self):
        """Gets the track_id of this ObjectIndirectProperties.  # noqa: E501


        :return: The track_id of this ObjectIndirectProperties.  # noqa: E501
        :rtype: int
        """
        return self._track_id

    @track_id.setter
    def track_id(self, track_id):
        """Sets the track_id of this ObjectIndirectProperties.


        :param track_id: The track_id of this ObjectIndirectProperties.  # noqa: E501
        :type: int
        """

        self._track_id = track_id

    @property
    def line_id(self):
        """Gets the line_id of this ObjectIndirectProperties.  # noqa: E501


        :return: The line_id of this ObjectIndirectProperties.  # noqa: E501
        :rtype: int
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this ObjectIndirectProperties.


        :param line_id: The line_id of this ObjectIndirectProperties.  # noqa: E501
        :type: int
        """

        self._line_id = line_id

    @property
    def point_id(self):
        """Gets the point_id of this ObjectIndirectProperties.  # noqa: E501


        :return: The point_id of this ObjectIndirectProperties.  # noqa: E501
        :rtype: int
        """
        return self._point_id

    @point_id.setter
    def point_id(self, point_id):
        """Sets the point_id of this ObjectIndirectProperties.


        :param point_id: The point_id of this ObjectIndirectProperties.  # noqa: E501
        :type: int
        """

        self._point_id = point_id

    @property
    def extra(self):
        """Gets the extra of this ObjectIndirectProperties.  # noqa: E501


        :return: The extra of this ObjectIndirectProperties.  # noqa: E501
        :rtype: str
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this ObjectIndirectProperties.


        :param extra: The extra of this ObjectIndirectProperties.  # noqa: E501
        :type: str
        """

        self._extra = extra

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
        if issubclass(ObjectIndirectProperties, dict):
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
        if not isinstance(other, ObjectIndirectProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
