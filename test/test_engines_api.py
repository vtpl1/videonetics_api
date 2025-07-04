# coding: utf-8

"""
    Engine api

    Engine APIs  # noqa: E501

    OpenAPI spec version: 1.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.engines_api import EnginesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEnginesApi(unittest.TestCase):
    """EnginesApi unit test stubs"""

    def setUp(self):
        self.api = EnginesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_anpr_events_get(self):
        """Test case for anpr_events_get

        Get all anprEvents  # noqa: E501
        """
        pass

    def test_anpr_events_id_delete(self):
        """Test case for anpr_events_id_delete

        Delete an event  # noqa: E501
        """
        pass

    def test_anpr_events_id_get(self):
        """Test case for anpr_events_id_get

        Get anprEvent by id  # noqa: E501
        """
        pass

    def test_anpr_events_id_patch(self):
        """Test case for anpr_events_id_patch

        Patch  # noqa: E501
        """
        pass

    def test_anpr_events_post(self):
        """Test case for anpr_events_post

        Create an anprEvent  # noqa: E501
        """
        pass

    def test_attribute_events_get(self):
        """Test case for attribute_events_get

        Get all attributeEvents  # noqa: E501
        """
        pass

    def test_attribute_events_id_delete(self):
        """Test case for attribute_events_id_delete

        Delete an event  # noqa: E501
        """
        pass

    def test_attribute_events_id_get(self):
        """Test case for attribute_events_id_get

        Get attributeEvent by id  # noqa: E501
        """
        pass

    def test_attribute_events_id_patch(self):
        """Test case for attribute_events_id_patch

        Patch  # noqa: E501
        """
        pass

    def test_attribute_events_post(self):
        """Test case for attribute_events_post

        Create an attributeEvent  # noqa: E501
        """
        pass

    def test_clips_get(self):
        """Test case for clips_get

        Get all unprocesed clips  # noqa: E501
        """
        pass

    def test_clips_id_get(self):
        """Test case for clips_id_get

        Get clip by id  # noqa: E501
        """
        pass

    def test_clips_post(self):
        """Test case for clips_post

        Create an unprocesed clip  # noqa: E501
        """
        pass

    def test_engine_task_status_cumulative_get(self):
        """Test case for engine_task_status_cumulative_get

        Get task status response  # noqa: E501
        """
        pass

    def test_engine_task_status_get(self):
        """Test case for engine_task_status_get

        Get all engineTaskStatus  # noqa: E501
        """
        pass

    def test_engine_task_status_id_delete(self):
        """Test case for engine_task_status_id_delete

        Delete an engineTaskStatus  # noqa: E501
        """
        pass

    def test_engine_task_status_id_get(self):
        """Test case for engine_task_status_id_get

        Get engineTaskStatus by id  # noqa: E501
        """
        pass

    def test_engine_task_status_id_patch(self):
        """Test case for engine_task_status_id_patch

        Patch an engineTaskStatus  # noqa: E501
        """
        pass

    def test_engine_task_status_post(self):
        """Test case for engine_task_status_post

        Create an engineTaskStatus  # noqa: E501
        """
        pass

    def test_engine_tasks_get(self):
        """Test case for engine_tasks_get

        Get all engineTasks  # noqa: E501
        """
        pass

    def test_engine_tasks_id_delete(self):
        """Test case for engine_tasks_id_delete

        Delete an engine task  # noqa: E501
        """
        pass

    def test_engine_tasks_id_get(self):
        """Test case for engine_tasks_id_get

        Get engine task by id  # noqa: E501
        """
        pass

    def test_engine_tasks_id_patch(self):
        """Test case for engine_tasks_id_patch

        Patch an engine task  # noqa: E501
        """
        pass

    def test_engine_tasks_post(self):
        """Test case for engine_tasks_post

        Create an engineTask  # noqa: E501
        """
        pass

    def test_engines_get(self):
        """Test case for engines_get

        Get all engine details  # noqa: E501
        """
        pass

    def test_engines_id_delete(self):
        """Test case for engines_id_delete

        Delete an engine  # noqa: E501
        """
        pass

    def test_engines_id_get(self):
        """Test case for engines_id_get

        Get engine by id  # noqa: E501
        """
        pass

    def test_engines_id_patch(self):
        """Test case for engines_id_patch

        Patch  # noqa: E501
        """
        pass

    def test_engines_post(self):
        """Test case for engines_post

        Create an engine  # noqa: E501
        """
        pass

    def test_event_snaps_get(self):
        """Test case for event_snaps_get

        Get all eventSnaps  # noqa: E501
        """
        pass

    def test_event_snaps_id_get(self):
        """Test case for event_snaps_id_get

        Get eventSnap by id  # noqa: E501
        """
        pass

    def test_event_snaps_post(self):
        """Test case for event_snaps_post

        Create an eventSnap  # noqa: E501
        """
        pass

    def test_inferencers_get(self):
        """Test case for inferencers_get

        Get all inferencers details  # noqa: E501
        """
        pass

    def test_inferencers_id_delete(self):
        """Test case for inferencers_id_delete

        Delete an inferencer  # noqa: E501
        """
        pass

    def test_inferencers_id_get(self):
        """Test case for inferencers_id_get

        Get inferencer by id  # noqa: E501
        """
        pass

    def test_inferencers_id_patch(self):
        """Test case for inferencers_id_patch

        Patch  # noqa: E501
        """
        pass

    def test_inferencers_post(self):
        """Test case for inferencers_post

        Create an inferencer  # noqa: E501
        """
        pass

    def test_media_sources_get(self):
        """Test case for media_sources_get

        Get all media sources  # noqa: E501
        """
        pass

    def test_media_sources_id_delete(self):
        """Test case for media_sources_id_delete

        Delete a media source  # noqa: E501
        """
        pass

    def test_media_sources_id_get(self):
        """Test case for media_sources_id_get

        Get media source by id  # noqa: E501
        """
        pass

    def test_media_sources_id_patch(self):
        """Test case for media_sources_id_patch

        Patch  # noqa: E501
        """
        pass

    def test_media_sources_post(self):
        """Test case for media_sources_post

        Create a media source  # noqa: E501
        """
        pass

    def test_motion_detectors_get(self):
        """Test case for motion_detectors_get

        Get all motionDetectors details  # noqa: E501
        """
        pass

    def test_motion_detectors_id_delete(self):
        """Test case for motion_detectors_id_delete

        Delete an motionDetector  # noqa: E501
        """
        pass

    def test_motion_detectors_id_get(self):
        """Test case for motion_detectors_id_get

        Get motionDetector by id  # noqa: E501
        """
        pass

    def test_motion_detectors_id_patch(self):
        """Test case for motion_detectors_id_patch

        Patch  # noqa: E501
        """
        pass

    def test_motion_detectors_post(self):
        """Test case for motion_detectors_post

        Create an motionDetector  # noqa: E501
        """
        pass

    def test_pipelines_get(self):
        """Test case for pipelines_get

        Get all pipelines details  # noqa: E501
        """
        pass

    def test_pipelines_id_delete(self):
        """Test case for pipelines_id_delete

        Delete an pipeline  # noqa: E501
        """
        pass

    def test_pipelines_id_get(self):
        """Test case for pipelines_id_get

        Get pipeline by id  # noqa: E501
        """
        pass

    def test_pipelines_id_patch(self):
        """Test case for pipelines_id_patch

        Patch  # noqa: E501
        """
        pass

    def test_pipelines_post(self):
        """Test case for pipelines_post

        Create an pipeline  # noqa: E501
        """
        pass

    def test_pre_processes_get(self):
        """Test case for pre_processes_get

        Get all preProcesses details  # noqa: E501
        """
        pass

    def test_pre_processes_id_delete(self):
        """Test case for pre_processes_id_delete

        Delete an preProcess  # noqa: E501
        """
        pass

    def test_pre_processes_id_get(self):
        """Test case for pre_processes_id_get

        Get preProcess by id  # noqa: E501
        """
        pass

    def test_pre_processes_id_patch(self):
        """Test case for pre_processes_id_patch

        Patch  # noqa: E501
        """
        pass

    def test_pre_processes_post(self):
        """Test case for pre_processes_post

        Create an preProcess  # noqa: E501
        """
        pass

    def test_precis_engine_task_status_get(self):
        """Test case for precis_engine_task_status_get

        Get all precisEngineTaskStatus  # noqa: E501
        """
        pass

    def test_precis_engine_task_status_id_delete(self):
        """Test case for precis_engine_task_status_id_delete

        Delete an precisEngineTaskStatus  # noqa: E501
        """
        pass

    def test_precis_engine_task_status_id_get(self):
        """Test case for precis_engine_task_status_id_get

        Get precisEngineTaskStatus by id  # noqa: E501
        """
        pass

    def test_precis_engine_task_status_id_patch(self):
        """Test case for precis_engine_task_status_id_patch

        Patch an precisEngineTaskStatus  # noqa: E501
        """
        pass

    def test_precis_engine_task_status_post(self):
        """Test case for precis_engine_task_status_post

        Create an precisEngineTaskStatus  # noqa: E501
        """
        pass

    def test_precis_engine_tasks_get(self):
        """Test case for precis_engine_tasks_get

        Get all precisEngineTasks  # noqa: E501
        """
        pass

    def test_precis_engine_tasks_id_delete(self):
        """Test case for precis_engine_tasks_id_delete

        Delete an precis engine task  # noqa: E501
        """
        pass

    def test_precis_engine_tasks_id_get(self):
        """Test case for precis_engine_tasks_id_get

        Get precis engine task by id  # noqa: E501
        """
        pass

    def test_precis_engine_tasks_id_patch(self):
        """Test case for precis_engine_tasks_id_patch

        Patch an precis engine task  # noqa: E501
        """
        pass

    def test_precis_engine_tasks_post(self):
        """Test case for precis_engine_tasks_post

        Create an precisEngineTasks  # noqa: E501
        """
        pass

    def test_precis_engine_tasks_v2_jobid_post(self):
        """Test case for precis_engine_tasks_v2_jobid_post

        Create an precisEngineTasks  # noqa: E501
        """
        pass

    def test_snaps_get(self):
        """Test case for snaps_get

        Get all unprocesed snaps  # noqa: E501
        """
        pass

    def test_snaps_id_get(self):
        """Test case for snaps_id_get

        Get snap by id  # noqa: E501
        """
        pass

    def test_snaps_post(self):
        """Test case for snaps_post

        Create a unprocesed snap  # noqa: E501
        """
        pass

    def test_va_events_get(self):
        """Test case for va_events_get

        Get all vaEvents  # noqa: E501
        """
        pass

    def test_va_events_id_delete(self):
        """Test case for va_events_id_delete

        Delete an event  # noqa: E501
        """
        pass

    def test_va_events_id_get(self):
        """Test case for va_events_id_get

        Get vaEvent by id  # noqa: E501
        """
        pass

    def test_va_events_id_patch(self):
        """Test case for va_events_id_patch

        Patch  # noqa: E501
        """
        pass

    def test_va_events_post(self):
        """Test case for va_events_post

        Create an vaEvent  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
