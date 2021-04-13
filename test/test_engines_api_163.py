import unittest
from pprint import pprint

import json
import vtpl_api
from vtpl_api.api.engines_api import EnginesApi  # noqa: E501
from vtpl_api.api_client import ApiClient
from vtpl_api.configuration import Configuration
from vtpl_api.models.engine_task import EngineTask
from vtpl_api.rest import ApiException
from vtpl_api.models.va_event import VaEvent
from vtpl_api.models.meta_va_event import MetaVaEvent
from vtpl_api.models.event_details import EventDetails
from vtpl_api.models.snap import Snap
import uuid


class TestEnginesApi(unittest.TestCase):
    """EnginesApi unit test stubs"""

    def setUp(self):
        self.configuration = Configuration()
        self.configuration.host = "http://192.168.1.163:2050"

        self.api = EnginesApi(api_client=ApiClient(self.configuration))  # noqa: E501

    def tearDown(self):
        pass

    def test_engine_tasks_get(self):
        """Test case for engine_tasks_get

        Get all engineTasks  # noqa: E501
        """
        return
        try:
            # Get all engineTasks
            api_response = self.api.engine_tasks_get()
            assert len(api_response.items) > 0
            for item in api_response.items:
                assert len(item.source.source_list) > 0
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EnginesApi->engine_tasks_get: %s\n" % e)

    def test_patch_clean_engine_tasks(self):
        return

        try:
            # Get all engineTasks
            api_response = self.api.engine_tasks_get()
            for item in api_response.items:
                #item.engine_machine_id = None
                etag = item.etag
                id = item.id
                #item.etag = None
                #item.id = None
                #item.links = None
                body = {}
                body["engineMachineId"] = None
                print(f"id:{id} body:{body}")
                api_response2 = self.api.engine_tasks_id_patch(
                    if_match=etag, id=id, body=body)
                pprint(api_response2)
        except ApiException as e:
            print("Exception when calling EnginesApi->engine_tasks_id_patch: %s\n" % e)
            assert (False)

    def test_engine_task_state_machine(self):
        # 1 get engine tasks
        # 2 patch with machine id

        capabilties = [201, 207]
        max_channels = 2
        my_id = 'monotosh'
        vs3_host_name = 'http://192.168.1.163:2080'
        try:
            # Get all engineTasks
            #where={"$or": [ { "$and": [{"capbilitiesType": { "$in": [201, 207] } }, {"engineMachineId": { "$exists": false } }] }, {"engineMachineId": "monotosh"} ]}
            #where={"$and": [{"$or": [ { "$and": [{"capbilitiesType": { "$in": [201, 207] } }, {"engineMachineId": { "$exists": false } }] }, {"engineMachineId": "monotosh"} ]}, { "isExpired": false }]}
            # &sort=[('created', -1)]
            # &maxResults=1

            where = {"$and": [{"$or": [{"$and": [{"capbilitiesType": {"$in": capabilties}}, {
                "engineMachineId": {"$exists": False}}]}, {"engineMachineId": my_id}]}, {"isExpired": False}]}
            sort = [('created', -1)]
            maxResults = max_channels

            str_where = json.dumps(where)  # str(where).replace("'", "\"")
            print(f"where : {str_where}")

            api_response = self.api.engine_tasks_get(where=json.dumps(
                where), sort=json.dumps(sort), max_results=json.dumps(maxResults))
            assert len(api_response.items) > 0
            assert len(api_response.items) <= max_channels

            for item in api_response.items:
                assert len(item.source.source_list) > 0
                etag = item.etag
                id = item.id

                # assign tasks
                if True:
                    try:
                        api_response2 = self.api.engine_tasks_id_patch(
                            if_match=etag, id=id, body=json.dumps({"engineMachineId": my_id}))
                        pprint(api_response2)
                        assert api_response2.status == 'OK'
                        etag = api_response2.etag
                        id = api_response2.id
                        # process Tasks
                        # generate events

                        try:
                            snap_url = f'{vs3_host_name}/api/motion/1618288200000-1618288260000/5.png'
                            event_snap = Snap(
                                snap=snap_url, snap_id=str(uuid.uuid4()))
                            print(f"monotosh: event_snap {event_snap}")
                            api_response5 = self.api.event_snaps_post(
                                body=event_snap)

                        except ApiException as e:
                            print(
                                "Exception when calling EnginesApi->va_events_post: %s\n" % e)
                            assert (False)

                        try:
                            va_event = VaEvent()
                            va_event.capbilities_type = item.capbilities_type
                            va_event.meta_va_event = MetaVaEvent(count=1)
                            va_event.event_details = EventDetails(
                                engine_task_id=item.id, start_time_stamp=item.source.start_time_stamp, end_time_stamp=item.source.end_time_stamp)
                            va_event.event_snaps = [api_response5.id]
                            va_event.event_clips = []

                            print(f"va_event: {va_event}")
                            api_response4 = self.api.va_events_post(
                                body=va_event)
                        except ApiException as e:
                            print(
                                "Exception when calling EnginesApi->va_events_post: %s\n" % e)
                            assert (False)

                        if True:
                            try:
                                api_response3 = self.api.engine_tasks_id_patch(
                                    if_match=etag, id=id, body=json.dumps({"isExpired": True}))
                                pprint(api_response3)
                                assert api_response3.status == 'OK'
                                etag = api_response3.etag
                                id = api_response3.id
                            except ApiException as e:
                                print(
                                    "Exception when calling EnginesApi->engine_tasks_id_patch: %s\n" % e)
                                assert (False)

                    except ApiException as e:
                        print(
                            "Exception when calling EnginesApi->engine_tasks_id_patch: %s\n" % e)
                        assert (False)
            # pprint(api_response)
        except ApiException as e:
            print("Exception when calling EnginesApi->engine_tasks_get: %s\n" % e)

        pass
