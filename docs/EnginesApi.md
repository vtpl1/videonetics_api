# swagger_client.EnginesApi

All URIs are relative to *http://v2.videonetics.com:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anpr_events_get**](EnginesApi.md#anpr_events_get) | **GET** /anprEvents | Get all anprEvents
[**anpr_events_id_delete**](EnginesApi.md#anpr_events_id_delete) | **DELETE** /anprEvents/{id} | Delete an event
[**anpr_events_id_get**](EnginesApi.md#anpr_events_id_get) | **GET** /anprEvents/{id} | Get anprEvent by id
[**anpr_events_id_patch**](EnginesApi.md#anpr_events_id_patch) | **PATCH** /anprEvents/{id} | Patch
[**anpr_events_post**](EnginesApi.md#anpr_events_post) | **POST** /anprEvents | Create an anprEvent
[**attribute_events_get**](EnginesApi.md#attribute_events_get) | **GET** /attributeEvents | Get all attributeEvents
[**attribute_events_id_delete**](EnginesApi.md#attribute_events_id_delete) | **DELETE** /attributeEvents/{id} | Delete an event
[**attribute_events_id_get**](EnginesApi.md#attribute_events_id_get) | **GET** /attributeEvents/{id} | Get attributeEvent by id
[**attribute_events_id_patch**](EnginesApi.md#attribute_events_id_patch) | **PATCH** /attributeEvents/{id} | Patch
[**attribute_events_post**](EnginesApi.md#attribute_events_post) | **POST** /attributeEvents | Create an attributeEvent
[**clips_get**](EnginesApi.md#clips_get) | **GET** /clips | Get all unprocesed clips
[**clips_id_get**](EnginesApi.md#clips_id_get) | **GET** /clips/{id} | Get clip by id
[**clips_post**](EnginesApi.md#clips_post) | **POST** /clips | Create an unprocesed clip
[**engine_task_status_cumulative_get**](EnginesApi.md#engine_task_status_cumulative_get) | **GET** /engineTaskStatusCumulative | Get task status response
[**engine_task_status_get**](EnginesApi.md#engine_task_status_get) | **GET** /engineTaskStatus | Get all engineTaskStatus
[**engine_task_status_id_delete**](EnginesApi.md#engine_task_status_id_delete) | **DELETE** /engineTaskStatus/{id} | Delete an engineTaskStatus
[**engine_task_status_id_get**](EnginesApi.md#engine_task_status_id_get) | **GET** /engineTaskStatus/{id} | Get engineTaskStatus by id
[**engine_task_status_id_patch**](EnginesApi.md#engine_task_status_id_patch) | **PATCH** /engineTaskStatus/{id} | Patch an engineTaskStatus
[**engine_task_status_post**](EnginesApi.md#engine_task_status_post) | **POST** /engineTaskStatus | Create an engineTaskStatus
[**engine_tasks_get**](EnginesApi.md#engine_tasks_get) | **GET** /engineTasks | Get all engineTasks
[**engine_tasks_id_delete**](EnginesApi.md#engine_tasks_id_delete) | **DELETE** /engineTasks/{id} | Delete an engine task
[**engine_tasks_id_get**](EnginesApi.md#engine_tasks_id_get) | **GET** /engineTasks/{id} | Get engine task by id
[**engine_tasks_id_patch**](EnginesApi.md#engine_tasks_id_patch) | **PATCH** /engineTasks/{id} | Patch an engine task
[**engine_tasks_post**](EnginesApi.md#engine_tasks_post) | **POST** /engineTasks | Create an engineTask
[**engines_get**](EnginesApi.md#engines_get) | **GET** /engines | Get all engine details
[**engines_id_delete**](EnginesApi.md#engines_id_delete) | **DELETE** /engines/{id} | Delete an engine
[**engines_id_get**](EnginesApi.md#engines_id_get) | **GET** /engines/{id} | Get engine by id
[**engines_id_patch**](EnginesApi.md#engines_id_patch) | **PATCH** /engines/{id} | Patch
[**engines_post**](EnginesApi.md#engines_post) | **POST** /engines | Create an engine
[**event_snaps_get**](EnginesApi.md#event_snaps_get) | **GET** /eventSnaps | Get all eventSnaps
[**event_snaps_id_get**](EnginesApi.md#event_snaps_id_get) | **GET** /eventSnaps/{id} | Get eventSnap by id
[**event_snaps_post**](EnginesApi.md#event_snaps_post) | **POST** /eventSnaps | Create an eventSnap
[**inferencers_get**](EnginesApi.md#inferencers_get) | **GET** /inferencers | Get all inferencers details
[**inferencers_id_delete**](EnginesApi.md#inferencers_id_delete) | **DELETE** /inferencers/{id} | Delete an inferencer
[**inferencers_id_get**](EnginesApi.md#inferencers_id_get) | **GET** /inferencers/{id} | Get inferencer by id
[**inferencers_id_patch**](EnginesApi.md#inferencers_id_patch) | **PATCH** /inferencers/{id} | Patch
[**inferencers_post**](EnginesApi.md#inferencers_post) | **POST** /inferencers | Create an inferencer
[**media_sources_get**](EnginesApi.md#media_sources_get) | **GET** /mediaSources | Get all media sources
[**media_sources_id_delete**](EnginesApi.md#media_sources_id_delete) | **DELETE** /mediaSources/{id} | Delete a media source
[**media_sources_id_get**](EnginesApi.md#media_sources_id_get) | **GET** /mediaSources/{id} | Get media source by id
[**media_sources_id_patch**](EnginesApi.md#media_sources_id_patch) | **PATCH** /mediaSources/{id} | Patch
[**media_sources_post**](EnginesApi.md#media_sources_post) | **POST** /mediaSources | Create a media source
[**motion_detectors_get**](EnginesApi.md#motion_detectors_get) | **GET** /motionDetectors | Get all motionDetectors details
[**motion_detectors_id_delete**](EnginesApi.md#motion_detectors_id_delete) | **DELETE** /motionDetectors/{id} | Delete an motionDetector
[**motion_detectors_id_get**](EnginesApi.md#motion_detectors_id_get) | **GET** /motionDetectors/{id} | Get motionDetector by id
[**motion_detectors_id_patch**](EnginesApi.md#motion_detectors_id_patch) | **PATCH** /motionDetectors/{id} | Patch
[**motion_detectors_post**](EnginesApi.md#motion_detectors_post) | **POST** /motionDetectors | Create an motionDetector
[**pipelines_get**](EnginesApi.md#pipelines_get) | **GET** /pipelines | Get all pipelines details
[**pipelines_id_delete**](EnginesApi.md#pipelines_id_delete) | **DELETE** /pipelines/{id} | Delete an pipeline
[**pipelines_id_get**](EnginesApi.md#pipelines_id_get) | **GET** /pipelines/{id} | Get pipeline by id
[**pipelines_id_patch**](EnginesApi.md#pipelines_id_patch) | **PATCH** /pipelines/{id} | Patch
[**pipelines_post**](EnginesApi.md#pipelines_post) | **POST** /pipelines | Create an pipeline
[**pre_processes_get**](EnginesApi.md#pre_processes_get) | **GET** /preProcesses | Get all preProcesses details
[**pre_processes_id_delete**](EnginesApi.md#pre_processes_id_delete) | **DELETE** /preProcesses/{id} | Delete an preProcess
[**pre_processes_id_get**](EnginesApi.md#pre_processes_id_get) | **GET** /preProcesses/{id} | Get preProcess by id
[**pre_processes_id_patch**](EnginesApi.md#pre_processes_id_patch) | **PATCH** /preProcesses/{id} | Patch
[**pre_processes_post**](EnginesApi.md#pre_processes_post) | **POST** /preProcesses | Create an preProcess
[**precis_engine_task_status_get**](EnginesApi.md#precis_engine_task_status_get) | **GET** /precisEngineTaskStatus | Get all precisEngineTaskStatus
[**precis_engine_task_status_id_delete**](EnginesApi.md#precis_engine_task_status_id_delete) | **DELETE** /precisEngineTaskStatus/{id} | Delete an precisEngineTaskStatus
[**precis_engine_task_status_id_get**](EnginesApi.md#precis_engine_task_status_id_get) | **GET** /precisEngineTaskStatus/{id} | Get precisEngineTaskStatus by id
[**precis_engine_task_status_id_patch**](EnginesApi.md#precis_engine_task_status_id_patch) | **PATCH** /precisEngineTaskStatus/{id} | Patch an precisEngineTaskStatus
[**precis_engine_task_status_post**](EnginesApi.md#precis_engine_task_status_post) | **POST** /precisEngineTaskStatus | Create an precisEngineTaskStatus
[**precis_engine_tasks_get**](EnginesApi.md#precis_engine_tasks_get) | **GET** /precisEngineTasks | Get all precisEngineTasks
[**precis_engine_tasks_id_delete**](EnginesApi.md#precis_engine_tasks_id_delete) | **DELETE** /precisEngineTasks/{id} | Delete an precis engine task
[**precis_engine_tasks_id_get**](EnginesApi.md#precis_engine_tasks_id_get) | **GET** /precisEngineTasks/{id} | Get precis engine task by id
[**precis_engine_tasks_id_patch**](EnginesApi.md#precis_engine_tasks_id_patch) | **PATCH** /precisEngineTasks/{id} | Patch an precis engine task
[**precis_engine_tasks_post**](EnginesApi.md#precis_engine_tasks_post) | **POST** /precisEngineTasks | Create an precisEngineTasks
[**snaps_get**](EnginesApi.md#snaps_get) | **GET** /snaps | Get all unprocesed snaps
[**snaps_id_get**](EnginesApi.md#snaps_id_get) | **GET** /snaps/{id} | Get snap by id
[**snaps_post**](EnginesApi.md#snaps_post) | **POST** /snaps | Create a unprocesed snap
[**va_events_get**](EnginesApi.md#va_events_get) | **GET** /vaEvents | Get all vaEvents
[**va_events_id_delete**](EnginesApi.md#va_events_id_delete) | **DELETE** /vaEvents/{id} | Delete an event
[**va_events_id_get**](EnginesApi.md#va_events_id_get) | **GET** /vaEvents/{id} | Get vaEvent by id
[**va_events_id_patch**](EnginesApi.md#va_events_id_patch) | **PATCH** /vaEvents/{id} | Patch
[**va_events_post**](EnginesApi.md#va_events_post) | **POST** /vaEvents | Create an vaEvent

# **anpr_events_get**
> AnprEventsResponse anpr_events_get(where=where, page=page, sort=sort, max_results=max_results, embedded=embedded)

Get all anprEvents

Get all anprEvents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the anprEvent model. Example:   * To find anprEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /anprEvents?where={\"eventDetails.engineTaskId\":\"5c1956e925b6b30001103eaa\"}   * To find anprEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /anprEvents?where={\"eventDetails.engineTaskId\":\"5c1956e925b6b30001103eaa\",\"eventDetails.sourceId\":\"5c1956e925b6b30001103eab\"} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /anprEvents?page=4 (optional)
sort = 'sort_example' # str | The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort anprEvents by startTimeStamp in eventDetails IN ASCEDING order, use /anprEvents?sort=eventDetails.startTimeStamp   * To sort anprEvents by startTimeStamp in eventDetails IN DECENDING order, use /anprEvents?sort=-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest anprEvent among whole anprEvents, use /anprEvents?maxResults=1   * To limit anprEvents to 5, use /anprEvents?maxResults=5 (optional)
embedded = 'embedded_example' # str | The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * 'To find anprEvents with eventSnap object. use /anprEvents?embedded={\"eventSnaps\":1}' (optional)

try:
    # Get all anprEvents
    api_response = api_instance.anpr_events_get(where=where, page=page, sort=sort, max_results=max_results, embedded=embedded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->anpr_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the anprEvent model. Example:   * To find anprEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /anprEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;}   * To find anprEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /anprEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;,\&quot;eventDetails.sourceId\&quot;:\&quot;5c1956e925b6b30001103eab\&quot;} | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /anprEvents?page&#x3D;4 | [optional] 
 **sort** | **str**| The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort anprEvents by startTimeStamp in eventDetails IN ASCEDING order, use /anprEvents?sort&#x3D;eventDetails.startTimeStamp   * To sort anprEvents by startTimeStamp in eventDetails IN DECENDING order, use /anprEvents?sort&#x3D;-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest anprEvent among whole anprEvents, use /anprEvents?maxResults&#x3D;1   * To limit anprEvents to 5, use /anprEvents?maxResults&#x3D;5 | [optional] 
 **embedded** | **str**| The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find anprEvents with eventSnap object. use /anprEvents?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27; | [optional] 

### Return type

[**AnprEventsResponse**](AnprEventsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **anpr_events_id_delete**
> anpr_events_id_delete(id, if_match)

Delete an event

Delete an anprEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete an event
    api_instance.anpr_events_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->anpr_events_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **anpr_events_id_get**
> AnprEvent anpr_events_id_get(id, embedded=embedded)

Get anprEvent by id

Get anprEvent by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
embedded = 'embedded_example' # str | The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * 'To find anprEvents with eventSnap object. use /anprEvents/{id}?embedded={\"eventSnaps\":1}' (optional)

try:
    # Get anprEvent by id
    api_response = api_instance.anpr_events_id_get(id, embedded=embedded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->anpr_events_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **embedded** | **str**| The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find anprEvents with eventSnap object. use /anprEvents/{id}?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27; | [optional] 

### Return type

[**AnprEvent**](AnprEvent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **anpr_events_id_patch**
> DefaultResponse anpr_events_id_patch(if_match, id, body=body)

Patch

Patch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.AnprEvent() # AnprEvent |  (optional)

try:
    # Patch
    api_response = api_instance.anpr_events_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->anpr_events_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**AnprEvent**](AnprEvent.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **anpr_events_post**
> DefaultResponse anpr_events_post(body=body)

Create an anprEvent

Create an anprEvent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AnprEvent() # AnprEvent |  (optional)

try:
    # Create an anprEvent
    api_response = api_instance.anpr_events_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->anpr_events_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnprEvent**](AnprEvent.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_events_get**
> AttributeEventsResponse attribute_events_get(where=where, page=page, sort=sort, max_results=max_results, embedded=embedded)

Get all attributeEvents

Get all attributeEvents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the attributeEvent model. Example:   * To find attributeEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /attributeEvents?where={\"eventDetails.engineTaskId\":\"5c1956e925b6b30001103eaa\"}   * To find attributeEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /attributeEvents?where={\"eventDetails.engineTaskId\":\"5c1956e925b6b30001103eaa\",\"eventDetails.sourceId\":\"5c1956e925b6b30001103eab\"} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /attributeEvents?page=4 (optional)
sort = 'sort_example' # str | The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort attributeEvents by startTimeStamp in eventDetails IN ASCEDING order, use /attributeEvents?sort=eventDetails.startTimeStamp   * To sort attributeEvents by startTimeStamp in eventDetails IN DECENDING order, use /attributeEvents?sort=-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest attributeEvent among whole attributeEvents, use /attributeEvents?maxResults=1   * To limit attributeEvents to 5, use /attributeEvents?maxResults=5 (optional)
embedded = 'embedded_example' # str | The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * 'To find attributeEvents with eventSnap object. use /attributeEvents?embedded={\"eventSnaps\":1}' (optional)

try:
    # Get all attributeEvents
    api_response = api_instance.attribute_events_get(where=where, page=page, sort=sort, max_results=max_results, embedded=embedded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->attribute_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the attributeEvent model. Example:   * To find attributeEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /attributeEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;}   * To find attributeEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /attributeEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;,\&quot;eventDetails.sourceId\&quot;:\&quot;5c1956e925b6b30001103eab\&quot;} | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /attributeEvents?page&#x3D;4 | [optional] 
 **sort** | **str**| The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort attributeEvents by startTimeStamp in eventDetails IN ASCEDING order, use /attributeEvents?sort&#x3D;eventDetails.startTimeStamp   * To sort attributeEvents by startTimeStamp in eventDetails IN DECENDING order, use /attributeEvents?sort&#x3D;-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest attributeEvent among whole attributeEvents, use /attributeEvents?maxResults&#x3D;1   * To limit attributeEvents to 5, use /attributeEvents?maxResults&#x3D;5 | [optional] 
 **embedded** | **str**| The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find attributeEvents with eventSnap object. use /attributeEvents?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27; | [optional] 

### Return type

[**AttributeEventsResponse**](AttributeEventsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_events_id_delete**
> attribute_events_id_delete(id, if_match)

Delete an event

Delete an attributeEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete an event
    api_instance.attribute_events_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->attribute_events_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_events_id_get**
> AttributeEvent attribute_events_id_get(id, embedded=embedded)

Get attributeEvent by id

Get attributeEvent by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
embedded = 'embedded_example' # str | The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * 'To find attributeEvents with eventSnap object. use /attributeEvents/{id}?embedded={\"eventSnaps\":1}' (optional)

try:
    # Get attributeEvent by id
    api_response = api_instance.attribute_events_id_get(id, embedded=embedded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->attribute_events_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **embedded** | **str**| The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find attributeEvents with eventSnap object. use /attributeEvents/{id}?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27; | [optional] 

### Return type

[**AttributeEvent**](AttributeEvent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_events_id_patch**
> DefaultResponse attribute_events_id_patch(if_match, id, body=body)

Patch

Patch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.AttributeEvent() # AttributeEvent |  (optional)

try:
    # Patch
    api_response = api_instance.attribute_events_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->attribute_events_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**AttributeEvent**](AttributeEvent.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_events_post**
> DefaultResponse attribute_events_post(body=body)

Create an attributeEvent

Create an attributeEvent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AttributeEvent() # AttributeEvent |  (optional)

try:
    # Create an attributeEvent
    api_response = api_instance.attribute_events_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->attribute_events_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributeEvent**](AttributeEvent.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clips_get**
> ClipsResponse clips_get()

Get all unprocesed clips

Get all unprocesed clips

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))

try:
    # Get all unprocesed clips
    api_response = api_instance.clips_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->clips_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClipsResponse**](ClipsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clips_id_get**
> Clip clips_id_get(id)

Get clip by id

Get clip by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get clip by id
    api_response = api_instance.clips_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->clips_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**Clip**](Clip.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clips_post**
> DefaultResponse clips_post(body=body)

Create an unprocesed clip

Create an unprocesed clip

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Clip() # Clip |  (optional)

try:
    # Create an unprocesed clip
    api_response = api_instance.clips_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->clips_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Clip**](Clip.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_task_status_cumulative_get**
> EngineTaskStatusCumulative engine_task_status_cumulative_get()

Get task status response

Get task status response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))

try:
    # Get task status response
    api_response = api_instance.engine_task_status_cumulative_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engine_task_status_cumulative_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EngineTaskStatusCumulative**](EngineTaskStatusCumulative.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_task_status_get**
> EngineTaskStatusResponse engine_task_status_get(where=where, page=page, sort=sort, max_results=max_results)

Get all engineTaskStatus

Get all engineTaskStatus

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the engineTaskStatus model. Example:   * To find engineTaskStatus with engineTaskId equal \"11\", use /engineTaskStatus?where={\"engineTaskId\":\"11\"} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find engine tasks at page no 4, use /engineTaskStatus?page=4 (optional)
sort = 'sort_example' # str | The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort engineTasks by created IN ASCEDING order, use /engineTaskStatus?sort=created   * To sort engineTasks by created IN DECENDING order, use /engineTaskStatus?sort=-created   * Please note the - (minus) sign in front of the created, that indicates inverse of ASCENDING (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest engineTask among whole engineTasks, use /engineTaskStatus?maxResults=1   * To limit engineTasks to 2, use /engineTaskStatus?maxResults=2 (optional)

try:
    # Get all engineTaskStatus
    api_response = api_instance.engine_task_status_get(where=where, page=page, sort=sort, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engine_task_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the engineTaskStatus model. Example:   * To find engineTaskStatus with engineTaskId equal \&quot;11\&quot;, use /engineTaskStatus?where&#x3D;{\&quot;engineTaskId\&quot;:\&quot;11\&quot;} | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find engine tasks at page no 4, use /engineTaskStatus?page&#x3D;4 | [optional] 
 **sort** | **str**| The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort engineTasks by created IN ASCEDING order, use /engineTaskStatus?sort&#x3D;created   * To sort engineTasks by created IN DECENDING order, use /engineTaskStatus?sort&#x3D;-created   * Please note the - (minus) sign in front of the created, that indicates inverse of ASCENDING | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest engineTask among whole engineTasks, use /engineTaskStatus?maxResults&#x3D;1   * To limit engineTasks to 2, use /engineTaskStatus?maxResults&#x3D;2 | [optional] 

### Return type

[**EngineTaskStatusResponse**](EngineTaskStatusResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_task_status_id_delete**
> engine_task_status_id_delete(id, if_match)

Delete an engineTaskStatus

Delete an engineTaskStatus

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete an engineTaskStatus
    api_instance.engine_task_status_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->engine_task_status_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_task_status_id_get**
> EngineTaskStatus engine_task_status_id_get(id)

Get engineTaskStatus by id

Get engineTaskStatus for a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get engineTaskStatus by id
    api_response = api_instance.engine_task_status_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engine_task_status_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**EngineTaskStatus**](EngineTaskStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_task_status_id_patch**
> DefaultResponse engine_task_status_id_patch(if_match, id, body=body)

Patch an engineTaskStatus

Patch an engineTaskStatus. Submit an object with one or more properties of the engineTask model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.EngineTaskStatus() # EngineTaskStatus |  (optional)

try:
    # Patch an engineTaskStatus
    api_response = api_instance.engine_task_status_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engine_task_status_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**EngineTaskStatus**](EngineTaskStatus.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_task_status_post**
> DefaultResponse engine_task_status_post(body=body)

Create an engineTaskStatus

Create a engineTaskStatus.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.EngineTaskStatus() # EngineTaskStatus |  (optional)

try:
    # Create an engineTaskStatus
    api_response = api_instance.engine_task_status_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engine_task_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EngineTaskStatus**](EngineTaskStatus.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_tasks_get**
> EngineTasksResponse engine_tasks_get(where=where, page=page, sort=sort, max_results=max_results, embedded=embedded)

Get all engineTasks

Get all engineTasks details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the engineTask model. Example:   * To find engineTasks with capbilitiesType equal 211 and sourceId equal \"4\", use /engineTasks?where={\"capbilitiesType\":322,\"source.sourceId\":\"4\"}   * To find engineTasks with destination.extras.value equal \"1553774721506487\", use /engineTasks?where={\"destination.extras.value\":\"1553774721506487\"} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find engine tasks at page no 4, use /engines?page=4 (optional)
sort = 'sort_example' # str | The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort engineTasks by created IN ASCEDING order, use /engineTasks?sort=created   * To sort engineTasks by created IN DECENDING order, use /engineTasks?sort=-created   * Please note the - (minus) sign in front of the created, that indicates inverse of ASCENDING (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest engineTask among whole engineTasks, use /engineTasks?maxResults=1   * To limit engineTasks to 2, use /engineTasks?maxResults=2 (optional)
embedded = 'embedded_example' # str | The embedded clause takes a JSON as a string with sourceEndPoint argument. Example:   * 'To find engineTasks with sourceEndPoint object. use /engineTasks?embedded={\"sourceEndPoint\":1}' (optional)

try:
    # Get all engineTasks
    api_response = api_instance.engine_tasks_get(where=where, page=page, sort=sort, max_results=max_results, embedded=embedded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engine_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the engineTask model. Example:   * To find engineTasks with capbilitiesType equal 211 and sourceId equal \&quot;4\&quot;, use /engineTasks?where&#x3D;{\&quot;capbilitiesType\&quot;:322,\&quot;source.sourceId\&quot;:\&quot;4\&quot;}   * To find engineTasks with destination.extras.value equal \&quot;1553774721506487\&quot;, use /engineTasks?where&#x3D;{\&quot;destination.extras.value\&quot;:\&quot;1553774721506487\&quot;} | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find engine tasks at page no 4, use /engines?page&#x3D;4 | [optional] 
 **sort** | **str**| The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort engineTasks by created IN ASCEDING order, use /engineTasks?sort&#x3D;created   * To sort engineTasks by created IN DECENDING order, use /engineTasks?sort&#x3D;-created   * Please note the - (minus) sign in front of the created, that indicates inverse of ASCENDING | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest engineTask among whole engineTasks, use /engineTasks?maxResults&#x3D;1   * To limit engineTasks to 2, use /engineTasks?maxResults&#x3D;2 | [optional] 
 **embedded** | **str**| The embedded clause takes a JSON as a string with sourceEndPoint argument. Example:   * &#x27;To find engineTasks with sourceEndPoint object. use /engineTasks?embedded&#x3D;{\&quot;sourceEndPoint\&quot;:1}&#x27; | [optional] 

### Return type

[**EngineTasksResponse**](EngineTasksResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_tasks_id_delete**
> engine_tasks_id_delete(id, if_match)

Delete an engine task

Delete an engine task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete an engine task
    api_instance.engine_tasks_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->engine_tasks_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_tasks_id_get**
> EngineTask engine_tasks_id_get(id)

Get engine task by id

Get engine task for a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get engine task by id
    api_response = api_instance.engine_tasks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**EngineTask**](EngineTask.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_tasks_id_patch**
> DefaultResponse engine_tasks_id_patch(if_match, id, body=body)

Patch an engine task

Patch an engine task. Submit an object with one or more properties of the engineTask model. 'Ex. {\"capbilitiesType\": [211, 206]} or {\"capbilitiesType\": [211, 206], \"source\": {\"sourceId\":\"\", .....}}'

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.EngineTask() # EngineTask |  (optional)

try:
    # Patch an engine task
    api_response = api_instance.engine_tasks_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engine_tasks_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**EngineTask**](EngineTask.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_tasks_post**
> DefaultResponse engine_tasks_post(body=body)

Create an engineTask

Create a engineTasks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.EngineTask() # EngineTask |  (optional)

try:
    # Create an engineTask
    api_response = api_instance.engine_tasks_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engine_tasks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EngineTask**](EngineTask.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engines_get**
> EnginesResponse engines_get(where=where, page=page, sort=sort, max_results=max_results)

Get all engine details

Get all engine details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /engines?where={\"capabilities\":{\"$in\":[206,211]}} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /engines?page=4 (optional)
sort = 'sort_example' # str |  (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first registeredFace among all registeredFaces, use /engines?maxResults=1   * To limit registeredFaces to 5, use /engines?maxResults=5 (optional)

try:
    # Get all engine details
    api_response = api_instance.engines_get(where=where, page=page, sort=sort, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engines_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /engines?where&#x3D;{\&quot;capabilities\&quot;:{\&quot;$in\&quot;:[206,211]}} | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /engines?page&#x3D;4 | [optional] 
 **sort** | **str**|  | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first registeredFace among all registeredFaces, use /engines?maxResults&#x3D;1   * To limit registeredFaces to 5, use /engines?maxResults&#x3D;5 | [optional] 

### Return type

[**EnginesResponse**](EnginesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engines_id_delete**
> engines_id_delete(id, if_match)

Delete an engine

Delete an engine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete an engine
    api_instance.engines_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->engines_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engines_id_get**
> Engine engines_id_get(id)

Get engine by id

Get engine details for a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get engine by id
    api_response = api_instance.engines_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engines_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**Engine**](Engine.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engines_id_patch**
> DefaultResponse engines_id_patch(if_match, id, body=body)

Patch

Patch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.Engine() # Engine |  (optional)

try:
    # Patch
    api_response = api_instance.engines_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engines_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**Engine**](Engine.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engines_post**
> DefaultResponse engines_post(body=body)

Create an engine

Create an engine.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Engine() # Engine |  (optional)

try:
    # Create an engine
    api_response = api_instance.engines_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engines_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Engine**](Engine.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_snaps_get**
> EventSnapsResponse event_snaps_get()

Get all eventSnaps

Get all eventSnaps

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))

try:
    # Get all eventSnaps
    api_response = api_instance.event_snaps_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->event_snaps_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EventSnapsResponse**](EventSnapsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_snaps_id_get**
> Snap event_snaps_id_get(id)

Get eventSnap by id

Get eventSnap by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get eventSnap by id
    api_response = api_instance.event_snaps_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->event_snaps_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**Snap**](Snap.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_snaps_post**
> DefaultResponse event_snaps_post(body=body)

Create an eventSnap

Create an eventSnap.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Snap() # Snap |  (optional)

try:
    # Create an eventSnap
    api_response = api_instance.event_snaps_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->event_snaps_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Snap**](Snap.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inferencers_get**
> InferencersResponse inferencers_get(where=where, page=page, sort=sort, max_results=max_results)

Get all inferencers details

Get all inferencers details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /inferencers?where={\"capabilities\":{\"$in\":[206,211]}} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /inferencers?page=4 (optional)
sort = 'sort_example' # str |  (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first inferencer among all inferencers, use /inferencers?maxResults=1   * To limit inferencers to 5, use /inferencers?maxResults=5 (optional)

try:
    # Get all inferencers details
    api_response = api_instance.inferencers_get(where=where, page=page, sort=sort, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->inferencers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /inferencers?where&#x3D;{\&quot;capabilities\&quot;:{\&quot;$in\&quot;:[206,211]}} | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /inferencers?page&#x3D;4 | [optional] 
 **sort** | **str**|  | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first inferencer among all inferencers, use /inferencers?maxResults&#x3D;1   * To limit inferencers to 5, use /inferencers?maxResults&#x3D;5 | [optional] 

### Return type

[**InferencersResponse**](InferencersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inferencers_id_delete**
> inferencers_id_delete(id, if_match)

Delete an inferencer

Delete an inferencer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete an inferencer
    api_instance.inferencers_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->inferencers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inferencers_id_get**
> Inferencer inferencers_id_get(id)

Get inferencer by id

Get engine details for a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get inferencer by id
    api_response = api_instance.inferencers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->inferencers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**Inferencer**](Inferencer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inferencers_id_patch**
> DefaultResponse inferencers_id_patch(if_match, id, body=body)

Patch

Patch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.Inferencer() # Inferencer |  (optional)

try:
    # Patch
    api_response = api_instance.inferencers_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->inferencers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**Inferencer**](Inferencer.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inferencers_post**
> DefaultResponse inferencers_post(body=body)

Create an inferencer

Create an inferencer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Inferencer() # Inferencer |  (optional)

try:
    # Create an inferencer
    api_response = api_instance.inferencers_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->inferencers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Inferencer**](Inferencer.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_sources_get**
> MediaSourceResponse media_sources_get(where=where, page=page, sort=sort, max_results=max_results)

Get all media sources

Get all media sources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | Media sources (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /mediaSources?page=4 (optional)
sort = 'sort_example' # str |  (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first pipeline among all mediaSources, use /mediaSources?maxResults=1   * To limit mediaSources to 5, use /mediaSources?maxResults=5 (optional)

try:
    # Get all media sources
    api_response = api_instance.media_sources_get(where=where, page=page, sort=sort, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->media_sources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Media sources | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /mediaSources?page&#x3D;4 | [optional] 
 **sort** | **str**|  | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first pipeline among all mediaSources, use /mediaSources?maxResults&#x3D;1   * To limit mediaSources to 5, use /mediaSources?maxResults&#x3D;5 | [optional] 

### Return type

[**MediaSourceResponse**](MediaSourceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_sources_id_delete**
> media_sources_id_delete(id, if_match)

Delete a media source

Delete a media source

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete a media source
    api_instance.media_sources_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->media_sources_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_sources_id_get**
> SourceEndPoint media_sources_id_get(id)

Get media source by id

Get media source by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get media source by id
    api_response = api_instance.media_sources_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->media_sources_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**SourceEndPoint**](SourceEndPoint.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_sources_id_patch**
> DefaultResponse media_sources_id_patch(if_match, id, body=body)

Patch

Patch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.SourceEndPoint() # SourceEndPoint |  (optional)

try:
    # Patch
    api_response = api_instance.media_sources_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->media_sources_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**SourceEndPoint**](SourceEndPoint.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_sources_post**
> DefaultResponse media_sources_post(body=body)

Create a media source

Create a media source

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SourceEndPoint() # SourceEndPoint |  (optional)

try:
    # Create a media source
    api_response = api_instance.media_sources_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->media_sources_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceEndPoint**](SourceEndPoint.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **motion_detectors_get**
> MotionDetectorsResponse motion_detectors_get(where=where, page=page, sort=sort, max_results=max_results)

Get all motionDetectors details

Get all motionDetectors details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /motionDetectors?where={\"capabilities\":{\"$in\":[206,211]}} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /motionDetectors?page=4 (optional)
sort = 'sort_example' # str |  (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first motionDetector among all motionDetectors, use /motionDetectors?maxResults=1   * To limit motionDetectors to 5, use /motionDetectors?maxResults=5 (optional)

try:
    # Get all motionDetectors details
    api_response = api_instance.motion_detectors_get(where=where, page=page, sort=sort, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->motion_detectors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /motionDetectors?where&#x3D;{\&quot;capabilities\&quot;:{\&quot;$in\&quot;:[206,211]}} | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /motionDetectors?page&#x3D;4 | [optional] 
 **sort** | **str**|  | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first motionDetector among all motionDetectors, use /motionDetectors?maxResults&#x3D;1   * To limit motionDetectors to 5, use /motionDetectors?maxResults&#x3D;5 | [optional] 

### Return type

[**MotionDetectorsResponse**](MotionDetectorsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **motion_detectors_id_delete**
> motion_detectors_id_delete(id, if_match)

Delete an motionDetector

Delete an motionDetector

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete an motionDetector
    api_instance.motion_detectors_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->motion_detectors_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **motion_detectors_id_get**
> MotionDetector motion_detectors_id_get(id)

Get motionDetector by id

Get engine details for a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get motionDetector by id
    api_response = api_instance.motion_detectors_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->motion_detectors_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**MotionDetector**](MotionDetector.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **motion_detectors_id_patch**
> DefaultResponse motion_detectors_id_patch(if_match, id, body=body)

Patch

Patch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.MotionDetector() # MotionDetector |  (optional)

try:
    # Patch
    api_response = api_instance.motion_detectors_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->motion_detectors_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**MotionDetector**](MotionDetector.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **motion_detectors_post**
> DefaultResponse motion_detectors_post(body=body)

Create an motionDetector

Create an motionDetector.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.MotionDetector() # MotionDetector |  (optional)

try:
    # Create an motionDetector
    api_response = api_instance.motion_detectors_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->motion_detectors_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MotionDetector**](MotionDetector.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_get**
> PipelinesResponse pipelines_get(where=where, page=page, sort=sort, max_results=max_results)

Get all pipelines details

Get all pipelines details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /pipelines?where={\"capabilities\":{\"$in\":[206,211]}} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /pipelines?page=4 (optional)
sort = 'sort_example' # str |  (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first pipeline among all pipelines, use /pipelines?maxResults=1   * To limit pipelines to 5, use /pipelines?maxResults=5 (optional)

try:
    # Get all pipelines details
    api_response = api_instance.pipelines_get(where=where, page=page, sort=sort, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->pipelines_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /pipelines?where&#x3D;{\&quot;capabilities\&quot;:{\&quot;$in\&quot;:[206,211]}} | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /pipelines?page&#x3D;4 | [optional] 
 **sort** | **str**|  | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first pipeline among all pipelines, use /pipelines?maxResults&#x3D;1   * To limit pipelines to 5, use /pipelines?maxResults&#x3D;5 | [optional] 

### Return type

[**PipelinesResponse**](PipelinesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_id_delete**
> pipelines_id_delete(id, if_match)

Delete an pipeline

Delete an pipeline

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete an pipeline
    api_instance.pipelines_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->pipelines_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_id_get**
> Pipeline pipelines_id_get(id)

Get pipeline by id

Get engine details for a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get pipeline by id
    api_response = api_instance.pipelines_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->pipelines_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_id_patch**
> DefaultResponse pipelines_id_patch(if_match, id, body=body)

Patch

Patch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.Pipeline() # Pipeline |  (optional)

try:
    # Patch
    api_response = api_instance.pipelines_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->pipelines_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**Pipeline**](Pipeline.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_post**
> DefaultResponse pipelines_post(body=body)

Create an pipeline

Create an pipeline.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Pipeline() # Pipeline |  (optional)

try:
    # Create an pipeline
    api_response = api_instance.pipelines_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->pipelines_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pipeline**](Pipeline.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_processes_get**
> PreProcessesResponse pre_processes_get(where=where, page=page, sort=sort, max_results=max_results)

Get all preProcesses details

Get all preProcesses details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /preProcesses?where={\"capabilities\":{\"$in\":[206,211]}} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /preProcesses?page=4 (optional)
sort = 'sort_example' # str |  (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first preProcess among all preProcesses, use /preProcesses?maxResults=1   * To limit preProcesses to 5, use /preProcesses?maxResults=5 (optional)

try:
    # Get all preProcesses details
    api_response = api_instance.pre_processes_get(where=where, page=page, sort=sort, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->pre_processes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /preProcesses?where&#x3D;{\&quot;capabilities\&quot;:{\&quot;$in\&quot;:[206,211]}} | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /preProcesses?page&#x3D;4 | [optional] 
 **sort** | **str**|  | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first preProcess among all preProcesses, use /preProcesses?maxResults&#x3D;1   * To limit preProcesses to 5, use /preProcesses?maxResults&#x3D;5 | [optional] 

### Return type

[**PreProcessesResponse**](PreProcessesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_processes_id_delete**
> pre_processes_id_delete(id, if_match)

Delete an preProcess

Delete an preProcess

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete an preProcess
    api_instance.pre_processes_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->pre_processes_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_processes_id_get**
> PreProcess pre_processes_id_get(id)

Get preProcess by id

Get engine details for a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get preProcess by id
    api_response = api_instance.pre_processes_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->pre_processes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**PreProcess**](PreProcess.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_processes_id_patch**
> DefaultResponse pre_processes_id_patch(if_match, id, body=body)

Patch

Patch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.PreProcess() # PreProcess |  (optional)

try:
    # Patch
    api_response = api_instance.pre_processes_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->pre_processes_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**PreProcess**](PreProcess.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_processes_post**
> DefaultResponse pre_processes_post(body=body)

Create an preProcess

Create an preProcess.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PreProcess() # PreProcess |  (optional)

try:
    # Create an preProcess
    api_response = api_instance.pre_processes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->pre_processes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PreProcess**](PreProcess.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **precis_engine_task_status_get**
> PrecisEngineTaskStatusResponse precis_engine_task_status_get(where=where, page=page, sort=sort, max_results=max_results)

Get all precisEngineTaskStatus

Get all precisEngineTaskStatus

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the precisEngineTaskStatus model. Example:   * To find precisEngineTaskStatus with engineTaskId equal \"11\", use /precisEngineTaskStatus?where={\"engineTaskId\":\"11\"} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find engine tasks at page no 4, use /precisEngineTaskStatus?page=4 (optional)
sort = 'sort_example' # str | The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort engineTasks by created IN ASCEDING order, use /precisEngineTaskStatus?sort=created   * To sort engineTasks by created IN DECENDING order, use /precisEngineTaskStatus?sort=-created   * Please note the - (minus) sign in front of the created, that indicates inverse of ASCENDING (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest engineTask among whole precisEngineTask, use /precisEngineTaskStatus?maxResults=1   * To limit engineTasks to 2, use /precisEngineTaskStatus?maxResults=2 (optional)

try:
    # Get all precisEngineTaskStatus
    api_response = api_instance.precis_engine_task_status_get(where=where, page=page, sort=sort, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->precis_engine_task_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the precisEngineTaskStatus model. Example:   * To find precisEngineTaskStatus with engineTaskId equal \&quot;11\&quot;, use /precisEngineTaskStatus?where&#x3D;{\&quot;engineTaskId\&quot;:\&quot;11\&quot;} | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find engine tasks at page no 4, use /precisEngineTaskStatus?page&#x3D;4 | [optional] 
 **sort** | **str**| The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort engineTasks by created IN ASCEDING order, use /precisEngineTaskStatus?sort&#x3D;created   * To sort engineTasks by created IN DECENDING order, use /precisEngineTaskStatus?sort&#x3D;-created   * Please note the - (minus) sign in front of the created, that indicates inverse of ASCENDING | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest engineTask among whole precisEngineTask, use /precisEngineTaskStatus?maxResults&#x3D;1   * To limit engineTasks to 2, use /precisEngineTaskStatus?maxResults&#x3D;2 | [optional] 

### Return type

[**PrecisEngineTaskStatusResponse**](PrecisEngineTaskStatusResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **precis_engine_task_status_id_delete**
> precis_engine_task_status_id_delete(id, if_match)

Delete an precisEngineTaskStatus

Delete an precisEngineTaskStatus

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete an precisEngineTaskStatus
    api_instance.precis_engine_task_status_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->precis_engine_task_status_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **precis_engine_task_status_id_get**
> PrecisEngineTaskStatus precis_engine_task_status_id_get(id)

Get precisEngineTaskStatus by id

Get precisEngineTaskStatus for a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get precisEngineTaskStatus by id
    api_response = api_instance.precis_engine_task_status_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->precis_engine_task_status_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**PrecisEngineTaskStatus**](PrecisEngineTaskStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **precis_engine_task_status_id_patch**
> DefaultResponse precis_engine_task_status_id_patch(if_match, id, body=body)

Patch an precisEngineTaskStatus

Patch an engineTaskStatus. Submit an object with one or more properties of the precisEngineTaskStatus model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.PrecisEngineTaskStatus() # PrecisEngineTaskStatus |  (optional)

try:
    # Patch an precisEngineTaskStatus
    api_response = api_instance.precis_engine_task_status_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->precis_engine_task_status_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**PrecisEngineTaskStatus**](PrecisEngineTaskStatus.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **precis_engine_task_status_post**
> DefaultResponse precis_engine_task_status_post(body=body)

Create an precisEngineTaskStatus

Create a precisEngineTaskStatus.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PrecisEngineTaskStatus() # PrecisEngineTaskStatus |  (optional)

try:
    # Create an precisEngineTaskStatus
    api_response = api_instance.precis_engine_task_status_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->precis_engine_task_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrecisEngineTaskStatus**](PrecisEngineTaskStatus.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **precis_engine_tasks_get**
> PrecisEngineTasksResponse precis_engine_tasks_get(where=where, page=page, sort=sort, max_results=max_results, embedded=embedded)

Get all precisEngineTasks

Get all engineTasks details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the engineTask model. Example:   * To find precisEngineTasks with capbilitiesType equal 211 and sourceId equal \"4\", use /precisEngineTasks?where={\"capbilitiesType\":322,\"source.sourceId\":\"4\"}   * To find precisEngineTasks with destination.extras.value equal \"1553774721506487\", use /precisEngineTasks?where={\"destination.extras.value\":\"1553774721506487\"} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find engine tasks at page no 4, use /engines?page=4 (optional)
sort = 'sort_example' # str | The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort engineTasks by created IN ASCEDING order, use /precisEngineTasks?sort=created   * To sort engineTasks by created IN DECENDING order, use /precisEngineTasks?sort=-created   * Please note the - (minus) sign in front of the created, that indicates inverse of ASCENDING (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest engineTask among whole engineTasks, use /precisEngineTasks?maxResults=1   * To limit engineTasks to 2, use /precisEngineTasks?maxResults=2 (optional)
embedded = 'embedded_example' # str | The embedded clause takes a JSON as a string with sourceEndPoint argument. Example:   * 'To find engineTasks with sourceEndPoint object. use /precisEngineTasks?embedded={\"sourceEndPoint\":1}' (optional)

try:
    # Get all precisEngineTasks
    api_response = api_instance.precis_engine_tasks_get(where=where, page=page, sort=sort, max_results=max_results, embedded=embedded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->precis_engine_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the engineTask model. Example:   * To find precisEngineTasks with capbilitiesType equal 211 and sourceId equal \&quot;4\&quot;, use /precisEngineTasks?where&#x3D;{\&quot;capbilitiesType\&quot;:322,\&quot;source.sourceId\&quot;:\&quot;4\&quot;}   * To find precisEngineTasks with destination.extras.value equal \&quot;1553774721506487\&quot;, use /precisEngineTasks?where&#x3D;{\&quot;destination.extras.value\&quot;:\&quot;1553774721506487\&quot;} | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find engine tasks at page no 4, use /engines?page&#x3D;4 | [optional] 
 **sort** | **str**| The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort engineTasks by created IN ASCEDING order, use /precisEngineTasks?sort&#x3D;created   * To sort engineTasks by created IN DECENDING order, use /precisEngineTasks?sort&#x3D;-created   * Please note the - (minus) sign in front of the created, that indicates inverse of ASCENDING | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest engineTask among whole engineTasks, use /precisEngineTasks?maxResults&#x3D;1   * To limit engineTasks to 2, use /precisEngineTasks?maxResults&#x3D;2 | [optional] 
 **embedded** | **str**| The embedded clause takes a JSON as a string with sourceEndPoint argument. Example:   * &#x27;To find engineTasks with sourceEndPoint object. use /precisEngineTasks?embedded&#x3D;{\&quot;sourceEndPoint\&quot;:1}&#x27; | [optional] 

### Return type

[**PrecisEngineTasksResponse**](PrecisEngineTasksResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **precis_engine_tasks_id_delete**
> precis_engine_tasks_id_delete(id, if_match)

Delete an precis engine task

Delete an precis engine task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete an precis engine task
    api_instance.precis_engine_tasks_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->precis_engine_tasks_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **precis_engine_tasks_id_get**
> PrecisEngineTask precis_engine_tasks_id_get(id)

Get precis engine task by id

Get precis engine task for a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get precis engine task by id
    api_response = api_instance.precis_engine_tasks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->precis_engine_tasks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**PrecisEngineTask**](PrecisEngineTask.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **precis_engine_tasks_id_patch**
> DefaultResponse precis_engine_tasks_id_patch(if_match, id, body=body)

Patch an precis engine task

Patch an engine task. Submit an object with one or more properties of the engineTask model. 'Ex. {\"capbilitiesType\": [211, 206]} or {\"capbilitiesType\": [211, 206], \"source\": {\"sourceId\":\"\", .....}}'

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.PrecisEngineTask() # PrecisEngineTask |  (optional)

try:
    # Patch an precis engine task
    api_response = api_instance.precis_engine_tasks_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->precis_engine_tasks_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**PrecisEngineTask**](PrecisEngineTask.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **precis_engine_tasks_post**
> DefaultResponse precis_engine_tasks_post(body=body)

Create an precisEngineTasks

Create a engineTasks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PrecisEngineTask() # PrecisEngineTask |  (optional)

try:
    # Create an precisEngineTasks
    api_response = api_instance.precis_engine_tasks_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->precis_engine_tasks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrecisEngineTask**](PrecisEngineTask.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snaps_get**
> SnapsResponse snaps_get()

Get all unprocesed snaps

Get all unprocesed snaps

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))

try:
    # Get all unprocesed snaps
    api_response = api_instance.snaps_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->snaps_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnapsResponse**](SnapsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snaps_id_get**
> Snap snaps_id_get(id)

Get snap by id

Get snap by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID

try:
    # Get snap by id
    api_response = api_instance.snaps_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->snaps_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 

### Return type

[**Snap**](Snap.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snaps_post**
> DefaultResponse snaps_post(body=body)

Create a unprocesed snap

Create an unprocesed snap

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Snap() # Snap |  (optional)

try:
    # Create a unprocesed snap
    api_response = api_instance.snaps_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->snaps_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Snap**](Snap.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **va_events_get**
> VaEventsResponse va_events_get(where=where, page=page, sort=sort, max_results=max_results, embedded=embedded)

Get all vaEvents

Get all vaEvents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the vaEvent model. Example:   * To find vaEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /vaEvents?where={\"eventDetails.engineTaskId\":\"5c1956e925b6b30001103eaa\"}   * To find vaEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /vaEvents?where={\"eventDetails.engineTaskId\":\"5c1956e925b6b30001103eaa\",\"eventDetails.sourceId\":\"5c1956e925b6b30001103eab\"} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /vaEvents?page=4 (optional)
sort = 'sort_example' # str | The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort vaEvents by startTimeStamp in eventDetails IN ASCEDING order, use /vaEvents?sort=eventDetails.startTimeStamp   * To sort vaEvents by startTimeStamp in eventDetails IN DECENDING order, use /vaEvents?sort=-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest vaEvent among whole vaEvents, use /vaEvents?maxResults=1   * To limit vaEvents to 5, use /vaEvents?maxResults=5 (optional)
embedded = 'embedded_example' # str | The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * 'To find vaEvents with eventSnap object. use /vaEvents?embedded={\"eventSnaps\":1}' (optional)

try:
    # Get all vaEvents
    api_response = api_instance.va_events_get(where=where, page=page, sort=sort, max_results=max_results, embedded=embedded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->va_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the vaEvent model. Example:   * To find vaEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /vaEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;}   * To find vaEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /vaEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;,\&quot;eventDetails.sourceId\&quot;:\&quot;5c1956e925b6b30001103eab\&quot;} | [optional] 
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /vaEvents?page&#x3D;4 | [optional] 
 **sort** | **str**| The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort vaEvents by startTimeStamp in eventDetails IN ASCEDING order, use /vaEvents?sort&#x3D;eventDetails.startTimeStamp   * To sort vaEvents by startTimeStamp in eventDetails IN DECENDING order, use /vaEvents?sort&#x3D;-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest vaEvent among whole vaEvents, use /vaEvents?maxResults&#x3D;1   * To limit vaEvents to 5, use /vaEvents?maxResults&#x3D;5 | [optional] 
 **embedded** | **str**| The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find vaEvents with eventSnap object. use /vaEvents?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27; | [optional] 

### Return type

[**VaEventsResponse**](VaEventsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **va_events_id_delete**
> va_events_id_delete(id, if_match)

Delete an event

Delete an vaEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
if_match = 'if_match_example' # str | 

try:
    # Delete an event
    api_instance.va_events_id_delete(id, if_match)
except ApiException as e:
    print("Exception when calling EnginesApi->va_events_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **if_match** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **va_events_id_get**
> VaEvent va_events_id_get(id, embedded=embedded)

Get vaEvent by id

Get vaEvent by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Unique ID
embedded = 'embedded_example' # str | The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * 'To find vaEvents with eventSnap object. use /vaEvents/{id}?embedded={\"eventSnaps\":1}' (optional)

try:
    # Get vaEvent by id
    api_response = api_instance.va_events_id_get(id, embedded=embedded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->va_events_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID | 
 **embedded** | **str**| The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find vaEvents with eventSnap object. use /vaEvents/{id}?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27; | [optional] 

### Return type

[**VaEvent**](VaEvent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **va_events_id_patch**
> DefaultResponse va_events_id_patch(if_match, id, body=body)

Patch

Patch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = swagger_client.VaEvent() # VaEvent |  (optional)

try:
    # Patch
    api_response = api_instance.va_events_id_patch(if_match, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->va_events_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**|  | 
 **id** | **str**| Unique ID | 
 **body** | [**VaEvent**](VaEvent.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **va_events_post**
> DefaultResponse va_events_post(body=body)

Create an vaEvent

Create an vaEvent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.EnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.VaEvent() # VaEvent |  (optional)

try:
    # Create an vaEvent
    api_response = api_instance.va_events_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->va_events_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VaEvent**](VaEvent.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

