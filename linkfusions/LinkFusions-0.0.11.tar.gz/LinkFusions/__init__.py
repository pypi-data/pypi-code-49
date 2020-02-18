__version__ = '0.0.11'

__dev__ = 'local'
# This could be 'local', 'dev', 'live'

if __dev__ == 'local':
    BASE_URL = 'http://localhost:8000'
elif __dev__ == 'dev':
    BASE_URL = 'https://dev.linkfusions.com'
elif __dev__ == 'live':
    BASE_URL = 'https://app.linkfusions.com'


def get_url(url):
    return BASE_URL + url


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
