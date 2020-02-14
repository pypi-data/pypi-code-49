import inspect


class LoggingAspect:

    @staticmethod
    def invoke_pre_call_aspects(dli_client, metadata):
        if getattr(dli_client, 'logger', None):
            try:
                dli_client.logger.info('Client Function Called', extra=metadata)
            except Exception as e:
                dli_client.logger.exception(
                    'Error while invoking pre-call aspects.', e
                )

    @staticmethod
    def invoke_post_call_aspects(wrapped, metadata):
        pass

    @staticmethod
    def invoke_after_exception_aspects(wrapped_object, metadata, exception):
        if getattr(wrapped_object, 'logger', None):
            try:
                wrapped_object.logger.exception(
                    'Unhandled Exception', stack_info=True, extra={
                        'locals': inspect.trace()[-1][0].f_locals
                    })
            except Exception as e:
                wrapped_object.logger.exception(
                    'Error while invoking pre-call aspects.', e
                )


class AnalyticsAspect:

    @staticmethod
    def invoke_pre_call_aspects(dli_client, metadata):
        pass

    def invoke_post_call_aspects(self, dli_client, metadata):
        if getattr(dli_client, '_analytics_handler', None):
            try:
                self._create_event(dli_client, metadata, status_code=200)
            except Exception as e:
                dli_client.logger.exception(
                    'Error while invoking post-call aspects.', e
                )

    def invoke_after_exception_aspects(self, dli_client, metadata, exception):
        if getattr(dli_client, '_analytics_handler', None):
            try:
                status_code = self._retrieve_status_code_from_exception(exception)
                self._create_event(dli_client, metadata, status_code=status_code)
            except Exception as e:
                dli_client.logger.exception(
                    'Error while invoking after-exception aspects.', e
                )

    @staticmethod
    def _create_event(dli_client, metadata, status_code):
        additional_properties = metadata.get('properties') or {}
        dli_client._analytics_handler.create_event(
            metadata['subject'], metadata['organisation_id'],
            metadata['func'].__qualname__.split('.')[0],
            metadata['func'].__name__,
            {**metadata['arguments'], **metadata['kwargs'], **additional_properties},
            result_status_code=status_code
        )

    @staticmethod
    def _retrieve_status_code_from_exception(exception):
        try:
            return exception.response.status_code
        except AttributeError:
            return 500


def analytics_decorator(function, class_fields_to_include):
    aspect = AnalyticsAspect()

    def function_wrapper(target, *args, **kwargs):
        metadata = extract_metadata(
            target._client, target, function, args, kwargs, class_fields_to_include
        )

        aspect.invoke_pre_call_aspects(target._client, metadata)
        try:
            result = function(target, *args, **kwargs)
        except Exception as e:
            aspect.invoke_after_exception_aspects(target._client, metadata, e)
            raise e
        aspect.invoke_post_call_aspects(target._client, metadata)
        return result

    return function_wrapper


def logging_decorator(function, class_fields_to_include):
    aspect = LoggingAspect()

    def function_wrapper(target, *args, **kwargs):
        metadata = extract_metadata(
            target._client, target, function, args, kwargs, class_fields_to_include
        )
        aspect.invoke_pre_call_aspects(target._client, metadata)
        try:
            result = function(target, *args, **kwargs)
        except Exception as e:
            aspect.invoke_after_exception_aspects(target._client, metadata, e)
            raise e
        aspect.invoke_post_call_aspects(target._client, metadata)
        return result

    return function_wrapper


def extract_metadata(
        dli_client, wrapped_object, func, arguments,
        keyword_args, class_fields_to_include=None
):
    # Get the user calling the function
    org_id, subject = _retrieve_user_details(dli_client)

    # This is to find out what the 'arg' names are.
    argspec = inspect.getfullargspec(func)
    args_dict = dict(zip(argspec.args, [wrapped_object, *arguments]))

    properties = _read_field_values(class_fields_to_include, wrapped_object)

    if not subject:
        if args_dict.get('api_key'):
            subject = '***' + args_dict.get('api_key')[:6]
        else:
            subject = 'UNKNOWN USER'

    return {
        'func': func,
        'subject': subject,
        'organisation_id': org_id,
        'arguments': args_dict,
        'kwargs': dict(keyword_args),
        'properties': properties
    }


def _retrieve_user_details(dli_client):
    org_id = None
    user_id = getattr(dli_client, 'api_key', '')[:6]
    try:
        org_id = dli_client.session.decoded_token.get('datalake').get('organisation_id')
        user_id = dli_client.session.decoded_token.get('sub', 'UNKNOWN USER')
    except AttributeError:
        pass

    return org_id, user_id


def _read_field_values(class_fields_to_include, wrapped_object):
    properties = {}
    for field in class_fields_to_include or []:
        property_name = field.split('.')[-1]
        property_value = wrapped_object
        for nested_field_name in field.split('.'):
            property_value = property_value.__dict__[nested_field_name]
        properties.update({property_name: property_value})
    return properties
