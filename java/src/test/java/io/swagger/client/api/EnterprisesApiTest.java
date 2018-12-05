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
import io.swagger.client.model.Enterprise;
import io.swagger.client.model.EnterpriseDetail;
import io.swagger.client.model.Enterprises;
import java.util.UUID;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for EnterprisesApi
 */
@Ignore
public class EnterprisesApiTest {

    private final EnterprisesApi api = new EnterprisesApi();

    /**
     * Get enterprises with details
     *
     * List all enterprises available.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void enterprisesEnterpriseIdDetailsGetTest() throws ApiException {
        UUID enterpriseId = null;
        EnterpriseDetail response = api.enterprisesEnterpriseIdDetailsGet(enterpriseId);

        // TODO: test validations
    }
    /**
     * Get enterprises list
     *
     * List all enterprises available.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void enterprisesGetTest() throws ApiException {
        Enterprises response = api.enterprisesGet();

        // TODO: test validations
    }
    /**
     * Add new enterprise
     *
     * Add new enterprise.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void enterprisesPostTest() throws ApiException {
        UUID body = null;
        Enterprise response = api.enterprisesPost(body);

        // TODO: test validations
    }
}
