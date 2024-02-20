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

class Inferencer(object):
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
        'links': 'Links',
        'name': 'str',
        'description': 'str',
        'class_to_load': 'str',
        'module_to_load': 'str',
        'module_path_to_download_from': 'str',
        'confidence': 'float'
    }

    attribute_map = {
        'id': '_id',
        'updated': 'updated',
        'created': 'created',
        'etag': 'etag',
        'links': 'links',
        'name': 'name',
        'description': 'description',
        'class_to_load': 'classToLoad',
        'module_to_load': 'moduleToLoad',
        'module_path_to_download_from': 'modulePathToDownloadFrom',
        'confidence': 'confidence'
    }

    def __init__(self, id=None, updated=None, created=None, etag=None, links=None, name=None, description=None, class_to_load=None, module_to_load=None, module_path_to_download_from=None, confidence=10):  # noqa: E501
        """Inferencer - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._updated = None
        self._created = None
        self._etag = None
        self._links = None
        self._name = None
        self._description = None
        self._class_to_load = None
        self._module_to_load = None
        self._module_path_to_download_from = None
        self._confidence = None
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
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if class_to_load is not None:
            self.class_to_load = class_to_load
        if module_to_load is not None:
            self.module_to_load = module_to_load
        if module_path_to_download_from is not None:
            self.module_path_to_download_from = module_path_to_download_from
        if confidence is not None:
            self.confidence = confidence

    @property
    def id(self):
        """Gets the id of this Inferencer.  # noqa: E501


        :return: The id of this Inferencer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Inferencer.


        :param id: The id of this Inferencer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def updated(self):
        """Gets the updated of this Inferencer.  # noqa: E501


        :return: The updated of this Inferencer.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Inferencer.


        :param updated: The updated of this Inferencer.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this Inferencer.  # noqa: E501


        :return: The created of this Inferencer.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Inferencer.


        :param created: The created of this Inferencer.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def etag(self):
        """Gets the etag of this Inferencer.  # noqa: E501


        :return: The etag of this Inferencer.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this Inferencer.


        :param etag: The etag of this Inferencer.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def links(self):
        """Gets the links of this Inferencer.  # noqa: E501


        :return: The links of this Inferencer.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Inferencer.


        :param links: The links of this Inferencer.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this Inferencer.  # noqa: E501


        :return: The name of this Inferencer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Inferencer.


        :param name: The name of this Inferencer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Inferencer.  # noqa: E501


        :return: The description of this Inferencer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Inferencer.


        :param description: The description of this Inferencer.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def class_to_load(self):
        """Gets the class_to_load of this Inferencer.  # noqa: E501


        :return: The class_to_load of this Inferencer.  # noqa: E501
        :rtype: str
        """
        return self._class_to_load

    @class_to_load.setter
    def class_to_load(self, class_to_load):
        """Sets the class_to_load of this Inferencer.


        :param class_to_load: The class_to_load of this Inferencer.  # noqa: E501
        :type: str
        """

        self._class_to_load = class_to_load

    @property
    def module_to_load(self):
        """Gets the module_to_load of this Inferencer.  # noqa: E501


        :return: The module_to_load of this Inferencer.  # noqa: E501
        :rtype: str
        """
        return self._module_to_load

    @module_to_load.setter
    def module_to_load(self, module_to_load):
        """Sets the module_to_load of this Inferencer.


        :param module_to_load: The module_to_load of this Inferencer.  # noqa: E501
        :type: str
        """

        self._module_to_load = module_to_load

    @property
    def module_path_to_download_from(self):
        """Gets the module_path_to_download_from of this Inferencer.  # noqa: E501


        :return: The module_path_to_download_from of this Inferencer.  # noqa: E501
        :rtype: str
        """
        return self._module_path_to_download_from

    @module_path_to_download_from.setter
    def module_path_to_download_from(self, module_path_to_download_from):
        """Sets the module_path_to_download_from of this Inferencer.


        :param module_path_to_download_from: The module_path_to_download_from of this Inferencer.  # noqa: E501
        :type: str
        """

        self._module_path_to_download_from = module_path_to_download_from

    @property
    def confidence(self):
        """Gets the confidence of this Inferencer.  # noqa: E501

        inferencer Threshold  # noqa: E501

        :return: The confidence of this Inferencer.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this Inferencer.

        inferencer Threshold  # noqa: E501

        :param confidence: The confidence of this Inferencer.  # noqa: E501
        :type: float
        """

        self._confidence = confidence

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
        if issubclass(Inferencer, dict):
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
        if not isinstance(other, Inferencer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
