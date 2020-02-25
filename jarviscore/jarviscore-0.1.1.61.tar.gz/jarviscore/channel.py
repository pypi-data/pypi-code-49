import sys
from importlib import util
from copy import deepcopy
from os import path, listdir
from threading import Thread
from time import sleep


from .socket import Socket
from .module import Module
from .model import Model
from .settings import Settings
from .message import *
from .errors import ExtensionAlreadyLoaded, ExtensionNotFound, ExtensionFailed, NoEntryPointError, SettingException

from .log import Log


class Channel(Thread):

    name: str
    __modules: dict
    socket: Socket

    def __init__(self, bridge, nick: str, token: str, channel_name: str = "undefined", id=None):
        Thread.__init__(self)
        self.nick = nick
        self.name = f"Thread-Channel: {channel_name}"
        self.channel_name = channel_name.lower()
        self.socket = Socket(self, nick, token)
        self.bridge = bridge
        self.logging = Log(instance=channel_name, client="Twitch Channel")
        self.__id = id
        self.__modules = {}
        self.active = True
        self.__cache_modules()
        pass

    # Public modules for use in the Bridge and in modules

    def getID(self):
        if self.__id is None:
            return 0
        return self.__id

    def send(self, message):
        self.socket.send_message(self.channel_name, message)

    def send_whisper(self, target, message):
        self.socket.send_whisper(target, message)

    def load_module(self, module):
        self.__modules[module.name] = module

    def on_new_connection(self, channel: str):
        # self.logging.debug("`on_new_connection` invoked.")
        for module in self.__get_module_with_handler("on_new_connection"):
            module.on_new_connection(channel)
        
    def run(self):
        try:
            while self.active: 
                self.socket.listenToStream()
                sleep(0.00001)
        except KeyboardInterrupt:
            self.logging.log(f"Closing connection to {self.channel_name}")
            self.socket.close()
            self.active = False

    def close(self):
        self.logging.log(f"Closing connection to {self.channel_name}")
        self.active = False
        self.socket.close()



    # Callbacks used by the bridge for all Messages sent via the inbound socket.

    ### to do: add the rest of the message types in here

    # Base Callback
    def on_raw(self, data: RawMessage):
        try:
            # self.logging.debug("`on_raw` invoked.")
            for module in self.__get_module_with_handler("on_raw"):
                module.on_raw(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    # IRC: Membership Callbacks

    def on_join(self, data: Join):
        try:
            # self.logging.debug("`on_join` invoked.")
            for module in self.__get_module_with_handler("on_join"):
                module.on_join(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_part(self, data: Part):
        try:
            # self.logging.debug("`on_part` invoked.")
            for module in self.__get_module_with_handler("on_part"):
                module.on_part(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_mode(self, data: Mode):
        try:
            # self.logging.debug("`on_mode` invoked.") 
            for module in self.__get_module_with_handler("on_mode"):
                module.on_mode(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_names(self, data: Names):
        try:
            # self.logging.debug("`on_names` invoked.")
            for module in self.__get_module_with_handler("on_names"):
                module.on_names(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    # IRC: module & Tag Callbacks

    def on_clearchat(self, data: ClearChat):
        try:
            # self.logging.debug("`on_clearchat` invoked.")
            for module in self.__get_module_with_handler("on_clearchat"):
                module.on_clearchat(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_clearmessage(self, data: ClearMessage):
        try:
            # self.logging.debug("`on_clearmessage` invoked.")
            for module in self.__get_module_with_handler("on_clearmessage"):
                module.on_clearmessage(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")
    
    def on_hosttarget(self, data: HostTarget):
        try:
            # self.logging.debug("`on_hosttarget` invoked.")
            for module in self.__get_module_with_handler("on_hosttarget"):
                module.on_hosttarget(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_notice(self, data: Notice):
        try:
            # self.logging.debug(f"`on_notice` invoked. (not implemented)")
            for module in self.__get_module_with_handler("on_notice"):
                module.on_notice(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_reconnect(self, data: Reconnect):
        try:
            # self.logging.debug("`on_reconnect` invoked.")
            for module in self.__get_module_with_handler("on_reconnect"):
                module.on_reconnect(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_roomstate(self, data: RoomState):
        try:
            # self.logging.debug("`on_roomstate` invoked.")
            for module in self.__get_module_with_handler("on_roomstate"):
                module.on_roomstate(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_userstate(self, data: UserState):
        try:
            # self.logging.debug("`on_userstate` invoked.")
            for module in self.__get_module_with_handler("on_userstate"):
                module.on_userstate(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_globaluserstate(self, data: GlobalUserState):
        try:
            # self.logging.debug("`on_globaluserstate` invoked.")
            for module in self.__get_module_with_handler("on_globaluserstate"):
                module.on_globaluserstate(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_privmessage(self, data: PrivateMessage):
        try:
            # self.logging.debug("`on_privmessage` invoked.")
            for module in self.__get_module_with_handler("on_privmessage"):
                module.on_privmessage(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")
        
    def on_usernotice(self, data: UserNotice):
        try:
            # self.logging.debug("`on_usernotice` invoked.")
            for module in self.__get_module_with_handler("on_usernotice"):
                module.on_usernotice(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_ritual_usernotice(self, data: RitualUserNotice):
        try:
            # self.logging.debug("`on_ritual_usernotice` invoked.")
            for module in self.__get_module_with_handler("on_ritual_usernotice"):
                module.on_ritual_usernotice(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_bitbadgeupgrade_usernotice(self, data: BitBadgeUpgradeUserNotice):
        try:
            # self.logging.debug("`on_bitbadgeupgrade_usernotice` invoked.")
            for module in self.__get_module_with_handler("on_bitbadgeupgrade_usernotice"):
                module.on_bitbadgeupgrade_usernotice(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_raid_usernotice(self, data: RaidUserNotice):
        try:
            # self.logging.debug("`on_raid_usernotice` invoked.")
            for module in self.__get_module_with_handler("on_raid_usernotice"):
                module.on_raid_usernotice(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_subscriber_usernotice(self, data: SubscriberUserNotice):
        try:
            # self.logging.debug("`on_subscriber_usernotice` invoked.")
            for module in self.__get_module_with_handler("on_subscriber_usernotice"):
                module.on_subscriber_usernotice(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")
    
    def on_giftedsubscriber_usernotice(self, data: GiftedSubscriberUserNotice):
        try:
            # self.logging.debug("`on_giftedsubscriber_usernotice` invoked.")
            for module in self.__get_module_with_handler("on_giftedsubscriber_usernotice"):
                module.on_giftedsubscriber_usernotice(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_whisper(self, data: Whisper):
        try:
            # self.logging.debug("`on_whisper` invoked.")
            for module in self.__get_module_with_handler("on_whisper"):
                module.on_whisper(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_command(self, data: CommandMessage):
        try:
            # self.logging.debug("`on_module` invoked.")
            for module in self.__get_module_with_handler("on_command"):
                module.on_command(data)
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_heartbeat(self):
        try:
            for module in self.__get_module_with_handler("on_heartbeat"):
                module.on_heartbeat()
        except Exception as e:
            self.logging.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")







    # backend modules for managing the loading and processing of module modules
    
    def __cache_modules(self):
        modules = []
        for _file in listdir(path.join(path.dirname(__file__), 'modules/')):
            if "__" not in _file:
                # print ("r1: Found: ", _file)
                filename, ext = path.splitext(_file)
                if '.py' in ext:
                    modules.append(f'jarviscore.modules.{filename}')
        
        if path.exists("modules/"):
            print("Loading custom modules")
            for _file in listdir('modules/'):
                if "__" not in _file:
                    print ("Found: ", _file)
                    filename, ext = path.splitext(_file)
                    if '.py' in ext:
                        modules.append(f'modules.{filename}')
        
        if path.exists("bots/modules/"):
            print("Loading custom modules")
            for _file in listdir('bots/modules/'):
                if "__" not in _file:
                    print ("Found: ", _file)
                    filename, ext = path.splitext(_file)
                    if '.py' in ext:
                        modules.append(f'modules.{filename}')

        for extension in reversed(modules):
            try:
                self._load_module(f'{extension}')
            except Exception as e:
                try:
                    extension = extension.replace("jarviscore", "JarvisCore")
                    print("re-attempting to load: ", extension)
                    self._load_module(f'{extension}')
                except Exception as e:
                    exc = f'{type(e).__name__}: {e}'
                    print(f'Failed to load extension {extension}\n{exc}')
        

    def _load_module(self, name):
        if name in self.__modules:
            raise ExtensionAlreadyLoaded(name)

        spec = util.find_spec(name)
        if spec is None:
            raise ExtensionNotFound(name)

        self._load_from_module_spec(spec, name)

    
    def _load_from_module_spec(self, spec, key):
        lib = util.module_from_spec(spec)
        sys.modules[key] = lib
        try:
            spec.loader.exec_module(lib)
        except Exception as e:
            del sys.modules[key]
            raise ExtensionFailed(key, e) from e

        try:
            setup = getattr(lib, 'setup')
        except AttributeError:
            del sys.modules[key]
            raise NoEntryPointError(key)

        try:
            setup(self)
        except Exception as e:
            del sys.modules[key]
            self._call_module_finalizers(lib, key)
            raise ExtensionFailed(key, e) from e
        else:
            self.__modules[key] = lib

    

    def _call_module_finalizers(self, lib, key):
        try:
            teardown = getattr(lib, 'teardown')
        except AttributeError:
            pass
        else:
            try:
                teardown(self)
            except Exception:
                pass
        finally:
            self.__modules.pop(key, None)
            sys.modules.pop(key, None)

    def __get_module_with_handler(self, handler: str):
        for module in self.__modules:
            try:
                if hasattr(self.__modules[module], handler):
                    yield self.__modules[module]
            except AttributeError:
                pass
            


class ConnectedChannel(Channel):

    def __init__(self, bridge, nick: str, token: str, channel_name: str = "undefined", id = None):
        Channel.__init__(self, bridge, nick, token, channel_name, id)
        self.settings = Settings()
        self.model = Model(self.settings.get_setting("database.user"),
                   self.settings.get_setting("database.pass"))
        jid = self.__get_jarvis_id(id)
        self.__stream_id = None
        if jid is not None:
            self.__j_id = jid[0]
        else:
            self.__j_id = None        
        self.socket = Socket(self, nick, token, id=self.__j_id)


    def __get_jarvis_id(self, twitch_id):
        query = f"Select IdentityID from Identity where TwitchID = '{twitch_id}'"
        return self.model.fetchOne(query)

    def get_IdentityID(self):
        return self.__j_id

    def get_streamID(self):
        return self.__stream_id


    def set_streamID(self, stream_id):
        self.__stream_id = stream_id
        self.socket.set_stream_id(stream_id)
    
    def get_setting(self, setting):
        return self.settings.get_setting(setting)

    def get_all_settings(self):
        return self.settings.get_all_settings()

    def fetchOne(self, query):
        return self.model.fetchOne(query)

    def fetchAll(self, query):
        return self.model.fetchAll(query)

    def update(self, query):
        self.model.update(query)

    def insert(self, query):
        self.model.insert(query)
    
    def delete(self, query):
        self.model.delete(query)

    def get_timestamp(self):
        return self.model.get_timestamp()

    def log(self, message):
        self.logging.log(message)

    def info(self, message):
        self.logging.info(message)

    def warn(self, message):
        self.logging.warn(message)

    def error(self, message):
        self.logging.error(message)


    def get_setting_from_db(self, setting_key:str):
        """
        Get the setting value for a setting.
        
        Params: 
        setting_key (string) - the key of the setting in question
        """

        query = f"SELECT SettingValue from Channel_Settings c inner join Identity i on c.IdentityID = i.IdentityID \
            WHERE c.SettingKey = '{setting_key}' and i.TwitchID = '{self.getID()}'"

        return self.model.fetchOne(query)


    def set_setting_in_db(self, setting_key: str, setting_value: str):
        """
        Set a setting value in the database based on the key provided

        Params:
        setting_key (string) - the key of the setting in question
        setting_value (string) - the value of the setting in question
        """
        
        query = f"SELECT IdentityID FROM Identity WHERE TwitchID = '{self.getID()}'"
        print("base", query)
        IdentityId = self.model.fetchOne(query)
        if IdentityId is None:
            raise SettingException(f"No Identity could be found for the Twitch ID provided -> '{self.getID()}'")
        
        existing_query = f"""
        SELECT SettingID FROM Channel_Settings Where IdentityID = '{IdentityId[0]}' and SettingKey = '{setting_key}'
        """
        print("existing", existing_query)
        SettingId = self.model.fetchOne(existing_query)
        if SettingId is None:
            insert_query = f"""
            INSERT INTO Channel_Settings
            (SettingKey, SettingValue, IdentityID)
            VALUES ('{setting_key}','{setting_value}', '{IdentityId[0]}')
            """
            print("insert", insert_query)
            self.model.insert(insert_query)
        else:
            update_query = f"""
            UPDATE Channel_Settings
            Set SettingValue = '{setting_value}'
            WHERE SettingID = '{SettingId[0]}'
            """
            print("update", update_query)
            self.model.insert(update_query)



        
        

    
