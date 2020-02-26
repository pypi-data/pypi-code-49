import logging
from os import environ

import redis
from rediscluster.exceptions import RedisClusterException
from rediscluster import RedisCluster

REDIS_URL = environ.get('REDIS_URL') or 'localhost'
REDIS_PORT = environ.get("REDIS_PORT") or "6379"
REDIS_PORT = REDIS_PORT.split(",")
logger = logging.getLogger("RedisRespository")  # get the root logger


class RedisRepository:
    __instance = None

    @staticmethod
    def get_instance(tracer):
        if RedisRepository.__instance is None:
            RedisRepository(tracer)

        return RedisRepository.__instance

    def __init__(self, tracer):
        if RedisRepository.__instance is not None:
            raise Exception("RedisRepository should be a singleton")
        else:
            self.tracer = tracer
            try:
                startup_nodes = [{"host": REDIS_URL, "port": int(p)} for p in REDIS_PORT]
                self.red = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
            except RedisClusterException as exp:
                logger.error(f"Unable to connect to Redis cluster, falling back to Redis standalone connection: {exp}")
                self.red = redis.StrictRedis(REDIS_URL, REDIS_PORT, decode_responses=True)

            RedisRepository.__instance = self

    async def save_state(self, key, state,  timeout=3600):
        with self.tracer.start_active_span("redis_repo_save_state"):
            cue_state = state.__dict__
            del cue_state['events']
            cue_state = {k: v for k, v in cue_state.items() if v is not None}

            # logger.info(f"Saving cue state: {cue_state}")
            with self.red.pipeline() as pipe:
                pipe.hmset(key, cue_state)
                pipe.expire(key, timeout)
                pipe.execute()

    async def get_cue_state(self, state_key):
        with self.tracer.start_active_span("redis_repo_get_state"):
            res = self.red.hgetall(state_key)
            # logger.warning(f"Loading cue state: {res}")
            return res

    async def get_cue_id(self, state_key):
        with self.tracer.start_active_span("redis_repo_get_cue_id"):
            return self.red.hget(state_key, 'cueId')

    async def set_key_val(self, state_key, key, val):
        with self.tracer.start_active_span("redis_repo_set_key_val"):
            self.red.hset(state_key, key, val)

    async def test_conn(self):
        return self.red.setex("ping", 5, "")
