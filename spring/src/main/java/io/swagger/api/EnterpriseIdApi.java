/**
 * NOTE: This class is auto generated by the swagger code generator program (3.0.2).
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */
package io.swagger.api;

import io.swagger.model.Cameras;
import io.swagger.model.Event;
import io.swagger.model.Events;
import io.swagger.model.Tags;
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
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2018-12-05T07:09:15.776Z[GMT]")

@Api(value = "{enterpriseId}", description = "the {enterpriseId} API")
public interface EnterpriseIdApi {

    @ApiOperation(value = "Get all cameras for a enterprise", nickname = "enterpriseIdCameraIdVideosGet", notes = "List all cameras for a enterprise.", response = Cameras.class, tags={ "videos", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Get all cameras for a enterprise", response = Cameras.class) })
    @RequestMapping(value = "/{enterpriseId}/{cameraId}/videos",
        produces = { "application/json" }, 
        method = RequestMethod.GET)
    ResponseEntity<Cameras> enterpriseIdCameraIdVideosGet(@ApiParam(value = "enterprise Id",required=true) @PathVariable("enterpriseId") UUID enterpriseId,@ApiParam(value = "Camera Id",required=true) @PathVariable("cameraId") UUID cameraId);


    @ApiOperation(value = "Get all cameras for a enterprise", nickname = "enterpriseIdCamerasGet", notes = "List all cameras for a enterprise.", response = Cameras.class, tags={ "cameras", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Get all cameras for a enterprise", response = Cameras.class) })
    @RequestMapping(value = "/{enterpriseId}/cameras",
        produces = { "application/json" }, 
        method = RequestMethod.GET)
    ResponseEntity<Cameras> enterpriseIdCamerasGet(@ApiParam(value = "enterprise Id",required=true) @PathVariable("enterpriseId") UUID enterpriseId);


    @ApiOperation(value = "Get events list", nickname = "enterpriseIdEventsGet", notes = "List all the events available.", response = Events.class, tags={ "events", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "get all events", response = Events.class) })
    @RequestMapping(value = "/{enterpriseId}/events",
        produces = { "application/json" }, 
        method = RequestMethod.GET)
    ResponseEntity<Events> enterpriseIdEventsGet(@ApiParam(value = "enterprise Id",required=true) @PathVariable("enterpriseId") UUID enterpriseId);


    @ApiOperation(value = "Create new event", nickname = "enterpriseIdEventsPost", notes = "Create new event.", response = Event.class, tags={ "events", })
    @ApiResponses(value = { 
        @ApiResponse(code = 201, message = "pet response", response = Event.class) })
    @RequestMapping(value = "/{enterpriseId}/events",
        produces = { "application/json" }, 
        method = RequestMethod.POST)
    ResponseEntity<Event> enterpriseIdEventsPost(@ApiParam(value = "enterprise Id",required=true) @PathVariable("enterpriseId") UUID enterpriseId);


    @ApiOperation(value = "Get all tags for a enterprise", nickname = "enterpriseIdTagsGet", notes = "List all tags available for a enterprise.", response = Tags.class, tags={ "tags", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Get all tags", response = Tags.class) })
    @RequestMapping(value = "/{enterpriseId}/tags",
        produces = { "application/json" }, 
        method = RequestMethod.GET)
    ResponseEntity<Tags> enterpriseIdTagsGet(@ApiParam(value = "enterprise Id",required=true) @PathVariable("enterpriseId") UUID enterpriseId);

}
