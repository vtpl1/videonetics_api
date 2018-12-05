package io.swagger.api;

import io.swagger.model.Cameras;
import io.swagger.model.Event;
import io.swagger.model.Events;
import io.swagger.model.Tags;
import java.util.UUID;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.swagger.annotations.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.constraints.*;
import javax.validation.Valid;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;
import java.util.List;
import java.util.Map;
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2018-12-05T09:37:54.774Z[GMT]")

@Controller
public class EnterpriseIdApiController implements EnterpriseIdApi {

    private static final Logger log = LoggerFactory.getLogger(EnterpriseIdApiController.class);

    private final ObjectMapper objectMapper;

    private final HttpServletRequest request;

    @org.springframework.beans.factory.annotation.Autowired
    public EnterpriseIdApiController(ObjectMapper objectMapper, HttpServletRequest request) {
        this.objectMapper = objectMapper;
        this.request = request;
    }

    public ResponseEntity<Cameras> enterpriseIdCameraIdVideosGet(@ApiParam(value = "enterprise Id",required=true) @PathVariable("enterpriseId") UUID enterpriseId,@ApiParam(value = "Camera Id",required=true) @PathVariable("cameraId") UUID cameraId) {
        String accept = request.getHeader("Accept");
        return new ResponseEntity<Cameras>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<Cameras> enterpriseIdCamerasGet(@ApiParam(value = "enterprise Id",required=true) @PathVariable("enterpriseId") UUID enterpriseId) {
        String accept = request.getHeader("Accept");
        return new ResponseEntity<Cameras>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<Events> enterpriseIdEventsGet(@ApiParam(value = "enterprise Id",required=true) @PathVariable("enterpriseId") UUID enterpriseId) {
        String accept = request.getHeader("Accept");
        return new ResponseEntity<Events>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<Event> enterpriseIdEventsPost(@ApiParam(value = "enterprise Id",required=true) @PathVariable("enterpriseId") UUID enterpriseId) {
        String accept = request.getHeader("Accept");
        return new ResponseEntity<Event>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<Tags> enterpriseIdTagsGet(@ApiParam(value = "enterprise Id",required=true) @PathVariable("enterpriseId") UUID enterpriseId) {
        String accept = request.getHeader("Accept");
        return new ResponseEntity<Tags>(HttpStatus.NOT_IMPLEMENTED);
    }

}
