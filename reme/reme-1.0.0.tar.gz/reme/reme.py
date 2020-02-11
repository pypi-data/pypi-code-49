#!/usr/bin/env python3

"""
reme.py
A Discord bot that reminds you of things.

[Exit Codes]

1 - No token found
2 - Unable to login 
3 - Unable to connect to the database
4 - Unknown error
5 - Discord.Client error
6 - Asyncio exception thrown
"""

import asyncio
from db import DB
import discord
import entry
import logging
import os
import re
from datetime import datetime

class Reme(discord.Client):
    """
    A wrapper class extending discord.client that adds a database connection and stores the bot token
    """
    # The database object created by db.py
    db: DB = None
    # A mutex lock for the db object 
    db_lock: asyncio.Lock = asyncio.Lock()
    # The bot token id needed to authenticate on discord
    token: str = None

    async def bootstrap(self):
        """
        Starts the logic loop for retrieving and sending reminders
        """
        # connect to discord and start the event loops
        try:
            self.set_token()
            self.connect_to_db()

            # Create a task for the discord.Client.run coro
            discord_coro: asyncio.Task = asyncio.create_task(self.start(self.token))
            logging.debug("reme.py:bootstrap - discord.Client.start task has been created")

            # Create a task for the reminder logic loop coro
            reminder_coro: asyncio.Task = asyncio.create_task(self.reminder_loop())
            logging.debug("reme.py:bootstrap - reme.reminder_loop task has been created")

            await asyncio.gather(discord_coro, reminder_coro)

        except discord.errors.LoginFailure as e:
            logging.error("reme:bootstrap - Unable to login to Discord | {e}")
        except discord.errors.ClientException as e:
            logging.error("reme:bootstrap - Unable to login to Discord | {e}")
        except discord.errors.DiscordException as e:
            logging.error("reme:bootstrap - Unable to login to Discord | {e}")
        except KeyboardInterrupt as e:
            logging.debug(f"reme.py:bootstrap - A keyboard interupt has been received | {e}")
        except SystemExit as e:
            logging.debug(f"reme.py:bootstrap - A SystemExit signal has been received | {e}")
        except asyncio.CancelledError as e:
            logging.debug(f"reme.py:bootstrap - An asyncio task was canceled prematurely | {e}")
        except Exception as e:
            logging.error(f"reme.py:bootstrap- An error unknown occurred | {type(e)}: {e}")

        finally:
            reminder_coro.cancel()
            logging.debug("reme.py:bootstrap - The reme.reminder_loop task has been canceled")
            discord_coro.cancel()
            logging.debug("reme.py:bootstrap - The discord.Client.start task has been canceled")
            logging.info("Reme - Prepairing to close reme")
            await self.close_db()
            logging.info("Reme - Connection to the DB has been closed")
            #discord.client._cancel_tasks(self.loop)
            #logging.debug("reme.py:bootstrap - All tasks in the event loop have been canceled")
            #await self.loop.stop()
            #while self.loop.is_running():
                #logging.debug("reme.py:bootstrap - Waiting from event loop to finish")
            #logging.info("reme.py:bootstrap - The event loop has been stopped")
            #await self.close()

    # end bootstrap


    def help(self) -> str:
        """
        Returns the help docstring in discord markdown
        :return str
        """
    
        return """
        **Reme - A Discord bot that will send you reminders**
        **Author**: martinak1
        **Source**: [GitHub](https://github.com/martinak1/reme)
        **License**: [BSD-3-Clause](https://raw.githubusercontent.com/martinak1/reme/master/LICENSE)

        __**NOTE: Reme uses a 24 hour clock in order to simplify datetimes**__

        **Flags**
        ```css
        -d, debug - Reme echos what you send it after converting it to an Entry object
        -h, help  - Prints this usage docstring```

        **Formating**
        ```css
        !reme <Flag> <Message> @ mm/dd/yyyy hh:mm
        !reme <Flag> <Message> @ hh:mm
        !reme <Flag> <Message> +<Delta>[DdHhMm]```

        **Examples**
        ```css
        Print this help docstring
            !reme -h || !reme help

        Send a reminder 30 minutes from now
            !reme Take the pizza out of the oven +30m

        Send a reminder at 5:30 pm
            !reme Go grocery shopping @ 17:30

        Send a reminder on October 30th at 4:30 pm
            !reme DND Session @ 10/30 16:30```
       """

    # end help


    async def get_entries(self, time: datetime) -> list:
        """
        A coroutine that checks the DB for upcoming execution times and returns a list of entries that need to be sent
        :return list
        """
        entries: list = ()
        logging.debug("reme:get_entries - Collecting entries to be executed at {}".format(time))

        # get access to the db and collect the entries to be executed at the current datetime
        async with self.db_lock:
            logging.debug("reme.py:get_entries - Database lock has been aquired")
            entries = self.db.collect(time)

        logging.debug("reme.py:get_entries - Database lock has been released")
        return entries

    # end check_entries


    # TODO document
    # TODO add error handeling
    async def reminder_loop(self):
        """
        
        """
        # wait for connection to discord to be established
        await self.wait_until_ready()

        while True:
            logging.debug("reme.py:reminder_loop - Starting reminder loop")
            entries: list = await self.get_entries(
                datetime.now().replace(second=0, microsecond=0)
            )
            logging.debug(f"reme.py:reminder_loop - Collected {len(entries)} entries")
            to_delete: list = []
            tasks: list = []

            if entries:
                for e in entries:
                    logging.debug(
                        f"reme:reminder_loop - Creating a task for entry with UID: {e.uid} then pending it for deletion"
                    )
                    tasks.append(asyncio.create_task(self.send_reminders(e)))
                    to_delete.append(e.uid)

                logging.debug(
                    "reme:reminder_loop - {} tasks created and {} entries pending deletion".format(
                        len(tasks), len(to_delete)
                    )
                )

                # wait for all of the reminders to be sent
                asyncio.gather(*tasks)
                
                # remove entries that have already been executed
                if len(to_delete):
                    await self.remove_entries(to_delete)
                    logging.debug(f"reme.py:reminder_loop - {len(to_delete)} entries have been removed")
                    logging.debug("reme.py:reminder_loop - All reminders have been sent")

            logging.debug("reme.py:reminder_loop - Sleeping for 60 seconds")
            await asyncio.sleep(60)
        
    # end reminder_loop


    async def remove_entries(self, entries: list):
        """
        Removes entries from the database that have already been executed
        :param list[Entry]
        """
        async with self.db_lock:
            logging.debug("reme.py:remove_entries - Aquired database lock")

            for e in entries:
                self.db.remove(e)

            self.db.commit()

        logging.debug("reme.py:remove_entries - Released the database lock")

    # end remove_entries


    async def send_reminders(self, ent: entry.Entry):
        # TODO make this asyncronus; no need to wait for one message to be sent to send the rest
        """
        Sends a reminder to the specified users
        :param entry.Entry
        """
        ids: list = entry.users_from_string(ent.users) 
        template: str = f"""
        This is an automated reminder :kissing_heart:

        **Message:** {ent.msg}

        **From:** {self.get_user(ids[0]).name}
        """

        if ent.everyone:
            await self.get_channel(ent.channel).send(template)
            logging.debug(
                f"reme.py:send_reminders - A reminder for entry: {ent.uid} has been sent to the channel: {ent.channel}"
            )

        else:
            for id in ids:
                user: discord.User = self.get_user(id)
                await user.send(template)
                logging.debug(f"reme.py:send_reminders - A reminder for entry: {ent.uid} has been sent to {id}")

    # end send_message

    async def close_db(self):
        """
        Close the connection to the database
        """
        async with self.db_lock:
            logging.debug("reme.py:close_db - Acquired the DB lock")
            self.db.close()

        logging.debug("reme.py:close_db - Released the DB lock")
        logging.debug("reme.py:close_db - The connection to the DB has been closed")

    # end close_db


    def connect_to_db(self):
        """
        Initialize a connection to the database and initialize a mutex lock
        """
        # Don't know if I could just make this one line. I think if I did it 
        # like self.db = asyncio.Lock(*DB()), the DB object would fall out of scope
        # and the pointer would be pointing to garbage data
        self.db = DB()
        logging.info("reme.py:connect_to_db - Connection to the database has been established")

    # end set_db


    def set_token(self):       
        """
        Looks for a REME_TOKEN environment variable or a file named 'token.id' and stores the string value.
        This token allows the bot to login
        """
        #Token filelocation
        token_file: str = 'token.id'
        token: str = None

        try:
            token = os.environ['REME_TOKEN'] 

        except KeyError:
            logging.warning(
                "reme.py:Reme.set_token - REME_TOKEN environment variable not set"
            )

        # If token environment variable is not set, look for a token file
        if not token:
            try:
                with open(token_file) as tf:
                    token = tf.readline()
                    tf.close()

            except FileNotFoundError:
                logging.error(
                    "reme.py:Reme.set_token - REME_TOKEN variable is not set and the token file can not be found"
                )
                exit(1)

        self.token = token

    # end set_token


    ###########################################################################
    ## Discord.py Events
    ###########################################################################

    # TODO Sleep the reminder_loop task if disconnected from discord

    async def on_ready(self):
        logging.info(f"Reme has logged on to the server as {self.user}")


    async def on_connect(self):
        logging.info('Reme has connected to the server')


    async def on_disconnect(self):
        logging.warning("Reme has disconnected from the server")


    async def on_resume(self):
        logging.info("Reme has resumed it's connection to the server")


    # TODO figure out why it sends duplicate messages
    async def on_message(self, message):
        # ignore messages from reme
        if message.author == self.user:
            return
    
        # Debug message; Converts it to an entry then responds with what it made
        if message.content.startswith('!reme -d') or message.content.startswith('!reme debug'):
            ent = entry.from_msg(message)
            if ent:
                await message.author.send('Reme Debug {}'.format(ent))
            else:
                await message.channel.send(
                    'Message was not in the correct format. This is what you sent me: \n{}'
                    .format(message.content)
                )
        # Print the help docstring
        elif message.content.startswith('!reme -h') or message.content.startswith('!reme help'):
            await message.channel.send("{}".format(self.help()))
    
        # Commit to the DB
        elif message.content.startswith("!reme"):
            ent: entry.Entry = entry.from_msg(message)
            if ent: 
                async with self.db_lock:
                    self.db.add_entry(ent)

                await message.author.send(
                    f"Got your message {message.author.name}. I will send the reminder at {ent.executed}"
                )

# end Reme class