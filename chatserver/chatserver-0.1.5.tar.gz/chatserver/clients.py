from chatserver.database import find_user, create_user
from chatserver import ansi
import re


class AuthError(Exception):
    pass


class Client:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.user = None
        self.color = None
        self.addr = self.writer.get_extra_info("peername")

    async def send(self, msg):
        self.writer.write(msg.encode("utf-8"))
        await self.writer.drain()

    async def recv(self):
        return (await self.reader.read(250)).decode("utf-8").strip()

    async def input(self):
        return await self.recv()

    async def send_server_message(self, message):
        """Sends an unformatted message"""
        await self.send(message + "\n")

    async def send_message(self, room, message, sender):
        """Formats then sends a message"""
        formatted_msg = self.format_message(room, message, sender)
        await self.send(formatted_msg + "\n")

    @staticmethod
    def format_message(room, message, sender):
        """Formats a given message"""
        return f"{sender.user.username}: {message}"

    async def authenticate(self):
        await self.send("Username: ")
        username = await self.recv()

        if not validate_username(username):
            await self.send("Bad Username.\nYour connection has been terminated.")
            raise AuthError("Bad Username")

        if user := find_user(username).first():
            await self.send("Password: ")
            password = await self.input()
            if user.validate_password(password):
                await self.send("Logged in successfully!\n")
                return user
            else:
                await self.send(
                    "Invalid Password.\nYour connection has been terminated."
                )
                raise AuthError("Invalid Password")
        else:
            await self.send("Username not found. Creating new User.\n")
            await self.send("Password: ")
            password = await self.input()
            if not good_password(password):
                await self.send(
                    "Password is not long enough (min 8 chars).\nYour connection has been terminated."
                )
                raise AuthError("Password not good enough")
            await self.send("Confirm Password: ")
            password2 = await self.input()

            if password != password2:
                await self.send(
                    "Passwords do not match.\nYour connection has been terminated."
                )
                raise AuthError("Passwords do not match")

            create_user(username, password)
            await self.send("User Created.\nPlease Log In.\n")
            return await self.authenticate()


class AnsiClient(Client):
    async def send_server_message(self, message):
        await self.send(
            "\u001b[s\u001b[1G\u001b[2K"
        )  # save position, go to start or 1 row up
        await self.send(message)
        await self.send("\u001b[u\u001b[1S")  # resotre position and scroll

    async def send_message(self, room, message, sender):
        formatted_msg = self.format_message(room, message, sender)
        await self.send(
            "\u001b[s\u001b[1G\u001b[2K"
        )  # save position, go to start or 1 row up
        await self.send(formatted_msg)
        await self.send("\u001b[u\u001b[1S")  # resotre position and scroll

    @staticmethod
    def format_message(room, message, sender):
        for username in room:  # for mentions
            pattern = rf"\@{username}(?!\w)"
            m = re.search(pattern, message)
            if m:
                start = m.span()[0]
                end = m.span()[1]
                message = (
                    message[:start]
                    + ansi.ANSI_RESET
                    + room[username].color
                    + m.group(0)
                    + sender.color
                    + message[end:]
                )

        to_send = f"{sender.color}{sender.user.username}: {message}{ansi.ANSI_RESET}"

        return to_send

    async def input(self):
        data = await self.recv()
        await self.send(
            "\u001b[1A\u001b[2K"
        )  # go back up (to were inpupt is) and the clear line
        return data


def good_password(password):
    if len(password) >= 8:
        return True

    return False


def validate_username(username):
    if username == "Server":
        return False

    if len(username) == 0:
        return False

    for c in username.lower():
        if c not in "abcdefghijklmnopqrstuvwxyz1234567890_":
            return False

    return True
