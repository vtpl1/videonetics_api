# MetaAnprEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_plate_information** | [**LicensePlateDetails**](LicensePlateDetails.md) |  | [optional] 
**vehicle_type** | [**VehicleType**](VehicleType.md) |  | [optional] 
**vehicle_color** | [**Color**](Color.md) |  | [optional] 
**speed** | **float** |  | [optional] 
**is_wrong_lane** | **bool** |  | [optional] [default to False]
**is_wrong_way** | **bool** |  | [optional] [default to False]
**is_wrong_turn** | **bool** |  | [optional] [default to False]
**is_red_light_violation** | **bool** |  | [optional] [default to False]
**is_stop_light_violation** | **bool** |  | [optional] [default to False]
**vehicle_make** | **str** |  | [optional] 
**vehicle_model** | **str** |  | [optional] 
**driver_on_call_rectangle** | [**ObjectRectWithTimeStampAndEventSnapReference**](ObjectRectWithTimeStampAndEventSnapReference.md) |  | [optional] 
**no_seat_belt_rectangles** | [**list[ObjectRectWithTimeStampAndEventSnapReference]**](ObjectRectWithTimeStampAndEventSnapReference.md) |  | [optional] 
**passenger_no_seat_belt_rectangles** | [**list[ObjectRectWithTimeStampAndEventSnapReference]**](ObjectRectWithTimeStampAndEventSnapReference.md) |  | [optional] 
**no_helmet_rectangles** | [**list[ObjectRectWithTimeStampAndEventSnapReference]**](ObjectRectWithTimeStampAndEventSnapReference.md) |  | [optional] 
**triple_ride_rectangles** | [**ObjectRectWithTimeStampAndEventSnapReference**](ObjectRectWithTimeStampAndEventSnapReference.md) |  | [optional] 
**pillion_ride_rectangles** | [**list[ObjectRectWithTimeStampAndEventSnapReference]**](ObjectRectWithTimeStampAndEventSnapReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

