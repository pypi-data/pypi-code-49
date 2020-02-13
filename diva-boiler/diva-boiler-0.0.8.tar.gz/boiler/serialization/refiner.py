"""
Refiner answer deserialization into boiler models.
"""
from itertools import groupby
import json
from typing import Any, Dict, List, Union

from intervals import IntInterval  # type: ignore

from boiler import definitions, models


def invert_type_mapping(map: Dict[str, int]) -> Dict[int, str]:
    """Invert a refiner type mapping."""
    # For some reason, refiner answers provide the inverse of what you actually
    # need....
    return {v: k for k, v in map.items()}


def is_keyframe(detection: Dict[str, Any]) -> bool:
    # TODO: do we want to handle other types?
    return detection['src'] in ('ground-truth', 'truth')


def deserialize_detection(detection: Dict[str, Any]) -> models.Detection:
    box = detection['bbox']
    return models.Detection(
        frame=detection['frame'],
        box=models.Box(left=box[0], top=box[1], right=box[2], bottom=box[3],),
        keyframe=is_keyframe(detection),
    )


def deserialize_answer(answer_string: Union[str, Dict[str, Any]]) -> models.Activity:
    if isinstance(answer_string, str):
        answer = json.loads(answer_string)
    else:
        answer = answer_string

    if 'types' not in answer or 'activities' not in answer or 'detections' not in answer:
        raise ValueError('answer did not contain all required keys')

    if len(answer['activities']) != 1:
        raise ValueError('answer should contain exactly 1 activity')

    types = answer['types']
    activity = answer['activities'][0]
    flat_detections = sorted(answer['detections'], key=lambda d: d['id1'])

    actor_type_map: Dict[int, definitions.ActorType] = {}
    for actor_type in types:
        actor_type_string = list(actor_type['cset3'].keys())[0]
        actor_type_map[actor_type['id1']] = definitions.ActorType(actor_type_string)

    actor_map = {actor['id1']: actor for actor in activity.get('actors', [])}
    detection_map = groupby(flat_detections, lambda d: d['id1'])
    actors: List[models.Actor] = []

    for actor_id, detection_iterator in detection_map:
        answer_actor = actor_map[actor_id]
        actor_type = actor_type_map[actor_id]
        time_range = IntInterval(answer_actor['timespan'][0]['tsr0'])
        detections = [deserialize_detection(d) for d in detection_iterator if is_keyframe(d)]

        actor = models.Actor(
            begin=time_range.lower,
            end=time_range.upper,
            actor_type=actor_type.value,
            detections=detections,
        )
        actors.append(actor)

    activity_id = activity['id2']
    activity_type_map = invert_type_mapping(activity['act2'])
    activity_type = definitions.ActivityType(activity_type_map[activity_id])
    frame_range = IntInterval(activity['timespan'][0]['tsr0'])

    return models.Activity(
        activity_type=activity_type, begin=frame_range.lower, end=frame_range.upper, actors=actors,
    )
