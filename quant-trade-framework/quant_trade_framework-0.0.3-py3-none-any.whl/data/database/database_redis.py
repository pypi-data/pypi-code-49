import redis


class redisTools:
    def __init__(self,host ='182.151.7.177', port = 6379,passwd = 'qyG0usOb'):
        if passwd == '':
            self.pool = redis.ConnectionPool(host, port)
        else:
            self.pool = redis.ConnectionPool(host = host, port = port, password = passwd)

    def getRedisInstance(self):
        return redis.Redis(connection_pool=self.pool)


if __name__ == "__main__":
    temp = redisTools('182.151.7.177',passwd='qyG0usOb')
    client = temp.getRedisInstance()
    while True:
        print(client.ping())