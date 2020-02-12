import abc

class PluginBase(abc.ABC):
	def __init__(self, spawning_class, name, uuid, family_id):
		self._super_class = spawning_class
		self._child_name = name
		self._child_uuid = uuid
		self._child_family = family_id

	# No need to override methods
	def info(self):
		return {"name": self._child_name, "uuid": self._child_uuid, "family_id": self._child_family}

	# Required to override
	@abc.abstractmethod
	def register_listeners(self):
		pass

	# API Methods
	# Listeners
	def register_key_listener(self, key, listener):
		return self._super_class.register_key_listener(key, listener)

	def register_period_change_listener(self, listener):
		return self._super_class.register_period_change_listener(listener)

	def register_on_loop_listener(self, listener):
		return self._super_class.register_on_loop_listener(listener)

	def get_cross_plugin_data(self, key):
		return self._super_class.get_cross_plugin_data(self, key)

	def save_cross_plugin_data(self, key, value):
		return self._super_class.save_cross_plugin_data(self, key, value)

	
	# Configurations
	def get_current_config(self):
		return self._super_class.get_current_config(self)

	def get_current_family_config(self):
		return self._super_class.get_current_config(self)
