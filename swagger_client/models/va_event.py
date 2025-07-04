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
from swagger_client.models.event import Event  # noqa: F401,E501

class VaEvent(Event):
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
        'meta_va_event': 'MetaVaEvent'
    }
    if hasattr(Event, "swagger_types"):
        swagger_types.update(Event.swagger_types)

    attribute_map = {
        'meta_va_event': 'metaVaEvent'
    }
    if hasattr(Event, "attribute_map"):
        attribute_map.update(Event.attribute_map)

    def __init__(self, meta_va_event=None, *args, **kwargs):  # noqa: E501
        """VaEvent - a model defined in Swagger"""  # noqa: E501
        self._meta_va_event = None
        self.discriminator = None
        if meta_va_event is not None:
            self.meta_va_event = meta_va_event
        Event.__init__(self, *args, **kwargs)

    @property
    def meta_va_event(self):
        """Gets the meta_va_event of this VaEvent.  # noqa: E501


        :return: The meta_va_event of this VaEvent.  # noqa: E501
        :rtype: MetaVaEvent
        """
        return self._meta_va_event

    @meta_va_event.setter
    def meta_va_event(self, meta_va_event):
        """Sets the meta_va_event of this VaEvent.


        :param meta_va_event: The meta_va_event of this VaEvent.  # noqa: E501
        :type: MetaVaEvent
        """

        self._meta_va_event = meta_va_event

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
        if issubclass(VaEvent, dict):
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
        if not isinstance(other, VaEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
