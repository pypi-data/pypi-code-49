

class ExceptionFactory:
	def create_input_error(self, source, message, internal_message, exception, **kw):
		raise NotImplementedError()

	def create_internal_error(self, source, message, exception, **kw):
		raise NotImplementedError()


class DefaultExceptionFactory(ExceptionFactory):
	def create_input_error(self, source, message, internal_message, exception, **kw):
		return ValueError(str(source) + ': ' + str(message))

	def create_internal_error(self, source, message, exception, **kw):
		return SystemError(str(source) + ': ' + str(message))