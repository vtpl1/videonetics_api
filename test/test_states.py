import json
import logging
import time
from typing import Any, List, Tuple

import pytest
import requests
import urllib3
from vtpl_api.api.engines_api import EnginesApi
from vtpl_api.api_client import ApiClient
from vtpl_api.configuration import Configuration
from vtpl_api.models import engine_task, engine_task_status_failure
from vtpl_api.models.engine_task import EngineTask
from vtpl_api.models.engine_task_status import EngineTaskStatus
from vtpl_api.models.engine_task_status_failure import EngineTaskStatusFailure
from vtpl_api.models.engine_task_status_progress import \
    EngineTaskStatusProgress
from vtpl_api.models.event_details import EventDetails
from vtpl_api.models.meta_va_event import MetaVaEvent
from vtpl_api.models.snap import Snap
from vtpl_api.models.source_end_point import SourceEndPoint
from vtpl_api.models.source_end_point_source_list import \
    SourceEndPointSourceList
from vtpl_api.models.source_type import SourceType
from vtpl_api.models.va_event import VaEvent
from vtpl_api.rest import ApiException

# LOGGER.addHandler(logging.StreamHandler())


class DeeperLookApi:
    def __init__(self) -> None:
        host_name = "http://10.0.0.103"
        api_host = f"{host_name}:5000"
        config = Configuration()
        config.host = api_host
        self.vs3_host = f"{host_name}:9983"
        self.__api = EnginesApi(api_client=ApiClient(config))

    def get_jobs(self, capabilties, max_channels, my_id) -> List[EngineTask]:
        assert capabilties is not None
        assert max_channels > 0
        assert my_id is not None
        items = []
        try:
            # Get all engineTasks
            # where={"$or": [ { "$and": [{"capbilitiesType": { "$in": [201, 207] } }, {"engineMachineId": { "$exists": false } }] }, {"engineMachineId": "monotosh"} ]}
            # where={"$and": [{"$or": [ { "$and": [{"capbilitiesType": { "$in": [201, 207] } }, {"engineMachineId": { "$exists": false } }] }, {"engineMachineId": "monotosh"} ]}, { "isExpired": false }]}
            # &sort=[('created', -1)]
            # &maxResults=1

            where = {
                "$and": [
                    {
                        "$or": [
                            {
                                "$and": [
                                    {"capbilitiesType": {"$in": capabilties}},
                                    {"engineMachineId": {"$exists": False}},
                                ]
                            },
                            {"engineMachineId": my_id},
                        ]
                    },
                    {"isExpired": False},
                ]
            }
            logging.info(f"The where clause: {json.dumps(where)}")
            sort = [("created", -1)]
            max_results = max_channels
            api_response = self.__api.engine_tasks_get(
                where=json.dumps(where),
                sort=json.dumps(sort),
                max_results=json.dumps(max_results),
            )
            assert len(api_response.items) <= max_channels
            items = api_response.items
        except ApiException as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_get: %s\n" % e)
        except urllib3.exceptions.MaxRetryError as e:
            logging.error("Monotosh Exception when calling EnginesApi->engine_tasks_get: %s\n" % type(e))
        return items

    def flag_start_job(self, job_id: str, my_id: str) -> bool:
        assert job_id is not None
        assert len(job_id) > 0

        assert my_id is not None
        assert len(my_id) > 0
        ret = False
        etag = None

        try:
            api_response = self.__api.engine_tasks_id_get(job_id)
            assert api_response.id == job_id
            etag = api_response.etag
            # logging.info(api_response)

        except ApiException as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % e)
        except urllib3.exceptions.MaxRetryError as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % type(e))
        assert etag is not None
        try:
            api_response = self.__api.engine_tasks_id_patch(
                if_match=etag, id=job_id, body=json.dumps({"engineMachineId": my_id})
            )
            ret = True
        except ApiException as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_patch: %s\n" % e)
        except urllib3.exceptions.MaxRetryError as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_patch: %s\n" % type(e))

        return ret

    def flag_finish_job(self, job_id: str, my_id: str) -> bool:
        assert job_id is not None
        assert len(job_id) > 0

        assert my_id is not None
        assert len(my_id) > 0
        ret = False
        etag = None

        try:
            api_response = self.__api.engine_tasks_id_get(job_id)
            assert api_response.id == job_id
            etag = api_response.etag
            # logging.info(api_response)

        except ApiException as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % e)
        except urllib3.exceptions.MaxRetryError as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % type(e))
        assert etag is not None
        try:
            api_response = self.__api.engine_tasks_id_patch(
                if_match=etag,
                id=job_id,
                body=json.dumps({"engineMachineId": my_id, "isExpired": True}),
            )
            ret = True
        except ApiException as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_patch: %s\n" % e)
        except urllib3.exceptions.MaxRetryError as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_patch: %s\n" % type(e))

        return ret

    def send_job_status(self, job_id: str, percent: float, start_time_stamp: float, end_time_stamp: float) -> bool:
        assert job_id is not None
        assert len(job_id) > 0

        ret = False
        status_id = None
        etag = None

        try:
            api_response = self.__api.engine_task_status_get(
                where=json.dumps({"engineTaskId": job_id}),
                sort=json.dumps([("created", -1)]),
                max_results=json.dumps(1),
            )
            # assert api_response.id == job_id
            # etag = api_response.etag
            if len(api_response.items) > 0:
                etag = api_response.items[0].etag
                status_id = api_response.items[0].id
        except ApiException as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % e)
        except urllib3.exceptions.MaxRetryError as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % type(e))
        progress = EngineTaskStatusProgress(
            percentage=percent,
            start_time_stamp=start_time_stamp,
            end_time_stamp=end_time_stamp,
        )
        # failure = EngineTaskStatusFailure()
        failure = None
        body = EngineTaskStatus(engine_task_id=job_id, progress=progress, failure=failure)
        try:
            if status_id is None or etag is None:
                api_response = self.__api.engine_task_status_post(body=body)
            else:
                api_response = self.__api.engine_task_status_id_patch(if_match=etag, id=status_id, body=body)
        except ApiException as e:
            logging.error(
                "Exception when calling EnginesApi->engine_task_status_post or engine_task_status_id_patch: %s\n" % e
            )
        except urllib3.exceptions.MaxRetryError as e:
            logging.error(
                "Exception when calling EnginesApi->engine_task_status_post or engine_task_status_id_patch: %s\n"
                % type(e)
            )

        # assert etag is not None
        return ret

    def upload_image(self, jpeg_image_bytes: bytes, image_name: str) -> str:
        content_type = "image/jpeg"
        bucket_name = "deeperlook3"
        key_name = "dd-aa"
        api_url = f"{self.vs3_host}/api/vs3/test/{image_name}"
        ret = None
        try:
            files = {"file": (image_name, jpeg_image_bytes, content_type)}
            payload = {"Bucket": bucket_name, "Key": key_name, "ContentType": content_type}
            r = requests.request(method="POST", url=api_url, data=payload, files=files)
            logging.info(f"upload_image, status: {r.status_code}, text: {r.text}")

            if r.status_code == 201 or r.status_code == 200:
                json_response = r.json()
                ret = json_response["items"][0]["Location"]
        except requests.exceptions.ConnectionError:
            logging.error("upload_image connection error")
        return ret

    def send_event(self, job_id, start_time_stamp,  end_time_stamp, jpeg_image_bytes: bytes, event_data) -> bool:
        capbilities_type = 201
        assert jpeg_image_bytes is not None
        image_name = "dog.jpg"
        snap_url = self.upload_image(jpeg_image_bytes, image_name)
        ret = False
        api_response = None
        if snap_url is None:
            logging.error("Snap url is None")
            return False

        try:
            api_response = self.__api.event_snaps_post(body=Snap(snap=snap_url, snap_id=image_name))
        except ApiException as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % e)
        except urllib3.exceptions.MaxRetryError as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % type(e))
        if api_response is None:
            logging.error("event_snaps_post returned None")
            return False

        try:
            api_response = self.__api.va_events_post(body=VaEvent(meta_va_event=MetaVaEvent(count=1), capbilities_type=capbilities_type, event_details=EventDetails(
                engine_task_id=job_id, start_time_stamp=start_time_stamp, end_time_stamp=end_time_stamp),
                event_snaps=[api_response.id], event_clips=[]))
            ret = True
        except ApiException as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % e)
        except urllib3.exceptions.MaxRetryError as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % type(e))
        if api_response is None:
            logging.error("va_events_post returned None")
            return False

        return ret


