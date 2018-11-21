package io.swagger.api;

import io.swagger.model.Enterprise;
import io.swagger.model.EnterpriseDetail;
import io.swagger.model.Enterprises;
import java.util.UUID;

import java.util.*;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.test.context.junit4.SpringRunner;

import static org.junit.Assert.assertEquals;

@RunWith(SpringRunner.class)
@SpringBootTest
public class EnterprisesApiControllerIntegrationTest {

    @Autowired
    private EnterprisesApi api;

    @Test
    public void enterprisesEnterpriseIdDetailsGetTest() throws Exception {
        UUID enterpriseId = new UUID();
        ResponseEntity<EnterpriseDetail> responseEntity = api.enterprisesEnterpriseIdDetailsGet(enterpriseId);
        assertEquals(HttpStatus.NOT_IMPLEMENTED, responseEntity.getStatusCode());
    }

    @Test
    public void enterprisesGetTest() throws Exception {
        ResponseEntity<Enterprises> responseEntity = api.enterprisesGet();
        assertEquals(HttpStatus.NOT_IMPLEMENTED, responseEntity.getStatusCode());
    }

    @Test
    public void enterprisesPostTest() throws Exception {
        UUID body = new UUID();
        ResponseEntity<Enterprise> responseEntity = api.enterprisesPost(body);
        assertEquals(HttpStatus.NOT_IMPLEMENTED, responseEntity.getStatusCode());
    }

}
