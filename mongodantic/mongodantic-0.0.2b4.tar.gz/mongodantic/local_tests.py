import string
from urllib.parse import quote_plus as quote
from random import randint, choice
from mongodantic import init_db_connection_params


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(choice(letters) for i in range(stringLength))



MONGO_URL = 'mongodb://{user}:{pw}@{hosts}/?replicaSet={rs}&authSource={auth_src}'.format(
    user=quote('test'),
    pw=quote('2310zavbdJ'),
    hosts=','.join([
        'rc1c-xtmirfqttmz6j2fh.mdb.yandexcloud.net:27018'
    ]),
    rs='rs01',
    auth_src='test_db')
MONGO_DATABASE_NAME = 'test_db'
MONGO_SSL = False

init_db_connection_params(
    MONGO_URL,
    MONGO_DATABASE_NAME,
)

from mongodantic.models import MongoModel


class Test(MongoModel):
    name: str
    position: int


Test.find(name__in=['first', 'fifth']).list


def generate_50k():
    return [Test(name=randomString(), position=randint(1, 100000)) for _ in range(1, 50001)]

