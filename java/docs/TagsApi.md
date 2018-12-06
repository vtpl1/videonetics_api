# TagsApi

All URIs are relative to *https://v2.videonetics.com:5000/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterpriseIdTagsGet**](TagsApi.md#enterpriseIdTagsGet) | **GET** /{enterpriseId}/tags | Get all tags for a enterprise

<a name="enterpriseIdTagsGet"></a>
# **enterpriseIdTagsGet**
> Tags enterpriseIdTagsGet(enterpriseId)

Get all tags for a enterprise

List all tags available for a enterprise.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.TagsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: accessCode
OAuth accessCode = (OAuth) defaultClient.getAuthentication("accessCode");
accessCode.setAccessToken("YOUR ACCESS TOKEN");

TagsApi apiInstance = new TagsApi();
UUID enterpriseId = new UUID(); // UUID | enterprise Id
try {
    Tags result = apiInstance.enterpriseIdTagsGet(enterpriseId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TagsApi#enterpriseIdTagsGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterpriseId** | [**UUID**](.md)| enterprise Id |

### Return type

[**Tags**](Tags.md)

### Authorization

[accessCode](../README.md#accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

