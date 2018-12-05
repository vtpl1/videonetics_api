# EnterprisesApi

All URIs are relative to *https://virtserver.swaggerhub.com/videonetics/visna/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprisesEnterpriseIdDetailsGet**](EnterprisesApi.md#enterprisesEnterpriseIdDetailsGet) | **GET** /enterprises/{enterpriseId}/details | Get enterprises with details
[**enterprisesGet**](EnterprisesApi.md#enterprisesGet) | **GET** /enterprises | Get enterprises list
[**enterprisesPost**](EnterprisesApi.md#enterprisesPost) | **POST** /enterprises | Add new enterprise

<a name="enterprisesEnterpriseIdDetailsGet"></a>
# **enterprisesEnterpriseIdDetailsGet**
> EnterpriseDetail enterprisesEnterpriseIdDetailsGet(enterpriseId)

Get enterprises with details

List all enterprises available.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.EnterprisesApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: accessCode
OAuth accessCode = (OAuth) defaultClient.getAuthentication("accessCode");
accessCode.setAccessToken("YOUR ACCESS TOKEN");

EnterprisesApi apiInstance = new EnterprisesApi();
UUID enterpriseId = new UUID(); // UUID | enterprise Id
try {
    EnterpriseDetail result = apiInstance.enterprisesEnterpriseIdDetailsGet(enterpriseId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling EnterprisesApi#enterprisesEnterpriseIdDetailsGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterpriseId** | [**UUID**](.md)| enterprise Id |

### Return type

[**EnterpriseDetail**](EnterpriseDetail.md)

### Authorization

[accessCode](../README.md#accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="enterprisesGet"></a>
# **enterprisesGet**
> Enterprises enterprisesGet()

Get enterprises list

List all enterprises available.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.EnterprisesApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: accessCode
OAuth accessCode = (OAuth) defaultClient.getAuthentication("accessCode");
accessCode.setAccessToken("YOUR ACCESS TOKEN");

EnterprisesApi apiInstance = new EnterprisesApi();
try {
    Enterprises result = apiInstance.enterprisesGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling EnterprisesApi#enterprisesGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Enterprises**](Enterprises.md)

### Authorization

[accessCode](../README.md#accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="enterprisesPost"></a>
# **enterprisesPost**
> Enterprise enterprisesPost(body)

Add new enterprise

Add new enterprise.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.EnterprisesApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure OAuth2 access token for authorization: accessCode
OAuth accessCode = (OAuth) defaultClient.getAuthentication("accessCode");
accessCode.setAccessToken("YOUR ACCESS TOKEN");

EnterprisesApi apiInstance = new EnterprisesApi();
UUID body = new UUID(); // UUID | 
try {
    Enterprise result = apiInstance.enterprisesPost(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling EnterprisesApi#enterprisesPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UUID**](UUID.md)|  | [optional]

### Return type

[**Enterprise**](Enterprise.md)

### Authorization

[accessCode](../README.md#accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

