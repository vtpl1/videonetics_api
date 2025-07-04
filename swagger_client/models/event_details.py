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

class EventDetails(object):
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
        'engine_task_id': 'str',
        'source_end_point_id': 'str',
        'start_time_stamp': 'int',
        'end_time_stamp': 'int',
        'zone_id': 'int',
        'confidence': 'float',
        'capture_time_in_video': 'int',
        'extras': 'list[Extra]'
    }

    attribute_map = {
        'engine_task_id': 'engineTaskId',
        'source_end_point_id': 'sourceEndPointId',
        'start_time_stamp': 'startTimeStamp',
        'end_time_stamp': 'endTimeStamp',
        'zone_id': 'zoneId',
        'confidence': 'confidence',
        'capture_time_in_video': 'captureTimeInVideo',
        'extras': 'extras'
    }

    def __init__(self, engine_task_id=None, source_end_point_id=None, start_time_stamp=None, end_time_stamp=None, zone_id=0, confidence=0, capture_time_in_video=None, extras=None):  # noqa: E501
        """EventDetails - a model defined in Swagger"""  # noqa: E501
        self._engine_task_id = None
        self._source_end_point_id = None
        self._start_time_stamp = None
        self._end_time_stamp = None
        self._zone_id = None
        self._confidence = None
        self._capture_time_in_video = None
        self._extras = None
        self.discriminator = None
        if engine_task_id is not None:
            self.engine_task_id = engine_task_id
        if source_end_point_id is not None:
            self.source_end_point_id = source_end_point_id
        if start_time_stamp is not None:
            self.start_time_stamp = start_time_stamp
        if end_time_stamp is not None:
            self.end_time_stamp = end_time_stamp
        if zone_id is not None:
            self.zone_id = zone_id
        if confidence is not None:
            self.confidence = confidence
        if capture_time_in_video is not None:
            self.capture_time_in_video = capture_time_in_video
        if extras is not None:
            self.extras = extras

    @property
    def engine_task_id(self):
        """Gets the engine_task_id of this EventDetails.  # noqa: E501

        _id of engineTasks #$ref: '#/components/schemas/engineTasks'  # noqa: E501

        :return: The engine_task_id of this EventDetails.  # noqa: E501
        :rtype: str
        """
        return self._engine_task_id

    @engine_task_id.setter
    def engine_task_id(self, engine_task_id):
        """Sets the engine_task_id of this EventDetails.

        _id of engineTasks #$ref: '#/components/schemas/engineTasks'  # noqa: E501

        :param engine_task_id: The engine_task_id of this EventDetails.  # noqa: E501
        :type: str
        """

        self._engine_task_id = engine_task_id

    @property
    def source_end_point_id(self):
        """Gets the source_end_point_id of this EventDetails.  # noqa: E501


        :return: The source_end_point_id of this EventDetails.  # noqa: E501
        :rtype: str
        """
        return self._source_end_point_id

    @source_end_point_id.setter
    def source_end_point_id(self, source_end_point_id):
        """Sets the source_end_point_id of this EventDetails.


        :param source_end_point_id: The source_end_point_id of this EventDetails.  # noqa: E501
        :type: str
        """

        self._source_end_point_id = source_end_point_id

    @property
    def start_time_stamp(self):
        """Gets the start_time_stamp of this EventDetails.  # noqa: E501

        Event start timestamp in Unix epoch milliseconds  # noqa: E501

        :return: The start_time_stamp of this EventDetails.  # noqa: E501
        :rtype: int
        """
        return self._start_time_stamp

    @start_time_stamp.setter
    def start_time_stamp(self, start_time_stamp):
        """Sets the start_time_stamp of this EventDetails.

        Event start timestamp in Unix epoch milliseconds  # noqa: E501

        :param start_time_stamp: The start_time_stamp of this EventDetails.  # noqa: E501
        :type: int
        """

        self._start_time_stamp = start_time_stamp

    @property
    def end_time_stamp(self):
        """Gets the end_time_stamp of this EventDetails.  # noqa: E501

        Event end timestamp in Unix epoch milliseconds  # noqa: E501

        :return: The end_time_stamp of this EventDetails.  # noqa: E501
        :rtype: int
        """
        return self._end_time_stamp

    @end_time_stamp.setter
    def end_time_stamp(self, end_time_stamp):
        """Sets the end_time_stamp of this EventDetails.

        Event end timestamp in Unix epoch milliseconds  # noqa: E501

        :param end_time_stamp: The end_time_stamp of this EventDetails.  # noqa: E501
        :type: int
        """

        self._end_time_stamp = end_time_stamp

    @property
    def zone_id(self):
        """Gets the zone_id of this EventDetails.  # noqa: E501

        the zoneId of the engineTask in zoneSetting, #$ref: '#/components/schemas/zone'  # noqa: E501

        :return: The zone_id of this EventDetails.  # noqa: E501
        :rtype: int
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this EventDetails.

        the zoneId of the engineTask in zoneSetting, #$ref: '#/components/schemas/zone'  # noqa: E501

        :param zone_id: The zone_id of this EventDetails.  # noqa: E501
        :type: int
        """

        self._zone_id = zone_id

    @property
    def confidence(self):
        """Gets the confidence of this EventDetails.  # noqa: E501

        match confidence predicted by engine during event detection  # noqa: E501

        :return: The confidence of this EventDetails.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this EventDetails.

        match confidence predicted by engine during event detection  # noqa: E501

        :param confidence: The confidence of this EventDetails.  # noqa: E501
        :type: float
        """

        self._confidence = confidence

    @property
    def capture_time_in_video(self):
        """Gets the capture_time_in_video of this EventDetails.  # noqa: E501

        Event timestamp in video in Unix epoch milliseconds  # noqa: E501

        :return: The capture_time_in_video of this EventDetails.  # noqa: E501
        :rtype: int
        """
        return self._capture_time_in_video

    @capture_time_in_video.setter
    def capture_time_in_video(self, capture_time_in_video):
        """Sets the capture_time_in_video of this EventDetails.

        Event timestamp in video in Unix epoch milliseconds  # noqa: E501

        :param capture_time_in_video: The capture_time_in_video of this EventDetails.  # noqa: E501
        :type: int
        """

        self._capture_time_in_video = capture_time_in_video

    @property
    def extras(self):
        """Gets the extras of this EventDetails.  # noqa: E501


        :return: The extras of this EventDetails.  # noqa: E501
        :rtype: list[Extra]
        """
        return self._extras

    @extras.setter
    def extras(self, extras):
        """Sets the extras of this EventDetails.


        :param extras: The extras of this EventDetails.  # noqa: E501
        :type: list[Extra]
        """

        self._extras = extras

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
        if issubclass(EventDetails, dict):
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
        if not isinstance(other, EventDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
