import logging

import websockets


async def client(uri, token, callback):
    try:
        async with websockets.connect(*uri) if isinstance(uri, tuple) else \
                websockets.unix_connect(uri) as websocket:
            await websocket.send(token)
            logging.info("connected to server")

            async for message in websocket:
                logging.debug(f'new message: {message}')
                await callback(message)

    except websockets.exceptions.ConnectionClosedError:
        logging.error("server stopped")
    except ConnectionRefusedError:
        logging.error("can't connect to server")


def client_loop(uri, token, callback):
    import asyncio
    asyncio.get_event_loop().run_until_complete(
        client(uri, token, callback)
    )
