import asyncio
import time
import ssl
import os

from chatserver import clients
from chatserver import ansi

rooms = {
    "main": {},
    "random": {},
}

def get_color(room):
    """returns a color that isn't used much"""
    color_counts = {color: 0 for color in ansi.ANSI_COLORS}
    for color in map(lambda c: c.color, room.values()):
        color_counts[color] += 1

    least_used = ansi.ANSI_COLORS[0]
    occurances = color_counts[least_used]

    for color in color_counts:
        if color_counts[color] < occurances:
            occurances = color_counts[color]
            least_used = color
    
    return least_used


def handler_decerator(func):
    async def func_wrapper(r, w):
        try:
            await func(r, w)
        except (clients.AuthError, ConnectionResetError) as e:
            print(f"Connection terminated: {e}")
        finally:
            username = None
            room = None
            addr = w.get_extra_info('peername')
            for r in rooms:
                for c in rooms[r]:
                    if rooms[r][c].writer == w:
                        username = c
                        room = r
                        break
            
            if username and room:
                del rooms[room][username]
                await forward_server_message(rooms[room], f"Server: {username} left room #{room}.")
                await forward_server_message(rooms[room], f"Serer: There are currently {len(rooms[room])} in room #{room}.")
                log(f"{addr} ({username}) has disconnected")
            await w.drain()
            w.close()
    return func_wrapper

def log(message):
    prefix = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]"
    print(f"{prefix} {message}")


async def forward_message(room, sender, message):
    for client in room.values():
        await client.send_message(room, message, sender)

async def forward_server_message(room, message):
    for client in room.values():
        await client.send_server_message(message)


async def menu(client):
    await client.send("Please choose a room to enter")
    for r in rooms.keys():
        await client.send(f"\n* {r}")
    await client.send("\n>")
    while (room := (await client.recv())) not in rooms.keys():
        await client.send("Invalid rooms name\n>")
    return room

@handler_decerator
async def handle_client(reader, writer):
    client = clients.AnsiClient(reader, writer)
    log(f"{client.addr} has joined the server")
    user = await client.authenticate()
    client.user = user

    await client.send_server_message("Welcome!\nWhen in a chat room you can type `/menu` to leave the room and go back tot the menu.\nYou can mention users by typing @username i.e. if their username is example you can mention them by typing 'Hello @exmaple! How are you doing?'")

    room = await menu(client)
    color = get_color(rooms[room])
    client.color = color
    rooms[room][client.user.username] = client

    await forward_server_message(rooms[room], f"Server: {client.user.username} joined room #{room}.")
    await forward_server_message(rooms[room], f"Server: There are currently {len(rooms[room])} client(s) online.")

    while msg := (await client.input()):
        if msg[0] == "/":
            if msg[1:] == "menu":
                del rooms[room][client.user.username]
                await forward_server_message(rooms[room], f"Server: {client.user.username} left room #{room}.")
                await forward_server_message(rooms[room], f"Serer: There are currently {len(rooms[room])} in room #{room}.")
                room = await menu(client)
                color = get_color(rooms[room])
                client.color = color
                rooms[room][client.user.username] = client
                await forward_server_message(rooms[room], f"Server: {client.user.username} joined room #{room}.")
                await forward_server_message(rooms[room], f"Server: There are currently {len(rooms[room])} client(s) online.")

        else:
            await forward_message(rooms[room], client, msg)

    # client has disconnected


def main():
    cert_file = os.environ.get("CERT_FILE")
    key_file = os.environ.get("KEY_FILE")

    if cert_file != None and key_file != None and os.path.isfile(cert_file) and os.path.isfile(key_file):
        ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_context.check_hostname = False
        ssl_context.load_cert_chain(cert_file, key_file)
        log("Starting server with TLS")
    else:
        log("Starting server with without TLS")
        ssl_context = None
    

    loop = asyncio.get_event_loop()
    loop.create_task(asyncio.start_server(handle_client, "0.0.0.0", 7878, ssl=ssl_context))
    loop.run_forever()


if __name__ == "__main__":
    main()