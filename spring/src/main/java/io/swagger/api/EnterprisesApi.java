/**
 * NOTE: This class is auto generated by the swagger code generator program (3.0.2).
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */
package io.swagger.api;

import io.swagger.model.Enterprise;
import io.swagger.model.EnterpriseDetail;
import io.swagger.model.Enterprises;
import java.util.UUID;
import io.swagger.annotations.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.Valid;
import javax.validation.constraints.*;
import java.util.List;
import java.util.Map;
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2018-11-21T13:08:36.940Z[GMT]")

@Api(value = "enterprises", description = "the enterprises API")
public interface EnterprisesApi {

    @ApiOperation(value = "Get enterprises with details", nickname = "enterprisesEnterpriseIdDetailsGet", notes = "List all enterprises available.", response = EnterpriseDetail.class, authorizations = {
        @Authorization(value = "accessCode", scopes = {
            @AuthorizationScope(scope = "", description = "")
            })
    }, tags={ "enterprises", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Get all enterprises", response = EnterpriseDetail.class) })
    @RequestMapping(value = "/enterprises/{enterpriseId}/details",
        produces = { "application/json" }, 
        method = RequestMethod.GET)
    ResponseEntity<EnterpriseDetail> enterprisesEnterpriseIdDetailsGet(@ApiParam(value = "enterprise Id",required=true) @PathVariable("enterpriseId") UUID enterpriseId);


    @ApiOperation(value = "Get enterprises list", nickname = "enterprisesGet", notes = "List all enterprises available.", response = Enterprises.class, authorizations = {
        @Authorization(value = "accessCode", scopes = {
            @AuthorizationScope(scope = "", description = "")
            })
    }, tags={ "enterprises", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Get all enterprises", response = Enterprises.class) })
    @RequestMapping(value = "/enterprises",
        produces = { "application/json" }, 
        method = RequestMethod.GET)
    ResponseEntity<Enterprises> enterprisesGet();


    @ApiOperation(value = "Add new enterprise", nickname = "enterprisesPost", notes = "Add new enterprise.", response = Enterprise.class, authorizations = {
        @Authorization(value = "accessCode", scopes = {
            @AuthorizationScope(scope = "", description = "")
            })
    }, tags={ "enterprises", })
    @ApiResponses(value = { 
        @ApiResponse(code = 201, message = "Get all enterprises", response = Enterprise.class) })
    @RequestMapping(value = "/enterprises",
        produces = { "application/json" }, 
        consumes = { "application/json" },
        method = RequestMethod.POST)
    ResponseEntity<Enterprise> enterprisesPost(@ApiParam(value = ""  )  @Valid @RequestBody UUID body);

}
