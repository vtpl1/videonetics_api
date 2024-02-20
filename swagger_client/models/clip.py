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

class Clip(object):
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
        'clip': 'str',
        'clip_id': 'str',
        'starp_time_stamp': 'int',
        'end_time_stamp': 'int',
        'updated': 'datetime',
        'created': 'datetime',
        'etag': 'str',
        'links': 'Links'
    }

    attribute_map = {
        'id': '_id',
        'clip': 'clip',
        'clip_id': 'clipId',
        'starp_time_stamp': 'starpTimeStamp',
        'end_time_stamp': 'endTimeStamp',
        'updated': 'updated',
        'created': 'created',
        'etag': 'etag',
        'links': 'links'
    }

    def __init__(self, id=None, clip=None, clip_id=None, starp_time_stamp=None, end_time_stamp=None, updated=None, created=None, etag=None, links=None):  # noqa: E501
        """Clip - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._clip = None
        self._clip_id = None
        self._starp_time_stamp = None
        self._end_time_stamp = None
        self._updated = None
        self._created = None
        self._etag = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if clip is not None:
            self.clip = clip
        if clip_id is not None:
            self.clip_id = clip_id
        if starp_time_stamp is not None:
            self.starp_time_stamp = starp_time_stamp
        if end_time_stamp is not None:
            self.end_time_stamp = end_time_stamp
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if etag is not None:
            self.etag = etag
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this Clip.  # noqa: E501


        :return: The id of this Clip.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Clip.


        :param id: The id of this Clip.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def clip(self):
        """Gets the clip of this Clip.  # noqa: E501


        :return: The clip of this Clip.  # noqa: E501
        :rtype: str
        """
        return self._clip

    @clip.setter
    def clip(self, clip):
        """Sets the clip of this Clip.


        :param clip: The clip of this Clip.  # noqa: E501
        :type: str
        """

        self._clip = clip

    @property
    def clip_id(self):
        """Gets the clip_id of this Clip.  # noqa: E501


        :return: The clip_id of this Clip.  # noqa: E501
        :rtype: str
        """
        return self._clip_id

    @clip_id.setter
    def clip_id(self, clip_id):
        """Sets the clip_id of this Clip.


        :param clip_id: The clip_id of this Clip.  # noqa: E501
        :type: str
        """

        self._clip_id = clip_id

    @property
    def starp_time_stamp(self):
        """Gets the starp_time_stamp of this Clip.  # noqa: E501

        Unix timestamp from when clip is recorded  # noqa: E501

        :return: The starp_time_stamp of this Clip.  # noqa: E501
        :rtype: int
        """
        return self._starp_time_stamp

    @starp_time_stamp.setter
    def starp_time_stamp(self, starp_time_stamp):
        """Sets the starp_time_stamp of this Clip.

        Unix timestamp from when clip is recorded  # noqa: E501

        :param starp_time_stamp: The starp_time_stamp of this Clip.  # noqa: E501
        :type: int
        """

        self._starp_time_stamp = starp_time_stamp

    @property
    def end_time_stamp(self):
        """Gets the end_time_stamp of this Clip.  # noqa: E501

        Unix timestamp till when clip is recorded  # noqa: E501

        :return: The end_time_stamp of this Clip.  # noqa: E501
        :rtype: int
        """
        return self._end_time_stamp

    @end_time_stamp.setter
    def end_time_stamp(self, end_time_stamp):
        """Sets the end_time_stamp of this Clip.

        Unix timestamp till when clip is recorded  # noqa: E501

        :param end_time_stamp: The end_time_stamp of this Clip.  # noqa: E501
        :type: int
        """

        self._end_time_stamp = end_time_stamp

    @property
    def updated(self):
        """Gets the updated of this Clip.  # noqa: E501


        :return: The updated of this Clip.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Clip.


        :param updated: The updated of this Clip.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this Clip.  # noqa: E501


        :return: The created of this Clip.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Clip.


        :param created: The created of this Clip.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def etag(self):
        """Gets the etag of this Clip.  # noqa: E501


        :return: The etag of this Clip.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this Clip.


        :param etag: The etag of this Clip.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def links(self):
        """Gets the links of this Clip.  # noqa: E501


        :return: The links of this Clip.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Clip.


        :param links: The links of this Clip.  # noqa: E501
        :type: Links
        """

        self._links = links

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
        if issubclass(Clip, dict):
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
        if not isinstance(other, Clip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
