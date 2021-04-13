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

class EngineTaskStatus(object):
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
        'progress': 'EngineTaskStatusProgress',
        'failure': 'EngineTaskStatusFailure'
    }

    attribute_map = {
        'id': '_id',
        'engine_task_id': 'engineTaskId',
        'progress': 'progress',
        'failure': 'failure'
    }

    def __init__(self, id=None, engine_task_id=None, progress=None, failure=None):  # noqa: E501
        """EngineTaskStatus - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._engine_task_id = None
        self._progress = None
        self._failure = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if engine_task_id is not None:
            self.engine_task_id = engine_task_id
        if progress is not None:
            self.progress = progress
        if failure is not None:
            self.failure = failure

    @property
    def id(self):
        """Gets the id of this EngineTaskStatus.  # noqa: E501


        :return: The id of this EngineTaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EngineTaskStatus.


        :param id: The id of this EngineTaskStatus.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def engine_task_id(self):
        """Gets the engine_task_id of this EngineTaskStatus.  # noqa: E501


        :return: The engine_task_id of this EngineTaskStatus.  # noqa: E501
        :rtype: str
        """
        return self._engine_task_id

    @engine_task_id.setter
    def engine_task_id(self, engine_task_id):
        """Sets the engine_task_id of this EngineTaskStatus.


        :param engine_task_id: The engine_task_id of this EngineTaskStatus.  # noqa: E501
        :type: str
        """

        self._engine_task_id = engine_task_id

    @property
    def progress(self):
        """Gets the progress of this EngineTaskStatus.  # noqa: E501


        :return: The progress of this EngineTaskStatus.  # noqa: E501
        :rtype: EngineTaskStatusProgress
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this EngineTaskStatus.


        :param progress: The progress of this EngineTaskStatus.  # noqa: E501
        :type: EngineTaskStatusProgress
        """

        self._progress = progress

    @property
    def failure(self):
        """Gets the failure of this EngineTaskStatus.  # noqa: E501


        :return: The failure of this EngineTaskStatus.  # noqa: E501
        :rtype: EngineTaskStatusFailure
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """Sets the failure of this EngineTaskStatus.


        :param failure: The failure of this EngineTaskStatus.  # noqa: E501
        :type: EngineTaskStatusFailure
        """

        self._failure = failure

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
        if issubclass(EngineTaskStatus, dict):
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
        if not isinstance(other, EngineTaskStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
