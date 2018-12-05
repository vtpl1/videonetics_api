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

import io.swagger.client.ApiException;
import io.swagger.client.model.Cameras;
import java.util.UUID;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CamerasApi
 */
@Ignore
public class CamerasApiTest {

    private final CamerasApi api = new CamerasApi();

    /**
     * Get all cameras for a enterprise
     *
     * List all cameras for a enterprise.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void enterpriseIdCamerasGetTest() throws ApiException {
        UUID enterpriseId = null;
        Cameras response = api.enterpriseIdCamerasGet(enterpriseId);

        // TODO: test validations
    }
}
