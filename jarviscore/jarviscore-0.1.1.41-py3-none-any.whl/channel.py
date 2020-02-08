import sys
from importlib import util
from copy import deepcopy
from os import path, listdir
from threading import Thread
from time import sleep


from .socket import Socket
from .module import Module
from .message import *
from .errors import ExtensionAlreadyLoaded, ExtensionNotFound, ExtensionFailed, NoEntryPointError 

from .log import Log


class Channel(Thread):

    name: str
    __modules: dict
    socket: Socket

    def __init__(self, bridge, nick: str, token: str, channel_name: str = "undefined", id = None):
        Thread.__init__(self)
        self.name = f"Thread-Channel: {channel_name}"
        self.channel_name = channel_name.lower()
        self.socket = Socket(self, nick, token)
        self.bridge = bridge
        self.__id = id
        self.__modules = {}
        self.active = True
        self.__cache_modules()

        self.log = Log(instance=channel_name, client="Twitch Channel")
        pass

    # Public modules for use in the Bridge and in modules

    def getID(self):
        if self.__id is None:
            return 0
        return self.__id

    def send(self, message):
        self.socket.send_message(self.channel_name, message)

    def load_module(self, module):
        self.__modules[module.name] = module

    def on_new_connection(self, channel: str):
        # self.log.debug("`on_new_connection` invoked.")
        for module in self.__get_module_with_handler("on_new_connection"):
            module.on_new_connection(channel)
        
    def run(self):
        try:
            while self.active: 
                self.socket.listenToStream()
                sleep(0.00001)
        except KeyboardInterrupt:
            self.log.log(f"Closing connection to {self.channel_name}")
            self.socket.close()
            self.active = False

    def close(self):
        self.log.log(f"Closing connection to {self.channel_name}")
        self.active = False
        self.socket.close()



    # Callbacks used by the bridge for all Messages sent via the inbound socket.

    ### to do: add the rest of the message types in here

    # Base Callback
    def on_raw(self, data: RawMessage):
        try:
            # self.log.debug("`on_raw` invoked.")
            for module in self.__get_module_with_handler("on_raw"):
                module.on_raw(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    # IRC: Membership Callbacks

    def on_join(self, data: Join):
        try:
            # self.log.debug("`on_join` invoked.")
            for module in self.__get_module_with_handler("on_join"):
                module.on_join(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_part(self, data: Part):
        try:
            # self.log.debug("`on_part` invoked.")
            for module in self.__get_module_with_handler("on_part"):
                module.on_part(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_mode(self, data: Mode):
        try:
            # self.log.debug("`on_mode` invoked.") 
            for module in self.__get_module_with_handler("on_mode"):
                module.on_mode(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_names(self, data: Names):
        try:
            # self.log.debug("`on_names` invoked.")
            for module in self.__get_module_with_handler("on_names"):
                module.on_names(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    # IRC: module & Tag Callbacks

    def on_clearchat(self, data: ClearChat):
        try:
            # self.log.debug("`on_clearchat` invoked.")
            for module in self.__get_module_with_handler("on_clearchat"):
                module.on_clearchat(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_clearmessage(self, data: ClearMessage):
        try:
            # self.log.debug("`on_clearmessage` invoked.")
            for module in self.__get_module_with_handler("on_clearmessage"):
                module.on_clearmessage(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")
    
    def on_hosttarget(self, data: HostTarget):
        try:
            # self.log.debug("`on_hosttarget` invoked.")
            for module in self.__get_module_with_handler("on_hosttarget"):
                module.on_hosttarget(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_notice(self, data: Notice):
        try:
            # self.log.debug(f"`on_notice` invoked. (not implemented)")
            for module in self.__get_module_with_handler("on_notice"):
                module.on_notice(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_reconnect(self, data: Reconnect):
        try:
            # self.log.debug("`on_reconnect` invoked.")
            for module in self.__get_module_with_handler("on_reconnect"):
                module.on_reconnect(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_roomstate(self, data: RoomState):
        try:
            # self.log.debug("`on_roomstate` invoked.")
            for module in self.__get_module_with_handler("on_roomstate"):
                module.on_roomstate(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_userstate(self, data: UserState):
        try:
            # self.log.debug("`on_userstate` invoked.")
            for module in self.__get_module_with_handler("on_userstate"):
                module.on_userstate(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_globaluserstate(self, data: GlobalUserState):
        try:
            # self.log.debug("`on_globaluserstate` invoked.")
            for module in self.__get_module_with_handler("on_globaluserstate"):
                module.on_globaluserstate(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_privmessage(self, data: PrivateMessage):
        try:
            # self.log.debug("`on_privmessage` invoked.")
            for module in self.__get_module_with_handler("on_privmessage"):
                module.on_privmessage(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")
        
    def on_usernotice(self, data: UserNotice):
        try:
            # self.log.debug("`on_usernotice` invoked.")
            for module in self.__get_module_with_handler("on_usernotice"):
                module.on_usernotice(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_ritual_usernotice(self, data: RitualUserNotice):
        try:
            # self.log.debug("`on_ritual_usernotice` invoked.")
            for module in self.__get_module_with_handler("on_ritual_usernotice"):
                module.on_ritual_usernotice(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_bitbadgeupgrade_usernotice(self, data: BitBadgeUpgradeUserNotice):
        try:
            # self.log.debug("`on_bitbadgeupgrade_usernotice` invoked.")
            for module in self.__get_module_with_handler("on_bitbadgeupgrade_usernotice"):
                module.on_bitbadgeupgrade_usernotice(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_raid_usernotice(self, data: RaidUserNotice):
        try:
            # self.log.debug("`on_raid_usernotice` invoked.")
            for module in self.__get_module_with_handler("on_raid_usernotice"):
                module.on_raid_usernotice(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_subscriber_usernotice(self, data: SubscriberUserNotice):
        try:
            # self.log.debug("`on_subscriber_usernotice` invoked.")
            for module in self.__get_module_with_handler("on_subscriber_usernotice"):
                module.on_subscriber_usernotice(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")
    
    def on_giftedsubscriber_usernotice(self, data: GiftedSubscriberUserNotice):
        try:
            # self.log.debug("`on_giftedsubscriber_usernotice` invoked.")
            for module in self.__get_module_with_handler("on_giftedsubscriber_usernotice"):
                module.on_giftedsubscriber_usernotice(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_whisper(self, data: Whisper):
        try:
            # self.log.debug("`on_whisper` invoked.")
            for module in self.__get_module_with_handler("on_whisper"):
                module.on_whisper(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")

    def on_command(self, data: CommandMessage):
        try:
            # self.log.debug("`on_module` invoked.")
            for module in self.__get_module_with_handler("on_command"):
                module.on_command(data)
        except Exception as e:
            self.log.error(f"Suppressing a caught an exception, will continue without raising. Details below\n{type(e)}: {e}")






    # backend modules for managing the loading and processing of module modules
    
    def __cache_modules(self):
        modules = []
        for _file in listdir(path.join(path.dirname(__file__), 'modules/')):
            if "__init__" not in _file and "__pycache__" not in _file:
                # print ("r1: Found: ", _file)
                filename, ext = path.splitext(_file)
                if '.py' in ext:
                    modules.append(f'jarviscore.modules.{filename}')
        
        if path.exists("modules/"):
            print("Loading custom modules")
            for _file in listdir('modules/'):
                if "__init__" not in _file and "__pycache__" not in _file:
                    print ("Found: ", _file)
                    filename, ext = path.splitext(_file)
                    if '.py' in ext:
                        modules.append(f'modules.{filename}')
        
        if path.exists("bots/modules/"):
            print("Loading custom modules")
            for _file in listdir('bots/modules/'):
                if "__init__" not in _file and "__pycache__" not in _file:
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
            


            


        
        

    
