# Copyright Netflix, 2019
from enum import Enum
from typing import Optional
from typing import Text


class DestinationType(Enum):
    """
    Which destination type/protocol are you using?
    """

    RAE = 1  # switch everything to this
    CLOUD = 2  # switch everything to this


class TopicType(Enum):
    # step 1: handler registers to listen on this
    HANDLER_LISTENING_TOPIC = 1
    # step 2: requester listens here for a response
    REQUESTERS_RESPONSE_TOPIC = 2
    # step 3: requester posts a request to this topic
    REQUESTERS_REQUEST_TOPIC = 3
    # step 4: handler hears it on topic pattern from step 1
    # step 5: handler posts it back to this topic
    HANDLERS_RESPONSE_TOPIC = 4
    # step 6: requester hears it on topic from step 2

    # anything else goes here
    PUBSUB = 5


def topicmaker(
    myrole: DestinationType, remoterole: DestinationType, topictype: TopicType, userdata: Text, raeid: Optional[Text] = None,
) -> Text:
    """
    Make a topic based on the Netflix MQTT topic protocol.

    This is an OPTIONAL call that can help you form the proper request for most conditions where you
    are interacting with the Netflix request/response protocol. If you want to hard-code your topic forming,
    you are free to, but you're getting the phone call when it goes wrong.

    The topic structure is influenced by:
    whether the client is attached to a cloud or local broker
    whether the destination is one of a few defined types
    whether the destination topic is for a response, request, handler, or just general pubsub
    which direction a request is flowing (captured in destination types)

    # exisitng, comments and spacing for clarity

# RAE => Cloud: requests from RAE to cloud
topic # out 1           cloud/           external/client/{{ grains['id'] }}/
topic # in  1 _response/cloud/ _response/external/rae   /{{ grains['id'] }}/
# RAE <= Cloud: requests from cloud to RAE
topic # in  1           external/           client/rae/{{ grains['id'] }}/
topic # out 1 _response/external/ _response/client/rae/{{ grains['id'] }}/

# RAE => Cloud: request
topic # out 1           cloud/           external/client/{{ grains['id'] }}/
topic # in  1 _response/cloud/ _response/external/   rae/{{ grains['id'] }}/
# RAE <= Cloud: response
topic # in  1           external/           client/rae/{{ grains['id'] }}/
topic # out 1 _response/external/ _response/client/rae/{{ grains['id'] }}/


    """
    parts = []

    if topictype in [TopicType.REQUESTERS_RESPONSE_TOPIC, TopicType.HANDLERS_RESPONSE_TOPIC]:
        parts.append("_response")

    if myrole == DestinationType.CLOUD and remoterole == DestinationType.RAE:
        if raeid is None:
            raise ValueError("the ID of the RAE cannot be None")
        parts.append("client")
        parts.append("rae")
        parts.append(raeid)
    elif myrole == DestinationType.RAE and remoterole == DestinationType.CLOUD:
        parts.append("external")

    parts.append(userdata)

    if topictype == TopicType.HANDLER_LISTENING_TOPIC:
        parts.append("#")

    return "/".join(parts)
