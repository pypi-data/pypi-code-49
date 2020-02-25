"""F5 TEEM Library

    Example -- Basic::

        from f5teem import AnonymousDeviceClient

        client_info = {
            'name': 'f5-product-test',
            'version': '1.0.0',
            'id': '<asset UUID>'
        }
        telemetry_client = AnonymousDeviceClient(client_info, api_key='<API KEY>')
        telemetry_client.report(
            {
                'foo': 'bar'
            },
            telemetry_type='Installation Usage',
            telemetry_type_version='1'
        )
"""

from .anonymous_device_client import AnonymousDeviceClient

__all__ = [
    'AnonymousDeviceClient'
]
