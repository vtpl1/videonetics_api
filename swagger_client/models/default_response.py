# coding: utf-8

"""
    Engine api

    Engine APIs  # noqa: E501

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DefaultResponse(object):
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
        'updated': 'datetime',
        'created': 'datetime',
        'etag': 'str',
        'links': 'LinksSelf',
        'status': 'str'
    }

    attribute_map = {
        'id': '_id',
        'updated': 'updated',
        'created': 'created',
        'etag': 'etag',
        'links': 'links',
        'status': 'status'
    }

    def __init__(self, id=None, updated=None, created=None, etag=None, links=None, status=None):  # noqa: E501
        """DefaultResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._updated = None
        self._created = None
        self._etag = None
        self._links = None
        self._status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if etag is not None:
            self.etag = etag
        if links is not None:
            self.links = links
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this DefaultResponse.  # noqa: E501


        :return: The id of this DefaultResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DefaultResponse.


        :param id: The id of this DefaultResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def updated(self):
        """Gets the updated of this DefaultResponse.  # noqa: E501


        :return: The updated of this DefaultResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this DefaultResponse.


        :param updated: The updated of this DefaultResponse.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this DefaultResponse.  # noqa: E501


        :return: The created of this DefaultResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DefaultResponse.


        :param created: The created of this DefaultResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def etag(self):
        """Gets the etag of this DefaultResponse.  # noqa: E501


        :return: The etag of this DefaultResponse.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this DefaultResponse.


        :param etag: The etag of this DefaultResponse.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def links(self):
        """Gets the links of this DefaultResponse.  # noqa: E501


        :return: The links of this DefaultResponse.  # noqa: E501
        :rtype: LinksSelf
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DefaultResponse.


        :param links: The links of this DefaultResponse.  # noqa: E501
        :type: LinksSelf
        """

        self._links = links

    @property
    def status(self):
        """Gets the status of this DefaultResponse.  # noqa: E501


        :return: The status of this DefaultResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DefaultResponse.


        :param status: The status of this DefaultResponse.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(DefaultResponse, dict):
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
        if not isinstance(other, DefaultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
