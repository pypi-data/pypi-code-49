import math
from datetime import datetime

from pvlv_database.pvlv_database import Database
from pvlv_database.configurations.configuration import *


class BaseStatsUpdater(object):
    def __init__(self, db: Database):

        self.__db = db
        self.__timestamp = datetime.utcnow()

    def username(self, username: str):
        if username:
            self.__db.user.username = username

    def timestamp(self, timestamp: datetime):
        if timestamp:
            self.__timestamp = timestamp

    def guild_name(self, guild_name: str):
        if guild_name:
            self.__db.user.guild.guild_name = guild_name
            self.__db.guild.guild_name = guild_name

    def update_text(self, text):
        """
        Update the values based on the data given
        - time spent for messages
        - XP
        - Bill

        Then call the callback functions to check if there are actions to do like
        Send a message for:
        - the level_up
        - the bill status.
        """

        text_len = len(text)
        time_spent = math.ceil(text_len * TIME_SAMPLE_VALUE / SAMPLE_STRING_LEN)

        if text:
            """
            If is text update calculating the values based on the text sent
            """
            self.__db.user.guild.msg.update_msg_log((self.__timestamp, 1, time_spent))

            xp_uncut = int(math.ceil(text_len * XP_SAMPLE_VALUE / SAMPLE_STRING_LEN))
            xp = xp_uncut if xp_uncut <= XP_MAX_VALUE else XP_MAX_VALUE
            self.__db.user.guild.xp.xp_value += xp

            bits_uncut = int(math.ceil(text_len * BITS_SAMPLE_VALUE / SAMPLE_STRING_LEN))
            bits = bits_uncut if bits_uncut <= BITS_MAX_VALUE else BITS_MAX_VALUE
            self.__db.user.guild.bill.bits += bits

    def update_image(self):
        """
        Update Parameters Based on a default time to send a picture.
        """
        self.__db.user.guild.msg.update_img_log((self.__timestamp, 1, 6))
        self.__db.user.guild.xp.xp_value += 5
        self.__db.user.guild.bill.bits += 1

    def update_vocal(self, time: int):
        """
        Update Parameters Based on a default time to record an audio
        Counting the re-listening too, as most people do.
        """
        self.__db.user.guild.msg.update_msg_log((self.__timestamp, 1, time))
        self.__db.user.guild.xp.xp_value += 5
        self.__db.user.guild.bill.bits += 1

    @property
    def is_level_up(self):
        """
        Call back function to check if there is the need to send a message for level up.
        :return: True or False
        """
        return self.__db.user.guild.xp.is_level_up
