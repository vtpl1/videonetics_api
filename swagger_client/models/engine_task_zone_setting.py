# coding: utf-8

"""
    Engine api

    Engine APIs  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EngineTaskZoneSetting(object):
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
        'reference_width': 'int',
        'reference_height': 'int',
        'zones': 'list[Zone]'
    }

    attribute_map = {
        'reference_width': 'referenceWidth',
        'reference_height': 'referenceHeight',
        'zones': 'zones'
    }

    def __init__(self, reference_width=None, reference_height=None, zones=None):  # noqa: E501
        """EngineTaskZoneSetting - a model defined in Swagger"""  # noqa: E501
        self._reference_width = None
        self._reference_height = None
        self._zones = None
        self.discriminator = None
        if reference_width is not None:
            self.reference_width = reference_width
        if reference_height is not None:
            self.reference_height = reference_height
        if zones is not None:
            self.zones = zones

    @property
    def reference_width(self):
        """Gets the reference_width of this EngineTaskZoneSetting.  # noqa: E501

        Reference width on which zones are relevent  # noqa: E501

        :return: The reference_width of this EngineTaskZoneSetting.  # noqa: E501
        :rtype: int
        """
        return self._reference_width

    @reference_width.setter
    def reference_width(self, reference_width):
        """Sets the reference_width of this EngineTaskZoneSetting.

        Reference width on which zones are relevent  # noqa: E501

        :param reference_width: The reference_width of this EngineTaskZoneSetting.  # noqa: E501
        :type: int
        """

        self._reference_width = reference_width

    @property
    def reference_height(self):
        """Gets the reference_height of this EngineTaskZoneSetting.  # noqa: E501

        Reference height on which zones are relevent  # noqa: E501

        :return: The reference_height of this EngineTaskZoneSetting.  # noqa: E501
        :rtype: int
        """
        return self._reference_height

    @reference_height.setter
    def reference_height(self, reference_height):
        """Sets the reference_height of this EngineTaskZoneSetting.

        Reference height on which zones are relevent  # noqa: E501

        :param reference_height: The reference_height of this EngineTaskZoneSetting.  # noqa: E501
        :type: int
        """

        self._reference_height = reference_height

    @property
    def zones(self):
        """Gets the zones of this EngineTaskZoneSetting.  # noqa: E501


        :return: The zones of this EngineTaskZoneSetting.  # noqa: E501
        :rtype: list[Zone]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """Sets the zones of this EngineTaskZoneSetting.


        :param zones: The zones of this EngineTaskZoneSetting.  # noqa: E501
        :type: list[Zone]
        """

        self._zones = zones

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
        if issubclass(EngineTaskZoneSetting, dict):
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
        if not isinstance(other, EngineTaskZoneSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
