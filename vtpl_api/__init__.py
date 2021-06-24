# coding: utf-8

# flake8: noqa

"""
    Engine api

    Engine APIs  # noqa: E501

    OpenAPI spec version: 1.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from vtpl_api.api.engines_api import EnginesApi
# import ApiClient
from vtpl_api.api_client import ApiClient
from vtpl_api.configuration import Configuration
# import models into sdk package
from vtpl_api.models.animal_properties import AnimalProperties
from vtpl_api.models.anpr_event import AnprEvent
from vtpl_api.models.anpr_events_response import AnprEventsResponse
from vtpl_api.models.attribute_event import AttributeEvent
from vtpl_api.models.attribute_events_response import AttributeEventsResponse
from vtpl_api.models.capability import Capability
from vtpl_api.models.clip import Clip
from vtpl_api.models.clips_response import ClipsResponse
from vtpl_api.models.color import Color
from vtpl_api.models.config import Config
from vtpl_api.models.default_response import DefaultResponse
from vtpl_api.models.destination_end_point import DestinationEndPoint
from vtpl_api.models.destination_end_point_destination_list import DestinationEndPointDestinationList
from vtpl_api.models.destination_type import DestinationType
from vtpl_api.models.engine import Engine
from vtpl_api.models.engine_task import EngineTask
from vtpl_api.models.engine_task_line_setting import EngineTaskLineSetting
from vtpl_api.models.engine_task_status import EngineTaskStatus
from vtpl_api.models.engine_task_status_failure import EngineTaskStatusFailure
from vtpl_api.models.engine_task_status_progress import EngineTaskStatusProgress
from vtpl_api.models.engine_task_status_response import EngineTaskStatusResponse
from vtpl_api.models.engine_task_zone_setting import EngineTaskZoneSetting
from vtpl_api.models.engine_tasks_response import EngineTasksResponse
from vtpl_api.models.engines_response import EnginesResponse
from vtpl_api.models.event import Event
from vtpl_api.models.event_details import EventDetails
from vtpl_api.models.event_snaps_response import EventSnapsResponse
from vtpl_api.models.event_type import EventType
from vtpl_api.models.evidence_config import EvidenceConfig
from vtpl_api.models.extra import Extra
from vtpl_api.models.href import Href
from vtpl_api.models.human_properties import HumanProperties
from vtpl_api.models.inferencer import Inferencer
from vtpl_api.models.inferencers_response import InferencersResponse
from vtpl_api.models.line import Line
from vtpl_api.models.line_type import LineType
from vtpl_api.models.links import Links
from vtpl_api.models.links_self import LinksSelf
from vtpl_api.models.links_self_self import LinksSelfSelf
from vtpl_api.models.media_source_response import MediaSourceResponse
from vtpl_api.models.meta import Meta
from vtpl_api.models.meta_anpr_event import MetaAnprEvent
from vtpl_api.models.meta_attribute_event import MetaAttributeEvent
from vtpl_api.models.meta_va_event import MetaVaEvent
from vtpl_api.models.motion_detector import MotionDetector
from vtpl_api.models.motion_detectors_response import MotionDetectorsResponse
from vtpl_api.models.object_dimension import ObjectDimension
from vtpl_api.models.object_direct_properties import ObjectDirectProperties
from vtpl_api.models.object_indirect_properties import ObjectIndirectProperties
from vtpl_api.models.object_info import ObjectInfo
from vtpl_api.models.object_rect import ObjectRect
from vtpl_api.models.pipeline import Pipeline
from vtpl_api.models.pipelines_response import PipelinesResponse
from vtpl_api.models.pre_process import PreProcess
from vtpl_api.models.pre_processes_response import PreProcessesResponse
from vtpl_api.models.schedule_source import ScheduleSource
from vtpl_api.models.snap import Snap
from vtpl_api.models.snaps_response import SnapsResponse
from vtpl_api.models.source_end_point import SourceEndPoint
from vtpl_api.models.source_end_point_source_list import SourceEndPointSourceList
from vtpl_api.models.source_type import SourceType
from vtpl_api.models.title import Title
from vtpl_api.models.track_properties import TrackProperties
from vtpl_api.models.va_event import VaEvent
from vtpl_api.models.va_events_response import VaEventsResponse
from vtpl_api.models.vehicle_properties import VehicleProperties
from vtpl_api.models.vehicle_type import VehicleType
from vtpl_api.models.vertex import Vertex
from vtpl_api.models.vtpl_video_frame import VtplVideoFrame
from vtpl_api.models.zone import Zone
from vtpl_api.models.zone_type import ZoneType
