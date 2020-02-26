"""
Creates sql tables if they don't exist
inserts messages into tables appropriately
"""
import json
import logging
import time
from os import environ

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, DECIMAL, select, MetaData, Table, and_
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.jaeger_config import conversation_tracer

SQL_LOG = logging.getLogger('sql_driver')
SQL_LOG.setLevel("DEBUG")
CHANNELS_TABLE = environ.get('SQL_CHANNEL_TABLE') or "channel"
TRANSCRIPT_TABLE = environ.get('SQL_CONVERSATION_TABLE') or "conversations_test"
MESSAGE_TABLE = environ.get('SQL_MESSAGE_TABLE') or "messages_test"
CONSUMER_OFFSET_TABLE = environ.get('SQL_CONSUMER_OFFSET_TABLE') or 'consumer_offset'
Base = declarative_base()


class Channels(Base):
    """channels table"""
    __tablename__ = CHANNELS_TABLE

    channelId = Column(Integer, primary_key=True)
    channelName = Column(String)

    def __repr__(self):
        return "<Channels(channelId='%s', channelName='%s')>" % (
            self.channelId, self.channelName)


class Transcript(Base):
    """convertions table"""
    __tablename__ = TRANSCRIPT_TABLE

    channelId = Column(Integer)
    conversationId = Column(String(64), primary_key=True)
    channelUserId = Column(String(64))
    guid = Column(String(64))
    startTime = Column(BigInteger)
    endTime = Column(BigInteger)
    errors = Column(Integer)
    outcome = Column(String)
    rating = Column(Integer)
    feedbackText = Column(String(64))
    flagged = Column(Boolean)
    missedIntent = Column(Boolean)

    def __repr__(self):
        return ("<Transcripts(channelId='%s',"
                "conversationId='%s',"
                "channelUserId='%s',"
                "startTime='%s',"
                "endTime='%s',"
                "errors='%s',"
                "outcome='%s',"
                "rating='%s',"
                "feedbackText='%s')>") % (
                   self.channelId,
                   self.conversationId,
                   self.channelUserId,
                   self.startTime,
                   self.endTime,
                   self.errors,
                   self.outcome,
                   self.rating,
                   self.feedbackText)


class Message(Base):
    """Messages table"""
    __tablename__ = MESSAGE_TABLE

    uid = Column(Integer, primary_key=True)
    conversationId = Column(String(64))
    message = Column(String)
    asrConfidence = Column(DECIMAL(5, 4))
    nluConfidence = Column(DECIMAL(5, 4))
    intent = Column(String)
    agent = Column(String)
    error = Column(Boolean)
    timestamp = Column(BigInteger)
    recordingId = Column(String)
    missedIntent = Column(Boolean)

    def __repr__(self):
        return ("<Message(conversationId='%s',"
                "message='%s',"
                "asrConfidence='%s',"
                "nluConfidence='%s',"
                "intent='%s',"
                "agent='%s',"
                "error='%s',"
                "timestamp='%s',"
                "recordingId='%s')>,"
                "missedIntent='%s") % (
                   self.conversationId,
                   self.message,
                   self.asrConfidence,
                   self.nluConfidence,
                   self.intent,
                   self.agent,
                   self.error,
                   self.timestamp,
                   self.recordingId,
                   self.missedIntent)


consumerOffset = Table(
    CONSUMER_OFFSET_TABLE,
    MetaData(),
    Column('id', Integer, primary_key=True),
    Column('partition', Integer),
    Column('offset', Integer),
    Column('groupId', String),
)


