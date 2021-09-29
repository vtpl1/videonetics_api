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

class ObjectRectWithTimeStampAndEventSnapReference(object):
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
        'time_stamp': 'int',
        'event_snap_index': 'int',
        'object_rect': 'ObjectRect'
    }

    attribute_map = {
        'time_stamp': 'timeStamp',
        'event_snap_index': 'eventSnapIndex',
        'object_rect': 'objectRect'
    }

    def __init__(self, time_stamp=None, event_snap_index=0, object_rect=None):  # noqa: E501
        """ObjectRectWithTimeStampAndEventSnapReference - a model defined in Swagger"""  # noqa: E501
        self._time_stamp = None
        self._event_snap_index = None
        self._object_rect = None
        self.discriminator = None
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if event_snap_index is not None:
            self.event_snap_index = event_snap_index
        if object_rect is not None:
            self.object_rect = object_rect

    @property
    def time_stamp(self):
        """Gets the time_stamp of this ObjectRectWithTimeStampAndEventSnapReference.  # noqa: E501


        :return: The time_stamp of this ObjectRectWithTimeStampAndEventSnapReference.  # noqa: E501
        :rtype: int
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this ObjectRectWithTimeStampAndEventSnapReference.


        :param time_stamp: The time_stamp of this ObjectRectWithTimeStampAndEventSnapReference.  # noqa: E501
        :type: int
        """

        self._time_stamp = time_stamp

    @property
    def event_snap_index(self):
        """Gets the event_snap_index of this ObjectRectWithTimeStampAndEventSnapReference.  # noqa: E501


        :return: The event_snap_index of this ObjectRectWithTimeStampAndEventSnapReference.  # noqa: E501
        :rtype: int
        """
        return self._event_snap_index

    @event_snap_index.setter
    def event_snap_index(self, event_snap_index):
        """Sets the event_snap_index of this ObjectRectWithTimeStampAndEventSnapReference.


        :param event_snap_index: The event_snap_index of this ObjectRectWithTimeStampAndEventSnapReference.  # noqa: E501
        :type: int
        """

        self._event_snap_index = event_snap_index

    @property
    def object_rect(self):
        """Gets the object_rect of this ObjectRectWithTimeStampAndEventSnapReference.  # noqa: E501


        :return: The object_rect of this ObjectRectWithTimeStampAndEventSnapReference.  # noqa: E501
        :rtype: ObjectRect
        """
        return self._object_rect

    @object_rect.setter
    def object_rect(self, object_rect):
        """Sets the object_rect of this ObjectRectWithTimeStampAndEventSnapReference.


        :param object_rect: The object_rect of this ObjectRectWithTimeStampAndEventSnapReference.  # noqa: E501
        :type: ObjectRect
        """

        self._object_rect = object_rect

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
        if issubclass(ObjectRectWithTimeStampAndEventSnapReference, dict):
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
        if not isinstance(other, ObjectRectWithTimeStampAndEventSnapReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
