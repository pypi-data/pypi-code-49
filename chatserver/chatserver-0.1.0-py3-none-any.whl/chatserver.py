import asyncio
import time
import ssl
import os
import re

clients = {}
client_colors = {}

ANSI_COLORS = [
    "\u001b[31m",
    "\u001b[32m",
    "\u001b[33m",
    "\u001b[34m",
    "\u001b[35m",
    "\u001b[36m",
]
ANSI_RESET = "\u001b[0m"

def get_color():
    """returns a color that isn't used much"""
    color_counts = {color: 0 for color in ANSI_COLORS}
    for color in client_colors.values():
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
            addr = w.get_extra_info('peername')
            for u in clients:
                if clients[u] == w:
                    username = u
                    break

            del clients[u]
            del client_colors[u]
            forward(w, f"Server: {username} left the chat.")
            forward(w, f"Server: There are currently {len(clients)} client(s) online.")
            await w.drain()
            w.close()
            log(f"{addr} ({username}) has disconnected")

    return func_wrapper

def log(message):
    prefix = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]"
    print(f"{prefix} {message}")

def format_message(message, sender, color=ANSI_RESET):
    for username in clients:  # for mentions
        pattern = rf"\@{username}(?!\w)"
        m = re.search(pattern, message)
        if m:
            start = m.span()[0]
            end = m.span()[1]
            message = message[:start] + ANSI_RESET +  client_colors[username] + m.group(0) + color + message[end:]

    to_send = f"{color}{sender}: {message}{ANSI_RESET}"

    return to_send

def forward(writer, message):
    for w in clients.values():
        if w != writer:
            send_msg(w, message)

def validate_username(username):
    if username == "Server":
        return False
    
    if username in clients:
        return False
    
    if len(username) == 0:
        return False
    
    for c in username.lower():
        if c not in "abcdefghijklmnopqrstuvwxyz1234567890_":
            return False
    
    return True

@handler_decerator
async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    log(f"{addr} has joined the server")
    # writer.write("\n\n\n\n".encode("utf-8"))
    await writer.drain()
    send_msg(writer, "Choose a username: ")
    await writer.drain()

    while validate_username(username := (await reader.read(255)).decode("utf-8").strip()) == False:
        send_msg(writer, "Username in use. Pick another. ")
        await writer.drain()
    
    log(f"{addr} now has username {username}")

    clients[username] = writer
    color = get_color()
    client_colors[username] = color
    send_msg(writer, f"Hello, {username}!")
    send_msg(writer, f"There are currently {len(clients)} client(s) online (including you).")
    forward(writer, f"Server: {username} joined the chat.")
    forward(writer, f"Server: There are currently {len(clients)} client(s) online.")

    await writer.drain()

    while (request := (await reader.read(255)).decode("utf-8").strip()) != "quit":
        if request:
            msg = format_message(request, username, color)
            writer.write(u"\u001b[1A\u001b[2K".encode("utf-8"))  # go back up (to were inpupt is) and the clear line
            writer.write(msg.encode("utf-8"))
            writer.write(u"\u001b[1S\u001b[1G".encode("utf-8"))  # scroll and go to start of line
            await writer.drain()
            forward(writer, msg)
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