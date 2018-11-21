package io.swagger.api;

import io.swagger.model.Cameras;
import io.swagger.model.Event;
import io.swagger.model.Events;
import io.swagger.model.Tags;
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
public class EnterpriseIdApiControllerIntegrationTest {

    @Autowired
    private EnterpriseIdApi api;

    @Test
    public void enterpriseIdCameraIdVideosGetTest() throws Exception {
        UUID enterpriseId = new UUID();
        UUID cameraId = new UUID();
        ResponseEntity<Cameras> responseEntity = api.enterpriseIdCameraIdVideosGet(enterpriseId, cameraId);
        assertEquals(HttpStatus.NOT_IMPLEMENTED, responseEntity.getStatusCode());
    }

    @Test
    public void enterpriseIdCamerasGetTest() throws Exception {
        UUID enterpriseId = new UUID();
        ResponseEntity<Cameras> responseEntity = api.enterpriseIdCamerasGet(enterpriseId);
        assertEquals(HttpStatus.NOT_IMPLEMENTED, responseEntity.getStatusCode());
    }

    @Test
    public void enterpriseIdEventsGetTest() throws Exception {
        UUID enterpriseId = new UUID();
        ResponseEntity<Events> responseEntity = api.enterpriseIdEventsGet(enterpriseId);
        assertEquals(HttpStatus.NOT_IMPLEMENTED, responseEntity.getStatusCode());
    }

    @Test
    public void enterpriseIdEventsPostTest() throws Exception {
        UUID enterpriseId = new UUID();
        ResponseEntity<Event> responseEntity = api.enterpriseIdEventsPost(enterpriseId);
        assertEquals(HttpStatus.NOT_IMPLEMENTED, responseEntity.getStatusCode());
    }

    @Test
    public void enterpriseIdTagsGetTest() throws Exception {
        UUID enterpriseId = new UUID();
        ResponseEntity<Tags> responseEntity = api.enterpriseIdTagsGet(enterpriseId);
        assertEquals(HttpStatus.NOT_IMPLEMENTED, responseEntity.getStatusCode());
    }

}
