"""Module implementing the networked Participant using gRPC."""

from enum import Enum, auto
import threading
import time
from typing import Optional, Tuple

from grpc import Channel, RpcError, StatusCode, insecure_channel
from numpy import ndarray
from xain_proto.fl.coordinator_pb2 import (
    EndTrainingRoundRequest,
    HeartbeatRequest,
    HeartbeatResponse,
    RendezvousReply,
    RendezvousRequest,
    RendezvousResponse,
    StartTrainingRoundRequest,
    StartTrainingRoundResponse,
    State,
)
from xain_proto.fl.coordinator_pb2_grpc import CoordinatorStub

from xain_sdk.config import Config, CoordinatorConfig, LoggingConfig
from xain_sdk.logger import get_logger, set_log_level
from xain_sdk.participant import InternalParticipant, Participant
from xain_sdk.store import (
    AbstractGlobalWeightsReader,
    AbstractLocalWeightsWriter,
    S3GlobalWeightsReader,
    S3LocalWeightsWriter,
)

logger = get_logger(__name__)


# timings in seconds
RETRY_TIMEOUT: int = 5
HEARTBEAT_TIME: int = 10


class ParState(Enum):
    """Enumeration of Participant states."""

    WAITING: auto = auto()
    TRAINING: auto = auto()
    DONE: auto = auto()


def rendezvous(channel: Channel, participant_id: str) -> None:
    """Start a rendezvous exchange with a coordinator.

    Args:
        channel: A gRPC channel to the coordinator.
        participant_id: ID of the participant.
    """

    coordinator: CoordinatorStub = CoordinatorStub(channel=channel)
    response: Optional[RendezvousResponse] = None

    while not response or response.reply == RendezvousReply.LATER:
        logger.debug(
            "Send RendezvousRequest to coordinator",
            participant_id=participant_id,
            coordinator_id=get_grpc_peer_id(channel=channel),
        )
        request: RendezvousRequest = RendezvousRequest()
        try:
            response = coordinator.Rendezvous(request=request)
        except RpcError as exc:
            status_code: StatusCode = exc.code()  # pylint: disable=no-member
            if status_code == StatusCode.UNAVAILABLE:
                logger.warn(
                    "Coordinator unavailable, retrying rendezvous after timeout",
                    participant_id=participant_id,
                    status_name=status_code.name,
                    details=exc.details(),  # pylint: disable=no-member
                )
                time.sleep(RETRY_TIMEOUT)
            else:
                raise
        else:
            logger.debug(
                "Received RendezvousResponse from coordinator",
                participant_id=participant_id,
                coordinator_id=get_grpc_peer_id(channel=channel),
                reply=RendezvousReply.Name(response.reply),
            )
            if response.reply == RendezvousReply.LATER:
                logger.info(
                    "Retrying rendezvous after timeout", retry_timeout=RETRY_TIMEOUT
                )
                time.sleep(RETRY_TIMEOUT)


def start_training_round(channel: Channel, participant_id: str) -> Tuple[int, int]:
    """Start a training round initiation exchange with a coordinator.

    The decoded contents of the response from the coordinator are returned.

    Args:
        channel: A gRPC channel to the coordinator.
        participant_id: ID of the participant.

    Returns:
        A tuple ``(epochs, epoch_base)`` where ``epochs`` is the
        number of epochs to train, and ``epoch_base`` is the epoch base
        of the global model.
    """

    coordinator: CoordinatorStub = CoordinatorStub(channel=channel)

    request: StartTrainingRoundRequest = StartTrainingRoundRequest()
    logger.debug(
        "Send StartTrainingRoundRequest to coordinator",
        participant_id=participant_id,
        coordinator_id=get_grpc_peer_id(channel=channel),
    )

    response: StartTrainingRoundResponse = coordinator.StartTrainingRound(
        request=request
    )
    logger.debug(
        "Received StartTrainingRoundResponse from coordinator",
        participant_id=participant_id,
        coordinator_id=get_grpc_peer_id(channel=channel),
        epoch=response.epochs,
        epoch_base=response.epoch_base,
    )

    return response.epochs, response.epoch_base


def end_training_round(
    channel: Channel, participant_id: str, number_samples: int, metrics: str
) -> None:
    """Start a training round completion exchange with a coordinator.

    The participant ID, the number of samples and the gathered metrics
    are sent.

    Args:
        channel: A gRPC channel to the coordinator.
        participant_id: ID of the participant.
        number_samples: The number of samples in the training dataset.
        metrics: Metrics data.

    """

    coordinator: CoordinatorStub = CoordinatorStub(channel=channel)

    request: EndTrainingRoundRequest = EndTrainingRoundRequest(
        participant_id=participant_id, number_samples=number_samples, metrics=metrics
    )
    logger.debug(
        "Send EndTrainingRoundRequest to coordinator",
        participant_id=participant_id,
        coordinator_id=get_grpc_peer_id(channel=channel),
    )

    coordinator.EndTrainingRound(request=request)
    logger.debug(
        "Received EndTrainingRoundResponse from coordinator",
        participant_id=participant_id,
        coordinator_id=get_grpc_peer_id(channel=channel),
    )


