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

class MetaAnprEvent(object):
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
        'license_plate_information': 'LicensePlateDetails',
        'vehicle_type': 'VehicleType',
        'vehicle_color': 'Color',
        'speed': 'float',
        'is_wrong_lane': 'bool',
        'is_wrong_way': 'bool',
        'is_wrong_turn': 'bool',
        'is_red_light_violation': 'bool',
        'is_stop_light_violation': 'bool',
        'vehicle_make': 'str',
        'vehicle_model': 'str',
        'driver_on_call_rectangle': 'ObjectRectWithTimeStampAndEventSnapReference',
        'no_seat_belt_rectangles': 'list[ObjectRectWithTimeStampAndEventSnapReference]',
        'passenger_no_seat_belt_rectangles': 'list[ObjectRectWithTimeStampAndEventSnapReference]',
        'no_helmet_rectangles': 'list[ObjectRectWithTimeStampAndEventSnapReference]',
        'triple_ride_rectangles': 'ObjectRectWithTimeStampAndEventSnapReference',
        'pillion_ride_rectangles': 'list[ObjectRectWithTimeStampAndEventSnapReference]'
    }

    attribute_map = {
        'license_plate_information': 'licensePlateInformation',
        'vehicle_type': 'vehicleType',
        'vehicle_color': 'vehicleColor',
        'speed': 'speed',
        'is_wrong_lane': 'isWrongLane',
        'is_wrong_way': 'isWrongWay',
        'is_wrong_turn': 'isWrongTurn',
        'is_red_light_violation': 'isRedLightViolation',
        'is_stop_light_violation': 'isStopLightViolation',
        'vehicle_make': 'vehicleMake',
        'vehicle_model': 'vehicleModel',
        'driver_on_call_rectangle': 'driverOnCallRectangle',
        'no_seat_belt_rectangles': 'noSeatBeltRectangles',
        'passenger_no_seat_belt_rectangles': 'passengerNoSeatBeltRectangles',
        'no_helmet_rectangles': 'noHelmetRectangles',
        'triple_ride_rectangles': 'tripleRideRectangles',
        'pillion_ride_rectangles': 'pillionRideRectangles'
    }

    def __init__(self, license_plate_information=None, vehicle_type=None, vehicle_color=None, speed=None, is_wrong_lane=False, is_wrong_way=False, is_wrong_turn=False, is_red_light_violation=False, is_stop_light_violation=False, vehicle_make=None, vehicle_model=None, driver_on_call_rectangle=None, no_seat_belt_rectangles=None, passenger_no_seat_belt_rectangles=None, no_helmet_rectangles=None, triple_ride_rectangles=None, pillion_ride_rectangles=None):  # noqa: E501
        """MetaAnprEvent - a model defined in Swagger"""  # noqa: E501
        self._license_plate_information = None
        self._vehicle_type = None
        self._vehicle_color = None
        self._speed = None
        self._is_wrong_lane = None
        self._is_wrong_way = None
        self._is_wrong_turn = None
        self._is_red_light_violation = None
        self._is_stop_light_violation = None
        self._vehicle_make = None
        self._vehicle_model = None
        self._driver_on_call_rectangle = None
        self._no_seat_belt_rectangles = None
        self._passenger_no_seat_belt_rectangles = None
        self._no_helmet_rectangles = None
        self._triple_ride_rectangles = None
        self._pillion_ride_rectangles = None
        self.discriminator = None
        if license_plate_information is not None:
            self.license_plate_information = license_plate_information
        if vehicle_type is not None:
            self.vehicle_type = vehicle_type
        if vehicle_color is not None:
            self.vehicle_color = vehicle_color
        if speed is not None:
            self.speed = speed
        if is_wrong_lane is not None:
            self.is_wrong_lane = is_wrong_lane
        if is_wrong_way is not None:
            self.is_wrong_way = is_wrong_way
        if is_wrong_turn is not None:
            self.is_wrong_turn = is_wrong_turn
        if is_red_light_violation is not None:
            self.is_red_light_violation = is_red_light_violation
        if is_stop_light_violation is not None:
            self.is_stop_light_violation = is_stop_light_violation
        if vehicle_make is not None:
            self.vehicle_make = vehicle_make
        if vehicle_model is not None:
            self.vehicle_model = vehicle_model
        if driver_on_call_rectangle is not None:
            self.driver_on_call_rectangle = driver_on_call_rectangle
        if no_seat_belt_rectangles is not None:
            self.no_seat_belt_rectangles = no_seat_belt_rectangles
        if passenger_no_seat_belt_rectangles is not None:
            self.passenger_no_seat_belt_rectangles = passenger_no_seat_belt_rectangles
        if no_helmet_rectangles is not None:
            self.no_helmet_rectangles = no_helmet_rectangles
        if triple_ride_rectangles is not None:
            self.triple_ride_rectangles = triple_ride_rectangles
        if pillion_ride_rectangles is not None:
            self.pillion_ride_rectangles = pillion_ride_rectangles

    @property
    def license_plate_information(self):
        """Gets the license_plate_information of this MetaAnprEvent.  # noqa: E501


        :return: The license_plate_information of this MetaAnprEvent.  # noqa: E501
        :rtype: LicensePlateDetails
        """
        return self._license_plate_information

    @license_plate_information.setter
    def license_plate_information(self, license_plate_information):
        """Sets the license_plate_information of this MetaAnprEvent.


        :param license_plate_information: The license_plate_information of this MetaAnprEvent.  # noqa: E501
        :type: LicensePlateDetails
        """

        self._license_plate_information = license_plate_information

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this MetaAnprEvent.  # noqa: E501


        :return: The vehicle_type of this MetaAnprEvent.  # noqa: E501
        :rtype: VehicleType
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this MetaAnprEvent.


        :param vehicle_type: The vehicle_type of this MetaAnprEvent.  # noqa: E501
        :type: VehicleType
        """

        self._vehicle_type = vehicle_type

    @property
    def vehicle_color(self):
        """Gets the vehicle_color of this MetaAnprEvent.  # noqa: E501


        :return: The vehicle_color of this MetaAnprEvent.  # noqa: E501
        :rtype: Color
        """
        return self._vehicle_color

    @vehicle_color.setter
    def vehicle_color(self, vehicle_color):
        """Sets the vehicle_color of this MetaAnprEvent.


        :param vehicle_color: The vehicle_color of this MetaAnprEvent.  # noqa: E501
        :type: Color
        """

        self._vehicle_color = vehicle_color

    @property
    def speed(self):
        """Gets the speed of this MetaAnprEvent.  # noqa: E501


        :return: The speed of this MetaAnprEvent.  # noqa: E501
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this MetaAnprEvent.


        :param speed: The speed of this MetaAnprEvent.  # noqa: E501
        :type: float
        """

        self._speed = speed

    @property
    def is_wrong_lane(self):
        """Gets the is_wrong_lane of this MetaAnprEvent.  # noqa: E501


        :return: The is_wrong_lane of this MetaAnprEvent.  # noqa: E501
        :rtype: bool
        """
        return self._is_wrong_lane

    @is_wrong_lane.setter
    def is_wrong_lane(self, is_wrong_lane):
        """Sets the is_wrong_lane of this MetaAnprEvent.


        :param is_wrong_lane: The is_wrong_lane of this MetaAnprEvent.  # noqa: E501
        :type: bool
        """

        self._is_wrong_lane = is_wrong_lane

    @property
    def is_wrong_way(self):
        """Gets the is_wrong_way of this MetaAnprEvent.  # noqa: E501


        :return: The is_wrong_way of this MetaAnprEvent.  # noqa: E501
        :rtype: bool
        """
        return self._is_wrong_way

    @is_wrong_way.setter
    def is_wrong_way(self, is_wrong_way):
        """Sets the is_wrong_way of this MetaAnprEvent.


        :param is_wrong_way: The is_wrong_way of this MetaAnprEvent.  # noqa: E501
        :type: bool
        """

        self._is_wrong_way = is_wrong_way

    @property
    def is_wrong_turn(self):
        """Gets the is_wrong_turn of this MetaAnprEvent.  # noqa: E501


        :return: The is_wrong_turn of this MetaAnprEvent.  # noqa: E501
        :rtype: bool
        """
        return self._is_wrong_turn

    @is_wrong_turn.setter
    def is_wrong_turn(self, is_wrong_turn):
        """Sets the is_wrong_turn of this MetaAnprEvent.


        :param is_wrong_turn: The is_wrong_turn of this MetaAnprEvent.  # noqa: E501
        :type: bool
        """

        self._is_wrong_turn = is_wrong_turn

    @property
    def is_red_light_violation(self):
        """Gets the is_red_light_violation of this MetaAnprEvent.  # noqa: E501


        :return: The is_red_light_violation of this MetaAnprEvent.  # noqa: E501
        :rtype: bool
        """
        return self._is_red_light_violation

    @is_red_light_violation.setter
    def is_red_light_violation(self, is_red_light_violation):
        """Sets the is_red_light_violation of this MetaAnprEvent.


        :param is_red_light_violation: The is_red_light_violation of this MetaAnprEvent.  # noqa: E501
        :type: bool
        """

        self._is_red_light_violation = is_red_light_violation

    @property
    def is_stop_light_violation(self):
        """Gets the is_stop_light_violation of this MetaAnprEvent.  # noqa: E501


        :return: The is_stop_light_violation of this MetaAnprEvent.  # noqa: E501
        :rtype: bool
        """
        return self._is_stop_light_violation

    @is_stop_light_violation.setter
    def is_stop_light_violation(self, is_stop_light_violation):
        """Sets the is_stop_light_violation of this MetaAnprEvent.


        :param is_stop_light_violation: The is_stop_light_violation of this MetaAnprEvent.  # noqa: E501
        :type: bool
        """

        self._is_stop_light_violation = is_stop_light_violation

    @property
    def vehicle_make(self):
        """Gets the vehicle_make of this MetaAnprEvent.  # noqa: E501


        :return: The vehicle_make of this MetaAnprEvent.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_make

    @vehicle_make.setter
    def vehicle_make(self, vehicle_make):
        """Sets the vehicle_make of this MetaAnprEvent.


        :param vehicle_make: The vehicle_make of this MetaAnprEvent.  # noqa: E501
        :type: str
        """

        self._vehicle_make = vehicle_make

    @property
    def vehicle_model(self):
        """Gets the vehicle_model of this MetaAnprEvent.  # noqa: E501


        :return: The vehicle_model of this MetaAnprEvent.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_model

    @vehicle_model.setter
    def vehicle_model(self, vehicle_model):
        """Sets the vehicle_model of this MetaAnprEvent.


        :param vehicle_model: The vehicle_model of this MetaAnprEvent.  # noqa: E501
        :type: str
        """

        self._vehicle_model = vehicle_model

    @property
    def driver_on_call_rectangle(self):
        """Gets the driver_on_call_rectangle of this MetaAnprEvent.  # noqa: E501


        :return: The driver_on_call_rectangle of this MetaAnprEvent.  # noqa: E501
        :rtype: ObjectRectWithTimeStampAndEventSnapReference
        """
        return self._driver_on_call_rectangle

    @driver_on_call_rectangle.setter
    def driver_on_call_rectangle(self, driver_on_call_rectangle):
        """Sets the driver_on_call_rectangle of this MetaAnprEvent.


        :param driver_on_call_rectangle: The driver_on_call_rectangle of this MetaAnprEvent.  # noqa: E501
        :type: ObjectRectWithTimeStampAndEventSnapReference
        """

        self._driver_on_call_rectangle = driver_on_call_rectangle

    @property
    def no_seat_belt_rectangles(self):
        """Gets the no_seat_belt_rectangles of this MetaAnprEvent.  # noqa: E501


        :return: The no_seat_belt_rectangles of this MetaAnprEvent.  # noqa: E501
        :rtype: list[ObjectRectWithTimeStampAndEventSnapReference]
        """
        return self._no_seat_belt_rectangles

    @no_seat_belt_rectangles.setter
    def no_seat_belt_rectangles(self, no_seat_belt_rectangles):
        """Sets the no_seat_belt_rectangles of this MetaAnprEvent.


        :param no_seat_belt_rectangles: The no_seat_belt_rectangles of this MetaAnprEvent.  # noqa: E501
        :type: list[ObjectRectWithTimeStampAndEventSnapReference]
        """

        self._no_seat_belt_rectangles = no_seat_belt_rectangles

    @property
    def passenger_no_seat_belt_rectangles(self):
        """Gets the passenger_no_seat_belt_rectangles of this MetaAnprEvent.  # noqa: E501


        :return: The passenger_no_seat_belt_rectangles of this MetaAnprEvent.  # noqa: E501
        :rtype: list[ObjectRectWithTimeStampAndEventSnapReference]
        """
        return self._passenger_no_seat_belt_rectangles

    @passenger_no_seat_belt_rectangles.setter
    def passenger_no_seat_belt_rectangles(self, passenger_no_seat_belt_rectangles):
        """Sets the passenger_no_seat_belt_rectangles of this MetaAnprEvent.


        :param passenger_no_seat_belt_rectangles: The passenger_no_seat_belt_rectangles of this MetaAnprEvent.  # noqa: E501
        :type: list[ObjectRectWithTimeStampAndEventSnapReference]
        """

        self._passenger_no_seat_belt_rectangles = passenger_no_seat_belt_rectangles

    @property
    def no_helmet_rectangles(self):
        """Gets the no_helmet_rectangles of this MetaAnprEvent.  # noqa: E501


        :return: The no_helmet_rectangles of this MetaAnprEvent.  # noqa: E501
        :rtype: list[ObjectRectWithTimeStampAndEventSnapReference]
        """
        return self._no_helmet_rectangles

    @no_helmet_rectangles.setter
    def no_helmet_rectangles(self, no_helmet_rectangles):
        """Sets the no_helmet_rectangles of this MetaAnprEvent.


        :param no_helmet_rectangles: The no_helmet_rectangles of this MetaAnprEvent.  # noqa: E501
        :type: list[ObjectRectWithTimeStampAndEventSnapReference]
        """

        self._no_helmet_rectangles = no_helmet_rectangles

    @property
    def triple_ride_rectangles(self):
        """Gets the triple_ride_rectangles of this MetaAnprEvent.  # noqa: E501


        :return: The triple_ride_rectangles of this MetaAnprEvent.  # noqa: E501
        :rtype: ObjectRectWithTimeStampAndEventSnapReference
        """
        return self._triple_ride_rectangles

    @triple_ride_rectangles.setter
    def triple_ride_rectangles(self, triple_ride_rectangles):
        """Sets the triple_ride_rectangles of this MetaAnprEvent.


        :param triple_ride_rectangles: The triple_ride_rectangles of this MetaAnprEvent.  # noqa: E501
        :type: ObjectRectWithTimeStampAndEventSnapReference
        """

        self._triple_ride_rectangles = triple_ride_rectangles

    @property
    def pillion_ride_rectangles(self):
        """Gets the pillion_ride_rectangles of this MetaAnprEvent.  # noqa: E501


        :return: The pillion_ride_rectangles of this MetaAnprEvent.  # noqa: E501
        :rtype: list[ObjectRectWithTimeStampAndEventSnapReference]
        """
        return self._pillion_ride_rectangles

    @pillion_ride_rectangles.setter
    def pillion_ride_rectangles(self, pillion_ride_rectangles):
        """Sets the pillion_ride_rectangles of this MetaAnprEvent.


        :param pillion_ride_rectangles: The pillion_ride_rectangles of this MetaAnprEvent.  # noqa: E501
        :type: list[ObjectRectWithTimeStampAndEventSnapReference]
        """

        self._pillion_ride_rectangles = pillion_ride_rectangles

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
        if issubclass(MetaAnprEvent, dict):
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
        if not isinstance(other, MetaAnprEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
