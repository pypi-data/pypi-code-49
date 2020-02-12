
import base64
import dateutil.parser
import datetime
import cro_validate.api.exception_api as ExceptionApi


def tenant_code(value):
	split = value.split('+')
	if len(split) != 2:
		raise ExceptionApi.create_input_error('tenant_code', 'Invalid format')
	
	yard_code = split[0]
	try:
		location_id = int(split[1])
	except:
		raise ExceptionApi.create_input_error('tenant_code', 'Invalid format')

	return (yard_code, location_id)


def parse_datetime(value):
	dt = dateutil.parser.parse(value, fuzzy=False)
	if not dt.tzinfo:
		dt = dt.replace(tzinfo=datetime.timezone.utc)
	return dt


def parse_base64(value):
	decoded = base64.b64decode(value, validate=True)
	return decoded