/*
 * Videonetics Visual Computing Platform
 * API to access the Videonetics Visual Computing Platform for analytics events
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.api;

import io.swagger.client.ApiCallback;
import io.swagger.client.ApiClient;
import io.swagger.client.ApiException;
import io.swagger.client.ApiResponse;
import io.swagger.client.Configuration;
import io.swagger.client.Pair;
import io.swagger.client.ProgressRequestBody;
import io.swagger.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import io.swagger.client.model.Cameras;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class VideosApi {
    private ApiClient apiClient;

    public VideosApi() {
        this(Configuration.getDefaultApiClient());
    }

    public VideosApi(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return apiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    /**
     * Build call for enterpriseIdCameraIdVideosGet
     * @param enterpriseId enterprise Id (required)
     * @param cameraId Camera Id (required)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call enterpriseIdCameraIdVideosGetCall(UUID enterpriseId, UUID cameraId, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = null;
        
        // create path and map variables
        String localVarPath = "/{enterpriseId}/{cameraId}/videos"
            .replaceAll("\\{" + "enterpriseId" + "\\}", apiClient.escapeString(enterpriseId.toString()))
            .replaceAll("\\{" + "cameraId" + "\\}", apiClient.escapeString(cameraId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            
        };
        final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        if(progressListener != null) {
            apiClient.getHttpClient().networkInterceptors().add(new com.squareup.okhttp.Interceptor() {
                @Override
                public com.squareup.okhttp.Response intercept(com.squareup.okhttp.Interceptor.Chain chain) throws IOException {
                    com.squareup.okhttp.Response originalResponse = chain.proceed(chain.request());
                    return originalResponse.newBuilder()
                    .body(new ProgressResponseBody(originalResponse.body(), progressListener))
                    .build();
                }
            });
        }

        String[] localVarAuthNames = new String[] { "accessCode" };
        return apiClient.buildCall(localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }
    
    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call enterpriseIdCameraIdVideosGetValidateBeforeCall(UUID enterpriseId, UUID cameraId, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'enterpriseId' is set
        if (enterpriseId == null) {
            throw new ApiException("Missing the required parameter 'enterpriseId' when calling enterpriseIdCameraIdVideosGet(Async)");
        }
        // verify the required parameter 'cameraId' is set
        if (cameraId == null) {
            throw new ApiException("Missing the required parameter 'cameraId' when calling enterpriseIdCameraIdVideosGet(Async)");
        }
        
        com.squareup.okhttp.Call call = enterpriseIdCameraIdVideosGetCall(enterpriseId, cameraId, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * Get all cameras for a enterprise
     * List all cameras for a enterprise.
     * @param enterpriseId enterprise Id (required)
     * @param cameraId Camera Id (required)
     * @return Cameras
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public Cameras enterpriseIdCameraIdVideosGet(UUID enterpriseId, UUID cameraId) throws ApiException {
        ApiResponse<Cameras> resp = enterpriseIdCameraIdVideosGetWithHttpInfo(enterpriseId, cameraId);
        return resp.getData();
    }

    /**
     * Get all cameras for a enterprise
     * List all cameras for a enterprise.
     * @param enterpriseId enterprise Id (required)
     * @param cameraId Camera Id (required)
     * @return ApiResponse&lt;Cameras&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Cameras> enterpriseIdCameraIdVideosGetWithHttpInfo(UUID enterpriseId, UUID cameraId) throws ApiException {
        com.squareup.okhttp.Call call = enterpriseIdCameraIdVideosGetValidateBeforeCall(enterpriseId, cameraId, null, null);
        Type localVarReturnType = new TypeToken<Cameras>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     * Get all cameras for a enterprise (asynchronously)
     * List all cameras for a enterprise.
     * @param enterpriseId enterprise Id (required)
     * @param cameraId Camera Id (required)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call enterpriseIdCameraIdVideosGetAsync(UUID enterpriseId, UUID cameraId, final ApiCallback<Cameras> callback) throws ApiException {

        ProgressResponseBody.ProgressListener progressListener = null;
        ProgressRequestBody.ProgressRequestListener progressRequestListener = null;

        if (callback != null) {
            progressListener = new ProgressResponseBody.ProgressListener() {
                @Override
                public void update(long bytesRead, long contentLength, boolean done) {
                    callback.onDownloadProgress(bytesRead, contentLength, done);
                }
            };

            progressRequestListener = new ProgressRequestBody.ProgressRequestListener() {
                @Override
                public void onRequestProgress(long bytesWritten, long contentLength, boolean done) {
                    callback.onUploadProgress(bytesWritten, contentLength, done);
                }
            };
        }

        com.squareup.okhttp.Call call = enterpriseIdCameraIdVideosGetValidateBeforeCall(enterpriseId, cameraId, progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<Cameras>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
}
