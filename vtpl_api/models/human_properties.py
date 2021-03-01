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

class HumanProperties(object):
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
        'gender': 'str',
        'top_attire_color': 'str',
        'bottom_attire_color': 'str',
        'top_type': 'str',
        'bottom_type': 'str',
        'is_long_sleeve': 'str',
        'is_headdress_present': 'str',
        'is_bag_present': 'str'
    }

    attribute_map = {
        'gender': 'gender',
        'top_attire_color': 'topAttireColor',
        'bottom_attire_color': 'bottomAttireColor',
        'top_type': 'topType',
        'bottom_type': 'bottomType',
        'is_long_sleeve': 'isLongSleeve',
        'is_headdress_present': 'isHeaddressPresent',
        'is_bag_present': 'isBagPresent'
    }

    def __init__(self, gender=None, top_attire_color=None, bottom_attire_color=None, top_type=None, bottom_type=None, is_long_sleeve=None, is_headdress_present=None, is_bag_present=None):  # noqa: E501
        """HumanProperties - a model defined in Swagger"""  # noqa: E501
        self._gender = None
        self._top_attire_color = None
        self._bottom_attire_color = None
        self._top_type = None
        self._bottom_type = None
        self._is_long_sleeve = None
        self._is_headdress_present = None
        self._is_bag_present = None
        self.discriminator = None
        if gender is not None:
            self.gender = gender
        if top_attire_color is not None:
            self.top_attire_color = top_attire_color
        if bottom_attire_color is not None:
            self.bottom_attire_color = bottom_attire_color
        if top_type is not None:
            self.top_type = top_type
        if bottom_type is not None:
            self.bottom_type = bottom_type
        if is_long_sleeve is not None:
            self.is_long_sleeve = is_long_sleeve
        if is_headdress_present is not None:
            self.is_headdress_present = is_headdress_present
        if is_bag_present is not None:
            self.is_bag_present = is_bag_present

    @property
    def gender(self):
        """Gets the gender of this HumanProperties.  # noqa: E501


        :return: The gender of this HumanProperties.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this HumanProperties.


        :param gender: The gender of this HumanProperties.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def top_attire_color(self):
        """Gets the top_attire_color of this HumanProperties.  # noqa: E501


        :return: The top_attire_color of this HumanProperties.  # noqa: E501
        :rtype: str
        """
        return self._top_attire_color

    @top_attire_color.setter
    def top_attire_color(self, top_attire_color):
        """Sets the top_attire_color of this HumanProperties.


        :param top_attire_color: The top_attire_color of this HumanProperties.  # noqa: E501
        :type: str
        """

        self._top_attire_color = top_attire_color

    @property
    def bottom_attire_color(self):
        """Gets the bottom_attire_color of this HumanProperties.  # noqa: E501


        :return: The bottom_attire_color of this HumanProperties.  # noqa: E501
        :rtype: str
        """
        return self._bottom_attire_color

    @bottom_attire_color.setter
    def bottom_attire_color(self, bottom_attire_color):
        """Sets the bottom_attire_color of this HumanProperties.


        :param bottom_attire_color: The bottom_attire_color of this HumanProperties.  # noqa: E501
        :type: str
        """

        self._bottom_attire_color = bottom_attire_color

    @property
    def top_type(self):
        """Gets the top_type of this HumanProperties.  # noqa: E501


        :return: The top_type of this HumanProperties.  # noqa: E501
        :rtype: str
        """
        return self._top_type

    @top_type.setter
    def top_type(self, top_type):
        """Sets the top_type of this HumanProperties.


        :param top_type: The top_type of this HumanProperties.  # noqa: E501
        :type: str
        """

        self._top_type = top_type

    @property
    def bottom_type(self):
        """Gets the bottom_type of this HumanProperties.  # noqa: E501


        :return: The bottom_type of this HumanProperties.  # noqa: E501
        :rtype: str
        """
        return self._bottom_type

    @bottom_type.setter
    def bottom_type(self, bottom_type):
        """Sets the bottom_type of this HumanProperties.


        :param bottom_type: The bottom_type of this HumanProperties.  # noqa: E501
        :type: str
        """

        self._bottom_type = bottom_type

    @property
    def is_long_sleeve(self):
        """Gets the is_long_sleeve of this HumanProperties.  # noqa: E501


        :return: The is_long_sleeve of this HumanProperties.  # noqa: E501
        :rtype: str
        """
        return self._is_long_sleeve

    @is_long_sleeve.setter
    def is_long_sleeve(self, is_long_sleeve):
        """Sets the is_long_sleeve of this HumanProperties.


        :param is_long_sleeve: The is_long_sleeve of this HumanProperties.  # noqa: E501
        :type: str
        """

        self._is_long_sleeve = is_long_sleeve

    @property
    def is_headdress_present(self):
        """Gets the is_headdress_present of this HumanProperties.  # noqa: E501


        :return: The is_headdress_present of this HumanProperties.  # noqa: E501
        :rtype: str
        """
        return self._is_headdress_present

    @is_headdress_present.setter
    def is_headdress_present(self, is_headdress_present):
        """Sets the is_headdress_present of this HumanProperties.


        :param is_headdress_present: The is_headdress_present of this HumanProperties.  # noqa: E501
        :type: str
        """

        self._is_headdress_present = is_headdress_present

    @property
    def is_bag_present(self):
        """Gets the is_bag_present of this HumanProperties.  # noqa: E501


        :return: The is_bag_present of this HumanProperties.  # noqa: E501
        :rtype: str
        """
        return self._is_bag_present

    @is_bag_present.setter
    def is_bag_present(self, is_bag_present):
        """Sets the is_bag_present of this HumanProperties.


        :param is_bag_present: The is_bag_present of this HumanProperties.  # noqa: E501
        :type: str
        """

        self._is_bag_present = is_bag_present

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
        if issubclass(HumanProperties, dict):
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
        if not isinstance(other, HumanProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other