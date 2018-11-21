package io.swagger.api;

import io.swagger.model.Enterprise;
import io.swagger.model.EnterpriseDetail;
import io.swagger.model.Enterprises;
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
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2018-11-21T13:08:36.940Z[GMT]")

@Controller
public class EnterprisesApiController implements EnterprisesApi {

    private static final Logger log = LoggerFactory.getLogger(EnterprisesApiController.class);

    private final ObjectMapper objectMapper;

    private final HttpServletRequest request;

    @org.springframework.beans.factory.annotation.Autowired
    public EnterprisesApiController(ObjectMapper objectMapper, HttpServletRequest request) {
        this.objectMapper = objectMapper;
        this.request = request;
    }

    public ResponseEntity<EnterpriseDetail> enterprisesEnterpriseIdDetailsGet(@ApiParam(value = "enterprise Id",required=true) @PathVariable("enterpriseId") UUID enterpriseId) {
        String accept = request.getHeader("Accept");
        return new ResponseEntity<EnterpriseDetail>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<Enterprises> enterprisesGet() {
        String accept = request.getHeader("Accept");
        return new ResponseEntity<Enterprises>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<Enterprise> enterprisesPost(@ApiParam(value = ""  )  @Valid @RequestBody UUID body) {
        String accept = request.getHeader("Accept");
        return new ResponseEntity<Enterprise>(HttpStatus.NOT_IMPLEMENTED);
    }

}