def training_round(
    channel: Channel, participant: InternalParticipant, round: int
) -> None:
    """Initiate a training round exchange with a coordinator.

    Begins with `start_training_round`. Then performs local training computation using
    the `participant`. Finally, completes with `end_training_round`.

    In case of empty weights from the coordinator (i.e. a 0th round for weights
    initialization) the aggregation meta data and metrics from the participant are
    ignored.

    Args:
        channel: A gRPC channel to the coordinator.
        participant: The local participant.
        round: round number.
    """

    # retrieve epochs and epoch base from the coordinator
    epochs: int
    epoch_base: int
    epochs, epoch_base = start_training_round(
        channel=channel, participant_id=participant.id
    )

    # read the global weights
    global_weights = participant.read_weights(round)

    # train a round
    local_weights: ndarray
    number_samples: int
    metrics: str
    local_weights, number_samples, metrics = participant.train_round(
        weights=global_weights, epochs=epochs, epoch_base=epoch_base
    )

    # write the local weights
    participant.write_weights(round, local_weights)
    end_training_round(
        channel=channel,
        participant_id=participant.id,
        number_samples=number_samples,
        metrics=metrics,
    )


class StateRecord:
    """Thread-safe record of a participant's state and round number."""

    def __init__(  # pylint: disable=redefined-builtin
        self, state: ParState = ParState.WAITING, round: int = -1
    ) -> None:
        """Initialize the state record.

        Args:
            state: The initial state. Defaults to WAITING.
            round: The initial training round. Defaults to -1.
        """

        self.cond: threading.Condition = threading.Condition()
        self.round: int = round
        self.state: ParState = state

    def lookup(self) -> Tuple[ParState, int]:
        """Get the state and round number.

        Returns:
            The state and round number.
        """

        with self.cond:
            return self.state, self.round

    def update(self, state: ParState) -> None:
        """Update the state.

        Args:
            state: The state to update to.
        """

        with self.cond:
            self.state = state
            self.cond.notify()

    def wait_until_selected_or_done(self) -> ParState:
        """Wait until the participant was selected for training or is done.

        Returns:
            The new state the participant is in.
        """

        with self.cond:
            self.cond.wait_for(lambda: self.state in {ParState.TRAINING, ParState.DONE})
            return self.state


def transit(state_record: StateRecord, heartbeat_response: HeartbeatResponse) -> None:
    """Participant state transition function on a heartbeat response.

    Updates the state record.

    Args:
        state_record: The updatable state record of the participant.
        heartbeat_response: The heartbeat response from the coordinator.
    """

    msg: State = heartbeat_response.state
    global_round: int = heartbeat_response.round
    with state_record.cond:
        if state_record.state == ParState.WAITING:
            if msg == State.ROUND and global_round > state_record.round:
                state_record.state = ParState.TRAINING
                state_record.round = global_round
                state_record.cond.notify()
                logger.info(
                    "Transition to training state",
                    local_state=state_record.state,
                    local_round=state_record.round,
                )
            elif msg == State.FINISHED:
                state_record.state = ParState.DONE
                state_record.cond.notify()
                logger.info(
                    "Transition to finished state", local_state=state_record.state
                )
            elif (
                msg == State.STANDBY
                or msg == State.ROUND
                and global_round == state_record.round
            ):
                logger.debug(
                    "Continue in waiting state",
                    local_round=state_record.round,
                    heartbeat_message=msg,
                    heartbeat_round=global_round,
                )
            else:
                logger.warn(
                    "Unexpected heartbeat response",
                    local_round=state_record.round,
                    heartbeat_message=msg,
                    heartbeat_round=global_round,
                )


