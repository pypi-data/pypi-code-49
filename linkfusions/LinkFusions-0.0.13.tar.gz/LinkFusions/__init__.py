__version__ = '0.0.13'

__dev__ = 'live'
# This could be 'local', 'dev', 'live'


def get_url(url):
    if __dev__ == 'local':
        base_url = 'http://localhost:8000'
    elif __dev__ == 'dev':
        base_url = 'https://dev.linkfusions.com'
    else:
        base_url = 'https://app.linkfusions.com'
    return base_url + url


class LinkFusions(object):
    def __init__(self, token):
        from .exceptions import BadRequest
        from .campaigns import EmailChannel, Campaign, MMSChannel, SMSChannel, VoiceChannel
        from .phone_numbers import Numbers, Redirect
        from .templates import Template
        from .contacts import Contact, ContactGroup

        self.EmailChannel = EmailChannel(token)
        self.Campaign = Campaign(token)
        self.Numbers = Numbers(token)
        self.Redirect = Redirect(token)
        self.MMSChannel = MMSChannel(token)
        self.SMSChannel = SMSChannel(token)
        self.VoiceChannel = VoiceChannel(token)
        self.Template = Template(token)
        self.Contact = Contact(token)
        self.ContactGroup = ContactGroup(token)

    @classmethod
    def auth(cls, email, password, client_id, client_secret):
        from .requestor import ApiRequestor
        ep = '/o/token/'
        data = {
            'grant_type': 'password',
            'username': email,
            'password': password,
            'client_id': client_id,
            'client_secret': client_secret
        }
        return ApiRequestor(endpoint=ep, data=data).send(as_json=False)


__all__ = [
    'LinkFusions',
    'get_url',
    '__dev__',
    '__version__'
]
