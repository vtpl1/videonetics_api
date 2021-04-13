# vtpl_api.EnginesApi

All URIs are relative to *http://v2.videonetics.com:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anpr_events_get**](EnginesApi.md#anpr_events_get) | **GET** /anprEvents | Get all anprEvents
[**anpr_events_id_get**](EnginesApi.md#anpr_events_id_get) | **GET** /anprEvents/{id} | Get anprEvent by id
[**anpr_events_post**](EnginesApi.md#anpr_events_post) | **POST** /anprEvents | Create an anprEvent
[**attribute_events_get**](EnginesApi.md#attribute_events_get) | **GET** /attributeEvents | Get all attributeEvents
[**attribute_events_id_get**](EnginesApi.md#attribute_events_id_get) | **GET** /attributeEvents/{id} | Get attributeEvent by id
[**attribute_events_post**](EnginesApi.md#attribute_events_post) | **POST** /attributeEvents | Create an attributeEvent
[**clips_get**](EnginesApi.md#clips_get) | **GET** /clips | Get all unprocesed clips
[**clips_id_get**](EnginesApi.md#clips_id_get) | **GET** /clips/{id} | Get clip by id
[**clips_post**](EnginesApi.md#clips_post) | **POST** /clips | Create an unprocesed clip
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
[**engines_post**](EnginesApi.md#engines_post) | **POST** /engines | Create an engine
[**event_snaps_get**](EnginesApi.md#event_snaps_get) | **GET** /eventSnaps | Get all eventSnaps
[**event_snaps_id_get**](EnginesApi.md#event_snaps_id_get) | **GET** /eventSnaps/{id} | Get eventSnap by id
[**event_snaps_post**](EnginesApi.md#event_snaps_post) | **POST** /eventSnaps | Create an eventSnap
[**snaps_get**](EnginesApi.md#snaps_get) | **GET** /snaps | Get all unprocesed snaps
[**snaps_id_get**](EnginesApi.md#snaps_id_get) | **GET** /snaps/{id} | Get snap by id
[**snaps_post**](EnginesApi.md#snaps_post) | **POST** /snaps | Create a unprocesed snap
[**va_events_get**](EnginesApi.md#va_events_get) | **GET** /vaEvents | Get all vaEvents
[**va_events_id_get**](EnginesApi.md#va_events_id_get) | **GET** /vaEvents/{id} | Get vaEvent by id
[**va_events_post**](EnginesApi.md#va_events_post) | **POST** /vaEvents | Create an vaEvent

# **anpr_events_get**
> AnprEventsResponse anpr_events_get(where=where, sort=sort, max_results=max_results, embedded=embedded)

Get all anprEvents

Get all anprEvents

### Example
```python
from __future__ import print_function
import time
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the anprEvent model. Example:   * To find anprEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /anprEvents?where={\"eventDetails.engineTaskId\":\"5c1956e925b6b30001103eaa\"}   * To find anprEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /anprEvents?where={\"eventDetails.engineTaskId\":\"5c1956e925b6b30001103eaa\",\"eventDetails.sourceId\":\"5c1956e925b6b30001103eab\"} (optional)
sort = 'sort_example' # str | The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort anprEvents by startTimeStamp in eventDetails IN ASCEDING order, use /anprEvents?sort=eventDetails.startTimeStamp   * To sort anprEvents by startTimeStamp in eventDetails IN DECENDING order, use /anprEvents?sort=-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest anprEvent among whole anprEvents, use /anprEvents?maxResults=1   * To limit anprEvents to 5, use /anprEvents?maxResults=5 (optional)
embedded = 'embedded_example' # str | The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * 'To find anprEvents with eventSnap object. use /anprEvents?embedded={\"eventSnaps\":1}' (optional)

try:
    # Get all anprEvents
    api_response = api_instance.anpr_events_get(where=where, sort=sort, max_results=max_results, embedded=embedded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->anpr_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the anprEvent model. Example:   * To find anprEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /anprEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;}   * To find anprEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /anprEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;,\&quot;eventDetails.sourceId\&quot;:\&quot;5c1956e925b6b30001103eab\&quot;} | [optional] 
 **sort** | **str**| The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort anprEvents by startTimeStamp in eventDetails IN ASCEDING order, use /anprEvents?sort&#x3D;eventDetails.startTimeStamp   * To sort anprEvents by startTimeStamp in eventDetails IN DECENDING order, use /anprEvents?sort&#x3D;-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest anprEvent among whole anprEvents, use /anprEvents?maxResults&#x3D;1   * To limit anprEvents to 5, use /anprEvents?maxResults&#x3D;5 | [optional] 
 **embedded** | **str**| The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find anprEvents with eventSnap object. use /anprEvents?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27; | [optional] 

### Return type

[**AnprEventsResponse**](AnprEventsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **anpr_events_id_get**
> AnprEvent anpr_events_id_get(id, embedded=embedded)

Get anprEvent by id

Get anprEvent by id

### Example
```python
from __future__ import print_function
import time
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
body = vtpl_api.AnprEvent() # AnprEvent |  (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_events_get**
> AttributeEventsResponse attribute_events_get(where=where, sort=sort, max_results=max_results, embedded=embedded)

Get all attributeEvents

Get all attributeEvents

### Example
```python
from __future__ import print_function
import time
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the attributeEvent model. Example:   * To find attributeEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /attributeEvents?where={\"eventDetails.engineTaskId\":\"5c1956e925b6b30001103eaa\"}   * To find attributeEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /attributeEvents?where={\"eventDetails.engineTaskId\":\"5c1956e925b6b30001103eaa\",\"eventDetails.sourceId\":\"5c1956e925b6b30001103eab\"} (optional)
sort = 'sort_example' # str | The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort attributeEvents by startTimeStamp in eventDetails IN ASCEDING order, use /attributeEvents?sort=eventDetails.startTimeStamp   * To sort attributeEvents by startTimeStamp in eventDetails IN DECENDING order, use /attributeEvents?sort=-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest attributeEvent among whole attributeEvents, use /attributeEvents?maxResults=1   * To limit attributeEvents to 5, use /attributeEvents?maxResults=5 (optional)
embedded = 'embedded_example' # str | The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * 'To find attributeEvents with eventSnap object. use /attributeEvents?embedded={\"eventSnaps\":1}' (optional)

try:
    # Get all attributeEvents
    api_response = api_instance.attribute_events_get(where=where, sort=sort, max_results=max_results, embedded=embedded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->attribute_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the attributeEvent model. Example:   * To find attributeEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /attributeEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;}   * To find attributeEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /attributeEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;,\&quot;eventDetails.sourceId\&quot;:\&quot;5c1956e925b6b30001103eab\&quot;} | [optional] 
 **sort** | **str**| The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort attributeEvents by startTimeStamp in eventDetails IN ASCEDING order, use /attributeEvents?sort&#x3D;eventDetails.startTimeStamp   * To sort attributeEvents by startTimeStamp in eventDetails IN DECENDING order, use /attributeEvents?sort&#x3D;-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest attributeEvent among whole attributeEvents, use /attributeEvents?maxResults&#x3D;1   * To limit attributeEvents to 5, use /attributeEvents?maxResults&#x3D;5 | [optional] 
 **embedded** | **str**| The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find attributeEvents with eventSnap object. use /attributeEvents?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27; | [optional] 

### Return type

[**AttributeEventsResponse**](AttributeEventsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_events_id_get**
> AttributeEvent attribute_events_id_get(id, embedded=embedded)

Get attributeEvent by id

Get attributeEvent by id

### Example
```python
from __future__ import print_function
import time
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
body = vtpl_api.AttributeEvent() # AttributeEvent |  (optional)

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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()

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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
body = vtpl_api.Clip() # Clip |  (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_task_status_get**
> EngineTaskStatusResponse engine_task_status_get(page=page, sort=sort, max_results=max_results)

Get all engineTaskStatus

Get all engineTaskStatus

### Example
```python
from __future__ import print_function
import time
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find engine tasks at page no 4, use /engineTaskStatus?page=4 (optional)
sort = 'sort_example' # str | The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort engineTasks by created IN ASCEDING order, use /engineTaskStatus?sort=created   * To sort engineTasks by created IN DECENDING order, use /engineTaskStatus?sort=-created   * Please note the - (minus) sign in front of the created, that indicates inverse of ASCENDING (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest engineTask among whole engineTasks, use /engineTaskStatus?maxResults=1   * To limit engineTasks to 2, use /engineTaskStatus?maxResults=2 (optional)

try:
    # Get all engineTaskStatus
    api_response = api_instance.engine_task_status_get(page=page, sort=sort, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engine_task_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find engine tasks at page no 4, use /engineTaskStatus?page&#x3D;4 | [optional] 
 **sort** | **str**| The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort engineTasks by created IN ASCEDING order, use /engineTaskStatus?sort&#x3D;created   * To sort engineTasks by created IN DECENDING order, use /engineTaskStatus?sort&#x3D;-created   * Please note the - (minus) sign in front of the created, that indicates inverse of ASCENDING | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest engineTask among whole engineTasks, use /engineTaskStatus?maxResults&#x3D;1   * To limit engineTasks to 2, use /engineTaskStatus?maxResults&#x3D;2 | [optional] 

### Return type

[**EngineTaskStatusResponse**](EngineTaskStatusResponse.md)

### Authorization

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = vtpl_api.EngineTaskStatus() # EngineTaskStatus |  (optional)

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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
body = vtpl_api.EngineTaskStatus() # EngineTaskStatus |  (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_tasks_get**
> EngineTasksResponse engine_tasks_get(where=where, page=page, sort=sort, max_results=max_results)

Get all engineTasks

Get all engineTasks details

### Example
```python
from __future__ import print_function
import time
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the engineTask model. Example:   * To find engineTasks with capbilitiesType equal 211 and sourceId equal \"4\", use /engineTasks?where={\"capbilitiesType\":322,\"source.sourceId\":\"4\"}   * To find engineTasks with destination.extras.value equal \"1553774721506487\", use /engineTasks?where={\"destination.extras.value\":\"1553774721506487\"} (optional)
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find engine tasks at page no 4, use /engines?page=4 (optional)
sort = 'sort_example' # str | The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort engineTasks by created IN ASCEDING order, use /engineTasks?sort=created   * To sort engineTasks by created IN DECENDING order, use /engineTasks?sort=-created   * Please note the - (minus) sign in front of the created, that indicates inverse of ASCENDING (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest engineTask among whole engineTasks, use /engineTasks?maxResults=1   * To limit engineTasks to 2, use /engineTasks?maxResults=2 (optional)

try:
    # Get all engineTasks
    api_response = api_instance.engine_tasks_get(where=where, page=page, sort=sort, max_results=max_results)
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

### Return type

[**EngineTasksResponse**](EngineTasksResponse.md)

### Authorization

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
if_match = 'if_match_example' # str | 
id = 'id_example' # str | Unique ID
body = vtpl_api.EngineTask() # EngineTask |  (optional)

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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
body = vtpl_api.EngineTask() # EngineTask |  (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engines_get**
> EnginesResponse engines_get(page=page, where=where, max_results=max_results)

Get all engine details

Get all engine details

### Example
```python
from __future__ import print_function
import time
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
page = 56 # int | The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /engines?page=4 (optional)
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /engines?where={\"capabilities\":{\"$in\":[206,211]}} (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first registeredFace among all registeredFaces, use /engines?maxResults=1   * To limit registeredFaces to 5, use /engines?maxResults=5 (optional)

try:
    # Get all engine details
    api_response = api_instance.engines_get(page=page, where=where, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->engines_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page clause takes a the page number you want to query. Example:   * To find registered faces at page no 4, use /engines?page&#x3D;4 | [optional] 
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the registeredFace model. Example:   * To find enginess with capabilities 206, 211 , use /engines?where&#x3D;{\&quot;capabilities\&quot;:{\&quot;$in\&quot;:[206,211]}} | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get first registeredFace among all registeredFaces, use /engines?maxResults&#x3D;1   * To limit registeredFaces to 5, use /engines?maxResults&#x3D;5 | [optional] 

### Return type

[**EnginesResponse**](EnginesResponse.md)

### Authorization

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
body = vtpl_api.Engine() # Engine |  (optional)

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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()

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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
body = vtpl_api.Snap() # Snap |  (optional)

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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()

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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
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

No authorization required

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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
body = vtpl_api.Snap() # Snap |  (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **va_events_get**
> VaEventsResponse va_events_get(where=where, sort=sort, max_results=max_results, embedded=embedded)

Get all vaEvents

Get all vaEvents

### Example
```python
from __future__ import print_function
import time
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
where = 'where_example' # str | The where clause takes a JSON as a string with one or many properties of the vaEvent model. Example:   * To find vaEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /vaEvents?where={\"eventDetails.engineTaskId\":\"5c1956e925b6b30001103eaa\"}   * To find vaEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /vaEvents?where={\"eventDetails.engineTaskId\":\"5c1956e925b6b30001103eaa\",\"eventDetails.sourceId\":\"5c1956e925b6b30001103eab\"} (optional)
sort = 'sort_example' # str | The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort vaEvents by startTimeStamp in eventDetails IN ASCEDING order, use /vaEvents?sort=eventDetails.startTimeStamp   * To sort vaEvents by startTimeStamp in eventDetails IN DECENDING order, use /vaEvents?sort=-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING (optional)
max_results = 56 # int | The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest vaEvent among whole vaEvents, use /vaEvents?maxResults=1   * To limit vaEvents to 5, use /vaEvents?maxResults=5 (optional)
embedded = 'embedded_example' # str | The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * 'To find vaEvents with eventSnap object. use /vaEvents?embedded={\"eventSnaps\":1}' (optional)

try:
    # Get all vaEvents
    api_response = api_instance.va_events_get(where=where, sort=sort, max_results=max_results, embedded=embedded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->va_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| The where clause takes a JSON as a string with one or many properties of the vaEvent model. Example:   * To find vaEvents with engineTaskId equal 5c1956e925b6b30001103eaa, use /vaEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;}   * To find vaEvents with engineTaskId equal 5c1956e925b6b30001103eaa and sourceId equal 5c1956e925b6b30001103eab, use /vaEvents?where&#x3D;{\&quot;eventDetails.engineTaskId\&quot;:\&quot;5c1956e925b6b30001103eaa\&quot;,\&quot;eventDetails.sourceId\&quot;:\&quot;5c1956e925b6b30001103eab\&quot;} | [optional] 
 **sort** | **str**| The sort query parameter sorts the result set in ascending and desending order by one of the property of the result set. Example:   * To sort vaEvents by startTimeStamp in eventDetails IN ASCEDING order, use /vaEvents?sort&#x3D;eventDetails.startTimeStamp   * To sort vaEvents by startTimeStamp in eventDetails IN DECENDING order, use /vaEvents?sort&#x3D;-eventDetails.startTimeStamp   * Please note the - (minus) sign in front of the eventDetails.startTimeStamp, that indicates inverse of ASCENDING | [optional] 
 **max_results** | **int**| The maxResults query parameter limits results equal to # of maxResults. Example:   * To get latest vaEvent among whole vaEvents, use /vaEvents?maxResults&#x3D;1   * To limit vaEvents to 5, use /vaEvents?maxResults&#x3D;5 | [optional] 
 **embedded** | **str**| The embedded clause takes a JSON as a string with eventSnaps argument. Example:   * &#x27;To find vaEvents with eventSnap object. use /vaEvents?embedded&#x3D;{\&quot;eventSnaps\&quot;:1}&#x27; | [optional] 

### Return type

[**VaEventsResponse**](VaEventsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **va_events_id_get**
> VaEvent va_events_id_get(id, embedded=embedded)

Get vaEvent by id

Get vaEvent by id

### Example
```python
from __future__ import print_function
import time
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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
import vtpl_api
from vtpl_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vtpl_api.EnginesApi()
body = vtpl_api.VaEvent() # VaEvent |  (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