class DeeperLookTaskSubmitterApi:
    def __init__(self) -> None:
        host_name = "http://10.0.0.103"
        api_host = f"{host_name}:5000"
        config = Configuration()
        config.host = api_host
        self.vs3_host = f"{host_name}:9983"
        self.__api = EnginesApi(api_client=ApiClient(config))

    def upload_image(self, jpeg_image_bytes: bytes, image_name: str) -> str:
        content_type = "image/jpeg"
        bucket_name = "deeperlook3"
        key_name = "dd-aa"
        api_url = f"{self.vs3_host}/api/vs3/test/{image_name}"
        ret = None
        try:
            files = {"file": (image_name, jpeg_image_bytes, content_type)}
            payload = {"Bucket": bucket_name, "Key": key_name, "ContentType": content_type}
            r = requests.request(method="POST", url=api_url, data=payload, files=files)
            logging.info(f"upload_image, status: {r.status_code}, text: {r.text}")

            if r.status_code == 201 or r.status_code == 200:
                json_response = r.json()
                ret = json_response["items"][0]["Location"]
        except requests.exceptions.ConnectionError:
            logging.error("upload_image connection error")
        return ret

    def upload_video(self, video_file_path: str, video_name: str) -> Tuple[str, str]:
        content_type = "video/mp4"
        bucket_name = "deeperlook3"
        key_name = "dd-aa"
        api_url = f"{self.vs3_host}/api/vs3/test"
        ret = (None, None)
        try:
            files = {"file": (video_name, open(video_file_path, 'rb'), content_type)}
            payload = {"Bucket": bucket_name, "Key": key_name, "ContentType": content_type}
            r = requests.request(method="POST", url=api_url, data=payload, files=files)
            logging.info(f"upload_video, status: {r.status_code}, text: {r.text}")

            if r.status_code == 201 or r.status_code == 200:
                json_response = r.json()
                logging.info(json_response)
                ret1 = json_response["items"][0]["Location"]
                ret = (ret1, f"{self.vs3_host}{ret1}")
        except requests.exceptions.ConnectionError:
            logging.error("upload_video connection error")
        return ret

    def put_jobs(self, capbilities_type: int, video_file: str, start_time_stamp: int, end_time_stamp: int, time_to_live: int):
        video_file.replace("\\", "/")
        video_name = None
        for x in video_file.split("/"):
            video_name = x
        video_url, fully_qualified_url = self.upload_video(video_file, video_name)
        ret = False

        if video_url is None:
            logging.error("Video url is None")
            return False

        api_response = None

        try:
            api_response = self.__api.engine_tasks_post(body=EngineTask(
                capbilities_type=capbilities_type,
                time_to_live=time_to_live,
                source=SourceEndPoint(source_list=[SourceEndPointSourceList(type=SourceType.HTTP, base_url=fully_qualified_url)],
                                      start_time_stamp=start_time_stamp,
                                      end_time_stamp=end_time_stamp)))
            logging.info(api_response)
            ret = True
        except ApiException as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % e)
        except urllib3.exceptions.MaxRetryError as e:
            logging.error("Exception when calling EnginesApi->engine_tasks_id_get: %s\n" % type(e))
        if api_response is None:
            logging.error("event_snaps_post returned None")
            return False
        return ret


