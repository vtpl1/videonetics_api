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

class ObjectInfo(object):
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
        'object_direct_properties': 'ObjectDirectProperties',
        'object_indirect_properties': 'ObjectIndirectProperties',
        'object_type': 'str',
        'object_rect': 'ObjectRect',
        'confidence': 'float',
        'is_valid': 'bool'
    }

    attribute_map = {
        'object_direct_properties': 'objectDirectProperties',
        'object_indirect_properties': 'objectIndirectProperties',
        'object_type': 'objectType',
        'object_rect': 'objectRect',
        'confidence': 'confidence',
        'is_valid': 'isValid'
    }

    def __init__(self, object_direct_properties=None, object_indirect_properties=None, object_type=None, object_rect=None, confidence=0, is_valid=False):  # noqa: E501
        """ObjectInfo - a model defined in Swagger"""  # noqa: E501
        self._object_direct_properties = None
        self._object_indirect_properties = None
        self._object_type = None
        self._object_rect = None
        self._confidence = None
        self._is_valid = None
        self.discriminator = None
        if object_direct_properties is not None:
            self.object_direct_properties = object_direct_properties
        if object_indirect_properties is not None:
            self.object_indirect_properties = object_indirect_properties
        if object_type is not None:
            self.object_type = object_type
        if object_rect is not None:
            self.object_rect = object_rect
        if confidence is not None:
            self.confidence = confidence
        if is_valid is not None:
            self.is_valid = is_valid

    @property
    def object_direct_properties(self):
        """Gets the object_direct_properties of this ObjectInfo.  # noqa: E501


        :return: The object_direct_properties of this ObjectInfo.  # noqa: E501
        :rtype: ObjectDirectProperties
        """
        return self._object_direct_properties

    @object_direct_properties.setter
    def object_direct_properties(self, object_direct_properties):
        """Sets the object_direct_properties of this ObjectInfo.


        :param object_direct_properties: The object_direct_properties of this ObjectInfo.  # noqa: E501
        :type: ObjectDirectProperties
        """

        self._object_direct_properties = object_direct_properties

    @property
    def object_indirect_properties(self):
        """Gets the object_indirect_properties of this ObjectInfo.  # noqa: E501


        :return: The object_indirect_properties of this ObjectInfo.  # noqa: E501
        :rtype: ObjectIndirectProperties
        """
        return self._object_indirect_properties

    @object_indirect_properties.setter
    def object_indirect_properties(self, object_indirect_properties):
        """Sets the object_indirect_properties of this ObjectInfo.


        :param object_indirect_properties: The object_indirect_properties of this ObjectInfo.  # noqa: E501
        :type: ObjectIndirectProperties
        """

        self._object_indirect_properties = object_indirect_properties

    @property
    def object_type(self):
        """Gets the object_type of this ObjectInfo.  # noqa: E501


        :return: The object_type of this ObjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ObjectInfo.


        :param object_type: The object_type of this ObjectInfo.  # noqa: E501
        :type: str
        """

        self._object_type = object_type

    @property
    def object_rect(self):
        """Gets the object_rect of this ObjectInfo.  # noqa: E501


        :return: The object_rect of this ObjectInfo.  # noqa: E501
        :rtype: ObjectRect
        """
        return self._object_rect

    @object_rect.setter
    def object_rect(self, object_rect):
        """Sets the object_rect of this ObjectInfo.


        :param object_rect: The object_rect of this ObjectInfo.  # noqa: E501
        :type: ObjectRect
        """

        self._object_rect = object_rect

    @property
    def confidence(self):
        """Gets the confidence of this ObjectInfo.  # noqa: E501


        :return: The confidence of this ObjectInfo.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ObjectInfo.


        :param confidence: The confidence of this ObjectInfo.  # noqa: E501
        :type: float
        """

        self._confidence = confidence

    @property
    def is_valid(self):
        """Gets the is_valid of this ObjectInfo.  # noqa: E501


        :return: The is_valid of this ObjectInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this ObjectInfo.


        :param is_valid: The is_valid of this ObjectInfo.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

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
        if issubclass(ObjectInfo, dict):
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
        if not isinstance(other, ObjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