class AlcSeq:
    """Handles logic for when to write to the SQL database"""
    __instance = None

    @staticmethod
    def get_instance():
        if AlcSeq.__instance is not None:
            return AlcSeq.__instance

        return AlcSeq()

    def __init__(self):
        """Connect to engine and load channels"""
        if AlcSeq.__instance is not None:
            raise Exception("Instance has been initialized. Please use get_instance() instead.")

        SQL_LOG.info("Initializing sql engine")
        user = environ['SQL_USER']
        password = environ['SQL_PASSWORD']
        hostname = environ['SQL_HOSTNAME']
        self.engine = create_engine('mssql+pymssql://' + user + ':' + password + '@' + hostname + '/VersayDW',
                                    isolation_level='READ_UNCOMMITTED', pool_size=40, max_overflow=100)
        Base.metadata.create_all(self.engine)
        self.channel_id = {}
        self.load_channels()
        AlcSeq.__instance = self
        self.conversations = []
        self.sess = None

    def load_channels(self):
        """Load channels and set id/name mapping"""
        SQL_LOG.debug("Loading channels")
        channels = self.engine.execute(Channels.__table__.select())
        for channel in channels:
            self.channel_id[channel.channelName] = channel.channelId

    def create_channel(self, channel):
        SQL_LOG.info("Adding new channel to sql database")
        self.engine.execute(Channels.__table__.insert().values({"channelName": channel}))

    def get_conversation(self, conversation_id):
        return self.sess.query(Transcript).get(conversation_id)

    def get_or_null(self, exp):
        if exp:
            if isinstance(exp, str):
                return "'{}'".format(exp)
            else:
                return exp
        else:
            return 'NULL'

    def get_update_conversation_stmt(self, conversation_id, values):
        try:
            SQL_LOG.info(f"[{conversation_id}] - Updating conversation with values: {values}")
            stmt = Transcript.__table__.update().where(
                Transcript.__table__.c.conversationId == conversation_id
            ).values(
                values
            )
            return stmt
        except SQLAlchemyError as ex:
            SQL_LOG.error(f"Failed to commit SQL transaction: {ex}")

    def prepare_insert_conversation(self, event):
        SQL_LOG.info(f"[{event.sender_id}] - Prepare for creating a new conversation to the {TRANSCRIPT_TABLE} table")
        dnis = event.dnis

        if dnis and dnis not in self.channel_id:
            SQL_LOG.warning(f"Channel {dnis} is not found!")
            self.create_channel(dnis)
            self.load_channels()

        user_input_json = json.loads(event.text[6:])
        event.guid = user_input_json.get('guid')
        event.channel_user_id = user_input_json.get('channelUserId')
        values = {
            "channelId": self.channel_id.get(dnis),
            "conversationId": event.sender_id,
            "channelUserId": event.channel_user_id,
            "errors": event.errors,
            "outcome": event.outcome,
            "startTime": event.timestamp,
            "guid": event.guid,
            "endTime": None,
            "rating": event.rating,
            "feedbackText": event.feedback
        }

        return values

    def create_message(self, transcript):
        SQL_LOG.info(f"[{transcript.conversation_id}] - Message: {transcript.agent}: {transcript.message}")
        msg = {
            "conversationId": transcript.conversation_id,
            "message": transcript.message,
            "asrConfidence": transcript.asr_confidence,
            "nluConfidence": transcript.nlu_confidence,
            "intent": transcript.intent,
            "agent": transcript.agent,
            "error": transcript.errors,
            "timestamp": transcript.timestamp,
            "recordingId": transcript.recording_id,
            "missedIntent": transcript.missed_intent,
        }
        return msg

    def create_system_evt(self, sid, event):
        SQL_LOG.info(f"[{sid}] - System event: {event.value}")
        return {
            "conversationId": sid,
            "message": f"{event.value.get('name')}: {event.value.get('message')}",
            "asrConfidence": 1,
            "nluConfidence": 1,
            "intent": None,
            "agent": "system",
            "error": 0,
            "timestamp": event.timestamp,
            "recordingId": None,
            "missedIntent": False
        }

    def commit_users_msgs(self, conversations, msgs, stmts):
        with conversation_tracer.start_active_span('commit_users_msgs'):
            try:
                s = time.time()
                with self.engine.begin() as conn:
                    if len(conversations) > 0:
                        with conversation_tracer.start_active_span('create_transcripts'):
                            conn.execute(Transcript.__table__.insert().values(conversations))

                    if len(msgs) > 0:
                        with conversation_tracer.start_active_span('insert_msgs'):
                            conn.execute(Message.__table__.insert().values(msgs))

                    now = time.time()
                    with conversation_tracer.start_active_span('update_stmts'):
                        for stmt in stmts:
                            conn.execute(stmt)

                    d = (time.time() - now) * 1000
                    if len(stmts) > 0:
                        SQL_LOG.info(f"Duration of executing {len(stmts)} update statements: {d}ms")

                duration = (time.time() - s) * 1000
                if duration > 200:
                    SQL_LOG.info(f"Duration of committing all user msgs and {len(stmts)} of update statements are "
                                 f"executed: {duration}ms")

                return True
            except SQLAlchemyError as err:
                SQL_LOG.error(f"Failed to commit SQL transaction: {err}")
                return False

    def execute_stmt(self, stmt):
        with conversation_tracer.start_active_span('execute_stmts'):
            try:
                self.engine.execute(stmt)
            except SQLAlchemyError as ex:
                SQL_LOG.error(f"Failed to commit SQL transaction: {ex}")

    def commit_conversations(self, conversations):
        with conversation_tracer.start_active_span('exec_insert_conversations'):
            if len(conversations) > 0:
                try:
                    self.engine.execute(Transcript.__table__.insert().values(conversations))
                except SQLAlchemyError as ex:
                    SQL_LOG.error(f"Failed to commit SQL transaction: {ex}")

    def commit_msgs(self, messages):
        with conversation_tracer.start_active_span('exec_insert_msgs'):
            if len(messages) > 0:
                try:
                    self.engine.execute(Message.__table__.insert().values(messages))
                except SQLAlchemyError as ex:
                    SQL_LOG.error(f"Failed to commit SQL transaction: {ex}")

    def insert_missing_partitions(self, group_id, partition, offset):
        try:
            res = self.engine.execute(select([consumerOffset.c.offset]).where(
                and_(
                    consumerOffset.c.partition == partition,
                    consumerOffset.c.groupId == group_id
                )
            ))
            if not res.fetchone():
                SQL_LOG.info(f"Creating a new entry for partition {partition}")
                stmt = consumerOffset.insert().values(
                    groupId=group_id,
                    partition=partition,
                    offset=offset
                )
                self.engine.execute(stmt)
        except SQLAlchemyError as err:
            SQL_LOG.error(f"Failed to commit latest offset: {err}")

    def get_save_offset_stmt(self, group_id, partition, offset):
        try:
            SQL_LOG.info(f"Updating offset of the partition: {partition}, group_id: {group_id}, offset: {offset}")
            stmt = consumerOffset.update(
                and_(
                    consumerOffset.c.partition == partition,
                    consumerOffset.c.groupId == group_id
                )
            ).values(offset=offset)
            return stmt
        except SQLAlchemyError as err:
            SQL_LOG.error(f"Failed to commit latest offset: {err}")

    def get_offsets(self, partition_nums, group_id):
        try:
            stmt = select([
                consumerOffset.c.partition,
                consumerOffset.c.offset
            ]).where(
                and_(
                    consumerOffset.c.partition.in_(partition_nums),
                    consumerOffset.c.groupId == group_id,
                )
            )
            return self.engine.execute(stmt)
        except SQLAlchemyError as ex:
            SQL_LOG.error(f"Failed to get last committed offset: {ex}")

    def start_session(self):
        with conversation_tracer.start_active_span('start_session'):
            session = sessionmaker(bind=self.engine)
            self.sess = session()

    def commit_session(self):
        with conversation_tracer.start_active_span('commit_session'):
            try:
                self.sess.commit()
            except SQLAlchemyError as ex:
                SQL_LOG.error(f"Failed to commit SQL transaction: {ex}")
                self.sess.rollback()

    def close_session(self):
        with conversation_tracer.start_active_span('close_session'):
            self.sess.close()
