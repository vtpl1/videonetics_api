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

class Snap(object):
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
        'snap': 'str',
        'full_snap': 'str',
        'snap_id': 'str',
        'snap_time_stamp': 'int',
        'process_count': 'int',
        'registered_face_id': 'str',
        'feature_vector1': 'list[list[float]]',
        'feature_vector2': 'list[list[float]]',
        'confidence': 'float',
        'updated': 'datetime',
        'created': 'datetime',
        'etag': 'str',
        'links': 'Links'
    }

    attribute_map = {
        'id': '_id',
        'snap': 'snap',
        'full_snap': 'fullSnap',
        'snap_id': 'snapId',
        'snap_time_stamp': 'snapTimeStamp',
        'process_count': 'processCount',
        'registered_face_id': 'registeredFaceId',
        'feature_vector1': 'featureVector1',
        'feature_vector2': 'featureVector2',
        'confidence': 'confidence',
        'updated': 'updated',
        'created': 'created',
        'etag': 'etag',
        'links': 'links'
    }

    def __init__(self, id=None, snap=None, full_snap='', snap_id=None, snap_time_stamp=None, process_count=0, registered_face_id='0', feature_vector1=None, feature_vector2=None, confidence=0, updated=None, created=None, etag=None, links=None):  # noqa: E501
        """Snap - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._snap = None
        self._full_snap = None
        self._snap_id = None
        self._snap_time_stamp = None
        self._process_count = None
        self._registered_face_id = None
        self._feature_vector1 = None
        self._feature_vector2 = None
        self._confidence = None
        self._updated = None
        self._created = None
        self._etag = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if snap is not None:
            self.snap = snap
        if full_snap is not None:
            self.full_snap = full_snap
        if snap_id is not None:
            self.snap_id = snap_id
        if snap_time_stamp is not None:
            self.snap_time_stamp = snap_time_stamp
        if process_count is not None:
            self.process_count = process_count
        if registered_face_id is not None:
            self.registered_face_id = registered_face_id
        if feature_vector1 is not None:
            self.feature_vector1 = feature_vector1
        if feature_vector2 is not None:
            self.feature_vector2 = feature_vector2
        if confidence is not None:
            self.confidence = confidence
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
        """Gets the id of this Snap.  # noqa: E501


        :return: The id of this Snap.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Snap.


        :param id: The id of this Snap.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def snap(self):
        """Gets the snap of this Snap.  # noqa: E501


        :return: The snap of this Snap.  # noqa: E501
        :rtype: str
        """
        return self._snap

    @snap.setter
    def snap(self, snap):
        """Sets the snap of this Snap.


        :param snap: The snap of this Snap.  # noqa: E501
        :type: str
        """

        self._snap = snap

    @property
    def full_snap(self):
        """Gets the full_snap of this Snap.  # noqa: E501


        :return: The full_snap of this Snap.  # noqa: E501
        :rtype: str
        """
        return self._full_snap

    @full_snap.setter
    def full_snap(self, full_snap):
        """Sets the full_snap of this Snap.


        :param full_snap: The full_snap of this Snap.  # noqa: E501
        :type: str
        """

        self._full_snap = full_snap

    @property
    def snap_id(self):
        """Gets the snap_id of this Snap.  # noqa: E501


        :return: The snap_id of this Snap.  # noqa: E501
        :rtype: str
        """
        return self._snap_id

    @snap_id.setter
    def snap_id(self, snap_id):
        """Sets the snap_id of this Snap.


        :param snap_id: The snap_id of this Snap.  # noqa: E501
        :type: str
        """

        self._snap_id = snap_id

    @property
    def snap_time_stamp(self):
        """Gets the snap_time_stamp of this Snap.  # noqa: E501

        Unix timestamp when snap is taken  # noqa: E501

        :return: The snap_time_stamp of this Snap.  # noqa: E501
        :rtype: int
        """
        return self._snap_time_stamp

    @snap_time_stamp.setter
    def snap_time_stamp(self, snap_time_stamp):
        """Sets the snap_time_stamp of this Snap.

        Unix timestamp when snap is taken  # noqa: E501

        :param snap_time_stamp: The snap_time_stamp of this Snap.  # noqa: E501
        :type: int
        """

        self._snap_time_stamp = snap_time_stamp

    @property
    def process_count(self):
        """Gets the process_count of this Snap.  # noqa: E501


        :return: The process_count of this Snap.  # noqa: E501
        :rtype: int
        """
        return self._process_count

    @process_count.setter
    def process_count(self, process_count):
        """Sets the process_count of this Snap.


        :param process_count: The process_count of this Snap.  # noqa: E501
        :type: int
        """

        self._process_count = process_count

    @property
    def registered_face_id(self):
        """Gets the registered_face_id of this Snap.  # noqa: E501


        :return: The registered_face_id of this Snap.  # noqa: E501
        :rtype: str
        """
        return self._registered_face_id

    @registered_face_id.setter
    def registered_face_id(self, registered_face_id):
        """Sets the registered_face_id of this Snap.


        :param registered_face_id: The registered_face_id of this Snap.  # noqa: E501
        :type: str
        """

        self._registered_face_id = registered_face_id

    @property
    def feature_vector1(self):
        """Gets the feature_vector1 of this Snap.  # noqa: E501


        :return: The feature_vector1 of this Snap.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._feature_vector1

    @feature_vector1.setter
    def feature_vector1(self, feature_vector1):
        """Sets the feature_vector1 of this Snap.


        :param feature_vector1: The feature_vector1 of this Snap.  # noqa: E501
        :type: list[list[float]]
        """

        self._feature_vector1 = feature_vector1

    @property
    def feature_vector2(self):
        """Gets the feature_vector2 of this Snap.  # noqa: E501


        :return: The feature_vector2 of this Snap.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._feature_vector2

    @feature_vector2.setter
    def feature_vector2(self, feature_vector2):
        """Sets the feature_vector2 of this Snap.


        :param feature_vector2: The feature_vector2 of this Snap.  # noqa: E501
        :type: list[list[float]]
        """

        self._feature_vector2 = feature_vector2

    @property
    def confidence(self):
        """Gets the confidence of this Snap.  # noqa: E501


        :return: The confidence of this Snap.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this Snap.


        :param confidence: The confidence of this Snap.  # noqa: E501
        :type: float
        """

        self._confidence = confidence

    @property
    def updated(self):
        """Gets the updated of this Snap.  # noqa: E501


        :return: The updated of this Snap.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Snap.


        :param updated: The updated of this Snap.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this Snap.  # noqa: E501


        :return: The created of this Snap.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Snap.


        :param created: The created of this Snap.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def etag(self):
        """Gets the etag of this Snap.  # noqa: E501


        :return: The etag of this Snap.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this Snap.


        :param etag: The etag of this Snap.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def links(self):
        """Gets the links of this Snap.  # noqa: E501


        :return: The links of this Snap.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Snap.


        :param links: The links of this Snap.  # noqa: E501
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
        if issubclass(Snap, dict):
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
        if not isinstance(other, Snap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other