def message_loop(
    channel: Channel,
    participant_id: str,
    state_record: StateRecord,
    terminate: threading.Event,
) -> None:
    """Periodically send (and handle) heartbeat messages in a loop.

    Args:
        channel: A gRPC channel to the coordinator.
        participant_id: ID of the participant.
        state_record: The participant's state record.
        terminate: An event to terminate the message loop.
    """

    coordinator: CoordinatorStub = CoordinatorStub(channel=channel)

    while not terminate.is_set():
        state: ParState
        round: int
        state, round = state_record.lookup()
        request: HeartbeatRequest = HeartbeatRequest(
            state=par_state_to_proto_state(state), round=round
        )
        logger.debug(
            "Send HeartbeatRequest to coordinator",
            participant_id=participant_id,
            coordinator_id=get_grpc_peer_id(channel=channel),
            state=State.Name(par_state_to_proto_state(state)),
            round=round,
        )

        response: HeartbeatResponse = coordinator.Heartbeat(request=request)
        logger.debug(
            "Received HeartbeatResponse from coordinator",
            participant_id=participant_id,
            coordinator_id=get_grpc_peer_id(channel=channel),
            state=State.Name(response.state),
            round=response.round,
        )
        transit(state_record=state_record, heartbeat_response=response)
        terminate.wait(timeout=HEARTBEAT_TIME)


def start_participant(participant: Participant, config: Config) -> None:
    """Top-level function for the participant's state machine.

    After rendezvous and heartbeat initiation, the Participant is WAITING. If
    selected to train for the current round, it moves to TRAINING, otherwise it
    remains in WAITING. After training is complete for the round, it moves back
    to WAITING. When there is no more training to be done, it moves to the
    terminal state DONE.

    Args:
        participant: The participant for local training.
        config: A valid config.
    """

    config_logging: LoggingConfig = config.logging
    set_log_level(config_logging.level.upper())

    local_weights_writer: AbstractLocalWeightsWriter = S3LocalWeightsWriter(
        config.storage
    )
    global_weights_reader: AbstractGlobalWeightsReader = S3GlobalWeightsReader(
        config.storage
    )

    internal_participant: InternalParticipant = InternalParticipant(
        participant, local_weights_writer, global_weights_reader
    )

    coordinator_config: CoordinatorConfig = config.coordinator
    coordinator_url = f"{coordinator_config.host}:{coordinator_config.port}"

    # use insecure channel for now
    with insecure_channel(target=coordinator_url) as channel:  # thread-safe
        rendezvous(channel=channel, participant_id=participant.dummy_id)

        state_record: StateRecord = StateRecord()
        terminate: threading.Event = threading.Event()
        msg_loop = threading.Thread(
            target=message_loop,
            args=(channel, participant.dummy_id, state_record, terminate),
        )
        msg_loop.start()

        # in WAITING state
        logger.info("rendezvous successful, begin WAITING...")
        try:
            begin_waiting(state_record, channel, internal_participant)
        finally:
            # in DONE state
            logger.info("shutting down participant...")
            terminate.set()
            msg_loop.join()


def begin_waiting(
    state_record: StateRecord, channel: Channel, participant: InternalParticipant
) -> None:
    """"Perform actions in the Participant state WAITING.

    Args:
        state_record: The participant's state record.
        channel: A gRPC channel to the coordinator.
        participant: The participant for local training.
    """

    state: ParState = state_record.wait_until_selected_or_done()
    if state == ParState.TRAINING:  # selected
        logger.debug("received TRAINING signal")
        begin_training(state_record, channel, participant)
    elif state == ParState.DONE:
        logger.info("received DONE signal")
    else:
        logger.warn("received unknown signal", state_signal=state)


def begin_training(
    state_record: StateRecord, channel: Channel, participant: InternalParticipant
) -> None:
    """Perform actions in the Participant state TRAINING.

    Args:
        state_record: The participant's state record.
        channel: A gRPC channel to the coordinator.
        participant: The participant for local training.
    """

    _, local_round = state_record.lookup()
    # perform training comms and computation
    training_round(channel, participant, local_round)

    # internal transition back to WAITING
    logger.debug("trained round, going back to WAITING...")
    state_record.update(ParState.WAITING)
    begin_waiting(state_record, channel, participant)


def par_state_to_proto_state(state: ParState) -> State:
    """Convert the given ``ParState`` into the corresponding
    ``xain_proto.fl.coordinator_pb2.State``.

    Args:
        state: The ``ParState``.

    Returns:
        The corresponding ``xain_proto.fl.coordinator_pb2.State``.


    Raises:

        ValueError: If the ``ParState`` cannot be converted into a
            ``xain_proto.fl.coordinator_pb2.State``
    """
    if state == ParState.TRAINING:
        return State.TRAINING

    if state == ParState.WAITING:
        return State.READY

    if state == ParState.DONE:
        return State.FINISHED

    logger.error("Unknown ParState", state=state)
    raise ValueError(f"Unknown ParState {state}")


def get_grpc_peer_id(channel: Channel) -> str:
    """Get the ID of the target of the gRPC channel.

    Args:
        channel: A gRPC channel to the coordinator.

    Returns:
        The ID of the target of the gRPC channel..
    """

    return channel._channel.target().decode()  # pylint: disable=protected-access
