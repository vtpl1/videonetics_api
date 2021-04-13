# EventDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine_task_id** | **str** | _id of engineTasks #$ref: &#x27;#/components/schemas/engineTasks&#x27; | [optional] 
**start_time_stamp** | **int** | Event start timestamp in Unix epoch milliseconds | [optional] 
**end_time_stamp** | **int** | Event end timestamp in Unix epoch milliseconds | [optional] 
**zone_id** | **int** | the zoneId of the engineTask in zoneSetting, #$ref: &#x27;#/components/schemas/zone&#x27; | [optional] [default to 0]
**confidence** | **float** | match confidence predicted by engine during event detection | [optional] [default to 0]
**capture_time_in_video** | **int** | Event timestamp in video in Unix epoch milliseconds | [optional] 
**extras** | [**list[Extra]**](Extra.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

