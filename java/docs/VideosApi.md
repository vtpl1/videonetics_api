# VideosApi

All URIs are relative to *https://v2.videonetics.com:5000/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterpriseIdCameraIdVideosGet**](VideosApi.md#enterpriseIdCameraIdVideosGet) | **GET** /{enterpriseId}/{cameraId}/videos | Get all cameras for a enterprise

<a name="enterpriseIdCameraIdVideosGet"></a>
# **enterpriseIdCameraIdVideosGet**
> Cameras enterpriseIdCameraIdVideosGet(enterpriseId, cameraId)

Get all cameras for a enterprise

List all cameras for a enterprise.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.VideosApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: accessCode
OAuth accessCode = (OAuth) defaultClient.getAuthentication("accessCode");
accessCode.setAccessToken("YOUR ACCESS TOKEN");

VideosApi apiInstance = new VideosApi();
UUID enterpriseId = new UUID(); // UUID | enterprise Id
UUID cameraId = new UUID(); // UUID | Camera Id
try {
    Cameras result = apiInstance.enterpriseIdCameraIdVideosGet(enterpriseId, cameraId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling VideosApi#enterpriseIdCameraIdVideosGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterpriseId** | [**UUID**](.md)| enterprise Id |
 **cameraId** | [**UUID**](.md)| Camera Id |

### Return type

[**Cameras**](Cameras.md)

### Authorization

[accessCode](../README.md#accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

