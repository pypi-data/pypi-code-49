import json
import os
from ._constants import AZURE_CLIENT_ID

def _resolve_azure_access_token(request, writer, socket):
    try:
        from azure.identity import (ChainedTokenCredential, ManagedIdentityCredential, ClientSecretCredential,
                                    InteractiveBrowserCredential, DeviceCodeCredential)

        scope = request.get('scope')
        sp = request.get('sp')

        credentials = [ManagedIdentityCredential()]
        if sp is not None:
            sp_cred = json.loads(sp)
            credentials.append(ClientSecretCredential(sp_cred['tenantId'], sp_cred['servicePrincipalId'], sp_cred['password']))
        else:
            # user interaction required
            print('Credentials are not provided to access data from source. Please sign in using identity with required permission granted.')
            credentials.append(InteractiveBrowserCredential())
            credentials.append(DeviceCodeCredential(AZURE_CLIENT_ID))

        access_token = ChainedTokenCredential(*credentials).get_token(scope)
        writer.write(json.dumps({
            'result': 'success',
            'token': access_token.token,
            'seconds': access_token.expires_on
        }))
    except Exception as e:
        writer.write(json.dumps({'result': 'error', 'error': str(e)}))


def register_access_token_resolver(requests_channel):
    requests_channel.register_handler('resolve_azure_access_token', _resolve_azure_access_token)
