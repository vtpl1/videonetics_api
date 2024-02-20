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

class EngineTaskStatusCumulative(object):
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
        'total_tasks': 'int',
        'yet_to_allocate_tasks': 'int',
        'allocated_tasks': 'int',
        'completed_tasks': 'int'
    }

    attribute_map = {
        'total_tasks': 'totalTasks',
        'yet_to_allocate_tasks': 'yetToAllocateTasks',
        'allocated_tasks': 'allocatedTasks',
        'completed_tasks': 'completedTasks'
    }

    def __init__(self, total_tasks=None, yet_to_allocate_tasks=None, allocated_tasks=None, completed_tasks=None):  # noqa: E501
        """EngineTaskStatusCumulative - a model defined in Swagger"""  # noqa: E501
        self._total_tasks = None
        self._yet_to_allocate_tasks = None
        self._allocated_tasks = None
        self._completed_tasks = None
        self.discriminator = None
        if total_tasks is not None:
            self.total_tasks = total_tasks
        if yet_to_allocate_tasks is not None:
            self.yet_to_allocate_tasks = yet_to_allocate_tasks
        if allocated_tasks is not None:
            self.allocated_tasks = allocated_tasks
        if completed_tasks is not None:
            self.completed_tasks = completed_tasks

    @property
    def total_tasks(self):
        """Gets the total_tasks of this EngineTaskStatusCumulative.  # noqa: E501


        :return: The total_tasks of this EngineTaskStatusCumulative.  # noqa: E501
        :rtype: int
        """
        return self._total_tasks

    @total_tasks.setter
    def total_tasks(self, total_tasks):
        """Sets the total_tasks of this EngineTaskStatusCumulative.


        :param total_tasks: The total_tasks of this EngineTaskStatusCumulative.  # noqa: E501
        :type: int
        """

        self._total_tasks = total_tasks

    @property
    def yet_to_allocate_tasks(self):
        """Gets the yet_to_allocate_tasks of this EngineTaskStatusCumulative.  # noqa: E501


        :return: The yet_to_allocate_tasks of this EngineTaskStatusCumulative.  # noqa: E501
        :rtype: int
        """
        return self._yet_to_allocate_tasks

    @yet_to_allocate_tasks.setter
    def yet_to_allocate_tasks(self, yet_to_allocate_tasks):
        """Sets the yet_to_allocate_tasks of this EngineTaskStatusCumulative.


        :param yet_to_allocate_tasks: The yet_to_allocate_tasks of this EngineTaskStatusCumulative.  # noqa: E501
        :type: int
        """

        self._yet_to_allocate_tasks = yet_to_allocate_tasks

    @property
    def allocated_tasks(self):
        """Gets the allocated_tasks of this EngineTaskStatusCumulative.  # noqa: E501


        :return: The allocated_tasks of this EngineTaskStatusCumulative.  # noqa: E501
        :rtype: int
        """
        return self._allocated_tasks

    @allocated_tasks.setter
    def allocated_tasks(self, allocated_tasks):
        """Sets the allocated_tasks of this EngineTaskStatusCumulative.


        :param allocated_tasks: The allocated_tasks of this EngineTaskStatusCumulative.  # noqa: E501
        :type: int
        """

        self._allocated_tasks = allocated_tasks

    @property
    def completed_tasks(self):
        """Gets the completed_tasks of this EngineTaskStatusCumulative.  # noqa: E501


        :return: The completed_tasks of this EngineTaskStatusCumulative.  # noqa: E501
        :rtype: int
        """
        return self._completed_tasks

    @completed_tasks.setter
    def completed_tasks(self, completed_tasks):
        """Sets the completed_tasks of this EngineTaskStatusCumulative.


        :param completed_tasks: The completed_tasks of this EngineTaskStatusCumulative.  # noqa: E501
        :type: int
        """

        self._completed_tasks = completed_tasks

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
        if issubclass(EngineTaskStatusCumulative, dict):
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
        if not isinstance(other, EngineTaskStatusCumulative):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
