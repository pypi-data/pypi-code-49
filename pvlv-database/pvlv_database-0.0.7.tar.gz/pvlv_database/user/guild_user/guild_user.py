from pvlv_database.user.modules.commands import CommandData
from pvlv_database.user.modules.messages import MessagesData
from pvlv_database.user.modules.xp import XpData
from pvlv_database.user.modules.bill import BillData


class GuildUser(object):

    def __init__(self):
        # user data logging
        self.guild_id = None
        self.guild_name = ''
        self.permissions = 10

        self.commands = CommandData()
        self.msg = MessagesData()
        self.xp = XpData()
        self.bill = BillData()

    def extract_data(self, raw_data):
        self.guild_id = raw_data.get('guild_id', self.guild_id)
        self.guild_name = raw_data.get('guild_name', self.guild_name)
        self.permissions = raw_data.get('permissions', self.permissions)

        commands = raw_data.get('commands')
        self.commands = CommandData() if not commands else CommandData().extract_data(commands)

        msg = raw_data.get('msg')
        self.msg = MessagesData() if not msg else MessagesData().extract_data(msg)

        xp = raw_data.get('xp')
        self.xp = XpData() if not xp else XpData().extract_data(xp)

        bill = raw_data.get('bill')
        self.bill = BillData() if not bill else BillData().extract_data(bill)

        return self

    def build_data(self):

        data = {
            'guild_id': self.guild_id,
            'guild_name': self.guild_name,
            'permissions': self.permissions,

            'commands': self.commands.build_data(),
            'msg': self.msg.build_data(),
            'xp': self.xp.build_data(),
            'bill': self.bill.build_data(),
        }

        return data
