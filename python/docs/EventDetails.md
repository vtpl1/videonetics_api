# EventDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**camera_id** | **str** | _id of camera #$ref: &#x27;#/components/schemas/camera&#x27; from project cameras | [optional] 
**camera_ip** | **str** |  | [optional] 
**camera_name** | **str** |  | [optional] 
**is_valid** | **bool** | If event validated by operator/admin | [optional] [default to False]
**is_restricted** | **bool** | If event validated by operator/admin | [optional] [default to True]
**source_id** | **str** | _id of camera #$ref: &#x27;#/components/schemas/camera&#x27; from project cameras | [optional] 
**engine_task_id** | **str** | _id of engineTasks #$ref: &#x27;#/components/schemas/engineTasks&#x27; | [optional] 
**zone_id** | **int** | the zoneId of the engineTask in zoneSetting, #$ref: &#x27;#/components/schemas/zone&#x27; | [optional] [default to 0]
**confidence** | **float** | match confidence predicted by engine during event detection | [optional] [default to 0]
**start_time_stamp** | **int** | Event start timestamp in Unix epoch milliseconds | [optional] 
**end_time_stamp** | **int** | Event end timestamp in Unix epoch milliseconds | [optional] 
**video_file_name** | **str** | Video file name if it is present | [optional] 
**capture_time_in_video** | **int** | Event timestamp in video in Unix epoch milliseconds | [optional] [default to -1]
**gdpr_enabled** | **bool** | If gdpr enabled by admin | [optional] [default to False]
**latitude** | **float** |  | [optional] [default to 0]
**longitude** | **float** |  | [optional] [default to 0]
**extras** | [**list[Extra]**](Extra.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

