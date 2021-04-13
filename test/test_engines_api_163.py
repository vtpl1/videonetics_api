import unittest
from vtpl_api.api_client import ApiClient
from vtpl_api.configuration import Configuration

import vtpl_api
from vtpl_api.api.engines_api import EnginesApi  # noqa: E501
from vtpl_api.rest import ApiException
from pprint import pprint


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
        try:
            # Get all engineTasks
            api_response = self.api.engine_tasks_get()
            for item in api_response.items:
                body = {}
                body["engine_machine_id"] = None
                print(f"etag: {item.etag} id:{item.id} body:{body}")
                api_response2 = self.api.engine_tasks_id_patch(
                    if_match=item.etag, id=item.id, body=body)
                pprint(api_response2)
        except ApiException as e:
            print("Exception when calling EnginesApi->engine_tasks_id_patch: %s\n" % e)
