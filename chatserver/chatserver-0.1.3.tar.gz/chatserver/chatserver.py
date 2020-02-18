import asyncio
import time
import ssl
import os
import re

import auth

rooms = {
    "main": {},
    "random": {},
}


ANSI_COLORS = [
    "\u001b[31m",
    "\u001b[32m",
    "\u001b[33m",
    "\u001b[34m",
    "\u001b[35m",
    "\u001b[36m",
]

ANSI_RESET = "\u001b[0m"


def get_color(room):
    """returns a color that isn't used much"""
    color_counts = {color: 0 for color in ANSI_COLORS}
    for color in map(lambda x: x["color"], rooms[room].values()):
        color_counts[color] += 1

    least_used = ANSI_COLORS[0]
    occurances = color_counts[least_used]

    for color in color_counts:
        if color_counts[color] < occurances:
            occurances = color_counts[color]
            least_used = color
    
    return least_used


def send_msg(w, msg):
    w.write(u"\u001b[s\u001b[1G\u001b[2K".encode("utf-8"))  # save position, go to start or 1 row up
    w.write(f"{msg}".encode("utf-8"))
    w.write(u"\u001b[u\u001b[1S".encode("utf-8"))  # resotre position and scroll


def handler_decerator(func):
    async def func_wrapper(r, w):
        try:
            await func(r, w)
        finally:
            username = None
            room = None
            addr = w.get_extra_info('peername')
            for r in rooms:
                for c in rooms[r]:
                    if rooms[r][c]["writer"] == w:
                        username = c
                        room = r
                        break
            
            if username and room:
                del rooms[room][username]
                forward(room, w, f"Server: {username} left room #{room}.")
                forward(room, w, f"Serer: There are currently {len(rooms[room])} in room #{room}.")
                log(f"{addr} ({username}) has disconnected")
            await w.drain()
            w.close()
    return func_wrapper

def log(message):
    prefix = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]"
    print(f"{prefix} {message}")

def format_message(room, message, sender, color=ANSI_RESET):
    for username in rooms[room]:  # for mentions
        pattern = rf"\@{username}(?!\w)"
        m = re.search(pattern, message)
        if m:
            start = m.span()[0]
            end = m.span()[1]
            message = message[:start] + ANSI_RESET +  rooms[room][username]["color"] + m.group(0) + color + message[end:]

    to_send = f"{color}{sender}: {message}{ANSI_RESET}"

    return to_send

def forward(room, writer, message):
    for w in map(lambda x: x["writer"], rooms[room].values()):
        if w != writer:
            send_msg(w, message)

async def menu(user, reader, writer):
    writer.write("Please choose a room to enter".encode("utf-8"))
    for r in rooms.keys():
        writer.write(f"\n* {r}".encode("utf-8"))
    writer.write("\n>".encode("utf-8"))
    await writer.drain()
    while (room := (await reader.read(255)).decode("utf-8").strip()) not in rooms.keys():
        writer.write("Invalid rooms name\n>".encode("utf-8"))
        await writer.drain()
    return room

@handler_decerator
async def handle_client(reader, writer):
    user = await auth.authenticate_client(reader, writer)
    addr = writer.get_extra_info('peername')
    log(f"{addr} has joined the server")
    # writer.write("\n\n\n\n".encode("utf-8"))
    username = user.username
    
    room = await menu(username, reader, writer)
    color = get_color(room)
    rooms[room][username] = {"color": color, "writer": writer}

    send_msg(writer, f"Hello, {username}! Welcome to room #{room}.")
    send_msg(writer, f"There are currently {len(rooms[room])} client(s) in room #{room} (including you).")
    forward(room, writer, f"Server: {username} joined room #{room}.")
    forward(room, writer, f"Server: There are currently {len(rooms[room])} client(s) online.")

    await writer.drain()

    while (request := (await reader.read(255)).decode("utf-8").strip()) != "quit":
        if request:
            msg = format_message(room, request, username, color)
            writer.write(u"\u001b[1A\u001b[2K".encode("utf-8"))  # go back up (to were inpupt is) and the clear line
            writer.write(msg.encode("utf-8"))
            writer.write(u"\u001b[1S\u001b[1G".encode("utf-8"))  # scroll and go to start of line
            await writer.drain()
            forward(room, writer, msg)
            await writer.drain()
        else:  # client has disconnected
            break


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