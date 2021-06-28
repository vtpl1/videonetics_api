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

class Event(object):
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
        'user_id': 'str',
        'capbilities_type': 'Capability',
        'event_type': 'EventType',
        'event_details': 'EventDetails',
        'event_snaps': 'list[str]',
        'event_clips': 'list[str]',
        'updated': 'datetime',
        'created': 'datetime',
        'etag': 'str',
        'links': 'Links'
    }

    attribute_map = {
        'id': '_id',
        'user_id': 'userId',
        'capbilities_type': 'capbilitiesType',
        'event_type': 'eventType',
        'event_details': 'eventDetails',
        'event_snaps': 'eventSnaps',
        'event_clips': 'eventClips',
        'updated': 'updated',
        'created': 'created',
        'etag': 'etag',
        'links': 'links'
    }

    discriminator_value_class_map = {
          'attributeEvent': 'AttributeEvent',
'anprEvent': 'AnprEvent',
'vaEvent': 'VaEvent'    }

    def __init__(self, id=None, user_id=None, capbilities_type=None, event_type=None, event_details=None, event_snaps=None, event_clips=None, updated=None, created=None, etag=None, links=None):  # noqa: E501
        """Event - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._user_id = None
        self._capbilities_type = None
        self._event_type = None
        self._event_details = None
        self._event_snaps = None
        self._event_clips = None
        self._updated = None
        self._created = None
        self._etag = None
        self._links = None
        self.discriminator = 'eventType'
        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if capbilities_type is not None:
            self.capbilities_type = capbilities_type
        if event_type is not None:
            self.event_type = event_type
        if event_details is not None:
            self.event_details = event_details
        if event_snaps is not None:
            self.event_snaps = event_snaps
        if event_clips is not None:
            self.event_clips = event_clips
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
        """Gets the id of this Event.  # noqa: E501


        :return: The id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Event.


        :param id: The id of this Event.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this Event.  # noqa: E501


        :return: The user_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Event.


        :param user_id: The user_id of this Event.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def capbilities_type(self):
        """Gets the capbilities_type of this Event.  # noqa: E501


        :return: The capbilities_type of this Event.  # noqa: E501
        :rtype: Capability
        """
        return self._capbilities_type

    @capbilities_type.setter
    def capbilities_type(self, capbilities_type):
        """Sets the capbilities_type of this Event.


        :param capbilities_type: The capbilities_type of this Event.  # noqa: E501
        :type: Capability
        """

        self._capbilities_type = capbilities_type

    @property
    def event_type(self):
        """Gets the event_type of this Event.  # noqa: E501


        :return: The event_type of this Event.  # noqa: E501
        :rtype: EventType
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Event.


        :param event_type: The event_type of this Event.  # noqa: E501
        :type: EventType
        """

        self._event_type = event_type

    @property
    def event_details(self):
        """Gets the event_details of this Event.  # noqa: E501


        :return: The event_details of this Event.  # noqa: E501
        :rtype: EventDetails
        """
        return self._event_details

    @event_details.setter
    def event_details(self, event_details):
        """Sets the event_details of this Event.


        :param event_details: The event_details of this Event.  # noqa: E501
        :type: EventDetails
        """

        self._event_details = event_details

    @property
    def event_snaps(self):
        """Gets the event_snaps of this Event.  # noqa: E501

        _id of snap from #$ref: '#/components/schemas/snap'  # noqa: E501

        :return: The event_snaps of this Event.  # noqa: E501
        :rtype: list[str]
        """
        return self._event_snaps

    @event_snaps.setter
    def event_snaps(self, event_snaps):
        """Sets the event_snaps of this Event.

        _id of snap from #$ref: '#/components/schemas/snap'  # noqa: E501

        :param event_snaps: The event_snaps of this Event.  # noqa: E501
        :type: list[str]
        """

        self._event_snaps = event_snaps

    @property
    def event_clips(self):
        """Gets the event_clips of this Event.  # noqa: E501

        _id of snap from #$ref: '#/components/schemas/clip'  # noqa: E501

        :return: The event_clips of this Event.  # noqa: E501
        :rtype: list[str]
        """
        return self._event_clips

    @event_clips.setter
    def event_clips(self, event_clips):
        """Sets the event_clips of this Event.

        _id of snap from #$ref: '#/components/schemas/clip'  # noqa: E501

        :param event_clips: The event_clips of this Event.  # noqa: E501
        :type: list[str]
        """

        self._event_clips = event_clips

    @property
    def updated(self):
        """Gets the updated of this Event.  # noqa: E501


        :return: The updated of this Event.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Event.


        :param updated: The updated of this Event.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this Event.  # noqa: E501


        :return: The created of this Event.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Event.


        :param created: The created of this Event.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def etag(self):
        """Gets the etag of this Event.  # noqa: E501


        :return: The etag of this Event.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this Event.


        :param etag: The etag of this Event.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def links(self):
        """Gets the links of this Event.  # noqa: E501


        :return: The links of this Event.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Event.


        :param links: The links of this Event.  # noqa: E501
        :type: Links
        """

        self._links = links

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(Event, dict):
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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
