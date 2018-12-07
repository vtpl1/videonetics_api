# swagger-java-client

## Requirements

Building the API client library requires [Maven](https://maven.apache.org/) to be installed.

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn deploy
```

Refer to the [official documentation](https://maven.apache.org/plugins/maven-deploy-plugin/usage.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-java-client</artifactId>
    <version>1.0.0</version>
    <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "io.swagger:swagger-java-client:1.0.0"
```

### Others

At first generate the JAR by executing:

    mvn package

Then manually install the following JARs:

* target/swagger-java-client-1.0.0.jar
* target/lib/*.jar

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.CamerasApi;

import java.io.File;
import java.util.*;

public class CamerasApiExample {

    public static void main(String[] args) {
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
    }
}
```

## Documentation for API Endpoints

All URIs are relative to *http://v2.videonetics.com:5000/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CamerasApi* | [**enterpriseIdCamerasGet**](docs/CamerasApi.md#enterpriseIdCamerasGet) | **GET** /{enterpriseId}/cameras | Get all cameras for a enterprise
*EnterprisesApi* | [**enterprisesEnterpriseIdDetailsGet**](docs/EnterprisesApi.md#enterprisesEnterpriseIdDetailsGet) | **GET** /enterprises/{enterpriseId}/details | Get enterprises with details
*EnterprisesApi* | [**enterprisesGet**](docs/EnterprisesApi.md#enterprisesGet) | **GET** /enterprises | Get enterprises list
*EnterprisesApi* | [**enterprisesPost**](docs/EnterprisesApi.md#enterprisesPost) | **POST** /enterprises | Add new enterprise
*EventsApi* | [**enterpriseIdEventsGet**](docs/EventsApi.md#enterpriseIdEventsGet) | **GET** /{enterpriseId}/events | Get events list
*EventsApi* | [**enterpriseIdEventsPost**](docs/EventsApi.md#enterpriseIdEventsPost) | **POST** /{enterpriseId}/events | Create new event
*TagsApi* | [**enterpriseIdTagsGet**](docs/TagsApi.md#enterpriseIdTagsGet) | **GET** /{enterpriseId}/tags | Get all tags for a enterprise
*UsersApi* | [**usersGet**](docs/UsersApi.md#usersGet) | **GET** /users | Get all users
*UsersApi* | [**usersPost**](docs/UsersApi.md#usersPost) | **POST** /users | Create a Gloabal System level user
*VideosApi* | [**enterpriseIdCameraIdVideosGet**](docs/VideosApi.md#enterpriseIdCameraIdVideosGet) | **GET** /{enterpriseId}/{cameraId}/videos | Get all cameras for a enterprise

## Documentation for Models

 - [AccessStatus](docs/AccessStatus.md)
 - [BoundingBox](docs/BoundingBox.md)
 - [BoundingPoly](docs/BoundingPoly.md)
 - [Camera](docs/Camera.md)
 - [Cameras](docs/Cameras.md)
 - [Enterprise](docs/Enterprise.md)
 - [EnterpriseAccountStatus](docs/EnterpriseAccountStatus.md)
 - [EnterpriseDetail](docs/EnterpriseDetail.md)
 - [Enterprises](docs/Enterprises.md)
 - [Event](docs/Event.md)
 - [Events](docs/Events.md)
 - [FaceAnnotation](docs/FaceAnnotation.md)
 - [FaceAnnotations](docs/FaceAnnotations.md)
 - [FaceAttributes](docs/FaceAttributes.md)
 - [FavouriteTag](docs/FavouriteTag.md)
 - [GroupTag](docs/GroupTag.md)
 - [HeatMap](docs/HeatMap.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [LabelAnnotation](docs/LabelAnnotation.md)
 - [LabelAnnotations](docs/LabelAnnotations.md)
 - [Locale](docs/Locale.md)
 - [Location](docs/Location.md)
 - [LocationTag](docs/LocationTag.md)
 - [OtherTag](docs/OtherTag.md)
 - [Tags](docs/Tags.md)
 - [TextAnnotation](docs/TextAnnotation.md)
 - [TextAnnotations](docs/TextAnnotations.md)
 - [User](docs/User.md)
 - [UserRole](docs/UserRole.md)
 - [Users](docs/Users.md)
 - [Vertex](docs/Vertex.md)
 - [VertexWithValue](docs/VertexWithValue.md)

## Documentation for Authorization

Authentication schemes defined for the API:
### accessCode

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://accounts.google.com/o/oauth2/auth
- **Scopes**: 
  - : 


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author


