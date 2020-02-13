"""
Deserialize kpf to boiler_rest client types
"""
import math
from typing import Dict

import yaml

from boiler.models import Activity, ActivityList, Actor, Box, Detection

GEOM_ID = 'id0'  # detection id
ACTOR_ID = 'id1'  # actor id
CSET3 = 'cset3'
GEOM = 'geom'
TYPES = 'types'
FRAME = 'ts0'  # timestamp in frames
SECONDS = 'ts1'  # timestamp in seconds
BOX = 'g0'  # geometry bounding box: [top, left, bottom, right]
KEYFRAME = 'keyframe'  # boolean is keyframe?
ACTIVITY = 'act'
ACTIVITY_TYPE = 'act2'
ACTIVITY_ID = 'id2'
TIMESPANS = 'timespan'
FRAME_TIMESPAN = 'tsr0'
STATUS = 'src_status'
ACTORS = 'actors'


def load_yaml(file):
    try:
        return yaml.load(file, Loader=yaml.CLoader)
    except AttributeError:
        return yaml.safe_load(file)


# TODO: Fix kpf deserialization and remove type: ignore


def deserialize_types(file, actor_map):
    yml = load_yaml(file)
    for type_packet in yml:
        if TYPES in type_packet:
            kpf_types = type_packet[TYPES]
            id1 = kpf_types[ACTOR_ID]
            cset3 = kpf_types[CSET3]
            cset3keys = list(cset3.keys())
            if len(cset3keys) != 1:
                raise ValueError(f'{CSET3} should only have 1 key, found {cset3keys}')
            name = cset3keys[0]
            if id1 in actor_map:
                actor_map[id1].actor_type = name
            else:
                actor_map[id1] = Actor(actor_type=name)  # type: ignore


def deserialize_geom(file, actor_map):
    """
    python's yaml parsing is painfully slow,
    this func could take on the order of 10 seconds
    """
    yml = load_yaml(file)
    for geom_packet in yml:
        if GEOM in geom_packet:
            geom = geom_packet[GEOM]
            actor_id = geom[ACTOR_ID]
            frame = geom[FRAME]
            box = geom[BOX]
            box = [int(n) for n in box.split(' ')]
            if len(box) != 4:
                raise ValueError('expect bounding box to have 4 values')
            keyframe = False
            if KEYFRAME in geom:
                keyframe = geom[KEYFRAME]
            box = Box(left=box[0], top=box[1], right=box[2], bottom=box[3])
            detection = Detection(frame=frame, box=box, keyframe=keyframe)
            if actor_id in actor_map:
                actor_map[actor_id].detections.append(detection)
            else:
                actor_map[actor_id] = Actor(  # type: ignore
                    clip_id=actor_id, detections=[detection]
                )

    for actor in actor_map.values():
        actor.sort_detections()


def _deserialize_frame_timespan(timespans):
    for timespan in timespans:
        if FRAME_TIMESPAN in timespan:
            return timespan[FRAME_TIMESPAN]
    raise ValueError(f'no timespan in {timespans} with {FRAME_TIMESPAN}')


def _deserialize_actor(actor, actor_map):
    if ACTOR_ID not in actor:
        raise ValueError(f'actor {actor} missing {ACTOR_ID}')
    if TIMESPANS not in actor:
        raise ValueError(f'actor {actor} missing {TIMESPANS}')
    actor_id = actor[ACTOR_ID]
    timespans = actor[TIMESPANS]
    frame_timespan = _deserialize_frame_timespan(timespans)
    if actor_id in actor_map:
        actor_map[actor_id].begin = frame_timespan[0]
        actor_map[actor_id].end = frame_timespan[1]
    else:
        actor_map[actor_id] = Actor(  # type: ignore
            clip_id=actor_id, begin=frame_timespan[0], end=frame_timespan[1]
        )
    return actor_map[actor_id]


def _deserialize_activity(activity_packet, actor_map):
    """
    returns activity instance
    """
    activity = activity_packet[ACTIVITY]
    timespans = activity[TIMESPANS]
    frame_timespan = _deserialize_frame_timespan(timespans)
    actors = activity[ACTORS]
    activity_type_obj = activity[ACTIVITY_TYPE]
    activity_type_keys = list(activity_type_obj.keys())
    if len(activity_type_keys) != 1:
        raise ValueError(f'{activity_type_obj} should only have 1 key')
    activity_type = activity_type_keys[0]
    status = activity.get(STATUS, None)
    return Activity(  # type: ignore
        clip_id=activity[ACTIVITY_ID],
        activity_type=activity_type,
        begin=frame_timespan[0],
        end=frame_timespan[1],
        status=status,
        actors=[_deserialize_actor(a, actor_map) for a in actors],
    )


def deserialize_activities(file, activity_map, actor_map):
    """
    Load activity from file given geometry and types
    returns map from activity ID to activity
    """
    yml = load_yaml(file)
    for activity_packet in yml:
        if ACTIVITY in activity_packet:
            activity = _deserialize_activity(activity_packet, actor_map)
            activity_map[activity.clip_id] = activity


def serialize_types(actor_map: Dict[int, Actor]):
    for actor_id, actor in actor_map.items():
        line = {'types': {ACTOR_ID: actor_id, CSET3: {actor.actor_type: 1.0}}}
        yield '- {}'.format(yaml.dump(line, default_flow_style=True, width=math.inf))


def serialize_geom(actor_map: Dict[int, Actor]):
    geom_id = 1
    for actor_id, a in actor_map.items():
        for d in a.detections:
            if d.keyframe:
                line = {
                    'geom': {
                        ACTOR_ID: actor_id,
                        GEOM_ID: geom_id,
                        FRAME: d.frame,
                        # TODO ts1 requires framerate
                        BOX: f'{d.box.left} {d.box.top} {d.box.right} {d.box.bottom}',
                        KEYFRAME: True,
                    }
                }
                geom_id = geom_id + 1
                yield '- {}'.format(yaml.dump(line, default_flow_style=True, width=math.inf))


def serialize_activities(activity_map: Dict[int, Activity], actor_map: Dict[int, Actor]):
    inverse_actor_map = {actor: actor_id for actor_id, actor in actor_map.items()}

    for activity_id, activity in activity_map.items():
        activity = activity_map[activity_id]

        line = {
            ACTIVITY: {
                ACTIVITY_TYPE: {activity.activity_type: 1.0,},
                ACTIVITY_ID: activity_id,
                TIMESPANS: [{FRAME_TIMESPAN: [activity.begin, activity.end]}],
                ACTORS: [
                    {
                        ACTOR_ID: inverse_actor_map[actor],
                        TIMESPANS: [{FRAME_TIMESPAN: [actor.begin, actor.end]}],
                    }
                    for actor in activity.actors
                ],
            }
        }

        if activity.status:
            line[ACTIVITY][STATUS] = activity.status

        yield '- {}'.format(yaml.dump(line, default_flow_style=True, width=math.inf))


def serialize_to_files(
    output_basename: str, activity_list: ActivityList, keyframes_only=False,
):
    actor_map = activity_list.actor_map
    activity_map = activity_list.activity_map

    with open(output_basename + '.activities.yml', 'w', encoding='utf-8') as yamlfile:
        for line in serialize_activities(activity_map, actor_map):
            yamlfile.write(line)
    with open(output_basename + '.types.yml', 'w', encoding='utf-8') as yamlfile:
        for line in serialize_types(actor_map):
            yamlfile.write(line)
    with open(output_basename + '.geom.yml', 'w', encoding='utf-8') as yamlfile:
        for line in serialize_geom(actor_map):
            yamlfile.write(line)
