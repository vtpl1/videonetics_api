# CamerasApi

All URIs are relative to *https://virtserver.swaggerhub.com/videonetics/visna/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterpriseIdCamerasGet**](CamerasApi.md#enterpriseIdCamerasGet) | **GET** /{enterpriseId}/cameras | Get all cameras for a enterprise

<a name="enterpriseIdCamerasGet"></a>
# **enterpriseIdCamerasGet**
> Cameras enterpriseIdCamerasGet(enterpriseId)

Get all cameras for a enterprise

List all cameras for a enterprise.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.CamerasApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: accessCode
OAuth accessCode = (OAuth) defaultClient.getAuthentication("accessCode");
accessCode.setAccessToken("YOUR ACCESS TOKEN");

CamerasApi apiInstance = new CamerasApi();
UUID enterpriseId = new UUID(); // UUID | enterprise Id
try {
    Cameras result = apiInstance.enterpriseIdCamerasGet(enterpriseId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CamerasApi#enterpriseIdCamerasGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterpriseId** | [**UUID**](.md)| enterprise Id |

### Return type

[**Cameras**](Cameras.md)

### Authorization

[accessCode](../README.md#accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

