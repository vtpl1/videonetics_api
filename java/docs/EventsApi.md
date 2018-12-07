# EventsApi

All URIs are relative to *http://v2.videonetics.com:5000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterpriseIdEventsGet**](EventsApi.md#enterpriseIdEventsGet) | **GET** /{enterpriseId}/events | Get events list
[**enterpriseIdEventsPost**](EventsApi.md#enterpriseIdEventsPost) | **POST** /{enterpriseId}/events | Create new event

<a name="enterpriseIdEventsGet"></a>
# **enterpriseIdEventsGet**
> Events enterpriseIdEventsGet(enterpriseId)

Get events list

List all the events available.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.EventsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: accessCode
OAuth accessCode = (OAuth) defaultClient.getAuthentication("accessCode");
accessCode.setAccessToken("YOUR ACCESS TOKEN");

EventsApi apiInstance = new EventsApi();
UUID enterpriseId = new UUID(); // UUID | enterprise Id
try {
    Events result = apiInstance.enterpriseIdEventsGet(enterpriseId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling EventsApi#enterpriseIdEventsGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterpriseId** | [**UUID**](.md)| enterprise Id |

### Return type

[**Events**](Events.md)

### Authorization

[accessCode](../README.md#accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="enterpriseIdEventsPost"></a>
# **enterpriseIdEventsPost**
> Event enterpriseIdEventsPost(enterpriseId)

Create new event

Create new event.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.EventsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: accessCode
OAuth accessCode = (OAuth) defaultClient.getAuthentication("accessCode");
accessCode.setAccessToken("YOUR ACCESS TOKEN");

EventsApi apiInstance = new EventsApi();
UUID enterpriseId = new UUID(); // UUID | enterprise Id
try {
    Event result = apiInstance.enterpriseIdEventsPost(enterpriseId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling EventsApi#enterpriseIdEventsPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterpriseId** | [**UUID**](.md)| enterprise Id |

### Return type

[**Event**](Event.md)

### Authorization

[accessCode](../README.md#accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

