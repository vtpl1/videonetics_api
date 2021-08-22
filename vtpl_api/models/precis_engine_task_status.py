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

class PrecisEngineTaskStatus(object):
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
        'engine_task_id': 'str',
        'result_url': 'str',
        'progress': 'EngineTaskStatusProgress',
        'failure': 'EngineTaskStatusFailure',
        'updated': 'datetime',
        'created': 'datetime',
        'etag': 'str',
        'links': 'Links'
    }

    attribute_map = {
        'id': '_id',
        'engine_task_id': 'engineTaskId',
        'result_url': 'resultUrl',
        'progress': 'progress',
        'failure': 'failure',
        'updated': 'updated',
        'created': 'created',
        'etag': 'etag',
        'links': 'links'
    }

    def __init__(self, id=None, engine_task_id=None, result_url=None, progress=None, failure=None, updated=None, created=None, etag=None, links=None):  # noqa: E501
        """PrecisEngineTaskStatus - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._engine_task_id = None
        self._result_url = None
        self._progress = None
        self._failure = None
        self._updated = None
        self._created = None
        self._etag = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if engine_task_id is not None:
            self.engine_task_id = engine_task_id
        if result_url is not None:
            self.result_url = result_url
        if progress is not None:
            self.progress = progress
        if failure is not None:
            self.failure = failure
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
        """Gets the id of this PrecisEngineTaskStatus.  # noqa: E501


        :return: The id of this PrecisEngineTaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrecisEngineTaskStatus.


        :param id: The id of this PrecisEngineTaskStatus.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def engine_task_id(self):
        """Gets the engine_task_id of this PrecisEngineTaskStatus.  # noqa: E501


        :return: The engine_task_id of this PrecisEngineTaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._engine_task_id

    @engine_task_id.setter
    def engine_task_id(self, engine_task_id):
        """Sets the engine_task_id of this PrecisEngineTaskStatus.


        :param engine_task_id: The engine_task_id of this PrecisEngineTaskStatus.  # noqa: E501
        :type: str
        """

        self._engine_task_id = engine_task_id

    @property
    def result_url(self):
        """Gets the result_url of this PrecisEngineTaskStatus.  # noqa: E501


        :return: The result_url of this PrecisEngineTaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._result_url

    @result_url.setter
    def result_url(self, result_url):
        """Sets the result_url of this PrecisEngineTaskStatus.


        :param result_url: The result_url of this PrecisEngineTaskStatus.  # noqa: E501
        :type: str
        """

        self._result_url = result_url

    @property
    def progress(self):
        """Gets the progress of this PrecisEngineTaskStatus.  # noqa: E501


        :return: The progress of this PrecisEngineTaskStatus.  # noqa: E501
        :rtype: EngineTaskStatusProgress
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this PrecisEngineTaskStatus.


        :param progress: The progress of this PrecisEngineTaskStatus.  # noqa: E501
        :type: EngineTaskStatusProgress
        """

        self._progress = progress

    @property
    def failure(self):
        """Gets the failure of this PrecisEngineTaskStatus.  # noqa: E501


        :return: The failure of this PrecisEngineTaskStatus.  # noqa: E501
        :rtype: EngineTaskStatusFailure
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """Sets the failure of this PrecisEngineTaskStatus.


        :param failure: The failure of this PrecisEngineTaskStatus.  # noqa: E501
        :type: EngineTaskStatusFailure
        """

        self._failure = failure

    @property
    def updated(self):
        """Gets the updated of this PrecisEngineTaskStatus.  # noqa: E501


        :return: The updated of this PrecisEngineTaskStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this PrecisEngineTaskStatus.


        :param updated: The updated of this PrecisEngineTaskStatus.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this PrecisEngineTaskStatus.  # noqa: E501


        :return: The created of this PrecisEngineTaskStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PrecisEngineTaskStatus.


        :param created: The created of this PrecisEngineTaskStatus.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def etag(self):
        """Gets the etag of this PrecisEngineTaskStatus.  # noqa: E501


        :return: The etag of this PrecisEngineTaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this PrecisEngineTaskStatus.


        :param etag: The etag of this PrecisEngineTaskStatus.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def links(self):
        """Gets the links of this PrecisEngineTaskStatus.  # noqa: E501


        :return: The links of this PrecisEngineTaskStatus.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PrecisEngineTaskStatus.


        :param links: The links of this PrecisEngineTaskStatus.  # noqa: E501
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
        if issubclass(PrecisEngineTaskStatus, dict):
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
        if not isinstance(other, PrecisEngineTaskStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
