import asyncio
import asyncssh
import sys


class MySSHClientSession(asyncssh.SSHClientSession):
    def data_received(self, data, datatype):
        print(data, end='')

    def connection_lost(self, exc):
        if exc:
            print('SSH session error: ' + str(exc), file=sys.stderr)


class MySSHClient(asyncssh.SSHClient):
    def connection_made(self, conn):
        print('Connection made to %s.' % conn.get_extra_info('peername')[0])

    def auth_completed(self):
        print('Authentication successful.')


async def run_client():
    conn, client = await asyncssh.create_connection(MySSHClient, 'localhost')

    async with conn:
        chan, session = await conn.create_session(MySSHClientSession, 'ls abc')
        await chan.wait_closed()

try:
    asyncio.get_event_loop().run_until_complete(run_client())
except (OSError, asyncssh.Error) as exc:
    sys.exit('SSH connection failed: ' + str(exc))