def test_upload_image(caplog):
    caplog.set_level(logging.INFO)
    logging.info("Started")
    x = DeeperLookApi()
    with open("1.jpg", "rb") as f:
        x.upload_image(f.read(), "dog.jpg")

    logging.info("End")


def test_upload_video(caplog):
    caplog.set_level(logging.INFO)
    logging.info("Started")
    x = DeeperLookTaskSubmitterApi()
    ret = x.upload_video("1.AVI", "1.AVI")
    assert ret == "/api/vs3/test/1.AVI"


def test_job_executor(caplog):
    caplog.set_level(logging.INFO)
    logging.info("Started")
    my_id = "d6a64827-edab-4714-bcec-36f634106f11"
    x = DeeperLookApi()
    items = x.get_jobs([201, 207], 2, my_id)
    assert items is not None
    assert len(items) > 0
    for item in items:
        x.flag_start_job(item.id, my_id)
        for i in range(10, 101, 10):
            x.send_job_status(item.id, i, time.time(), time.time())
            with open("1.jpg", "rb") as f:
                assert x.send_event(item.id, item.source.start_time_stamp,
                                    item.source.end_time_stamp, f.read(), None) == True
        x.flag_finish_job(item.id, my_id)
    # logging.info(f"{items}")
    logging.info("End")


def test_job_submitter(caplog):
    caplog.set_level(logging.INFO)
    logging.info("Started")
    x = DeeperLookTaskSubmitterApi()
    my_id = "d6a64827-edab-4714-bcec-36f634106f11"
    y = DeeperLookApi()
    start_time_stamp = time.time()*1000
    end_time_stamp = start_time_stamp
    time_to_live = 5*3600*1000
    ret = x.put_jobs(201, "1.AVI", start_time_stamp, end_time_stamp, time_to_live)
    assert ret == True
    #y.get_jobs([201, 207], 2, my_id)

    logging.info("End")
    assert False
