__version__ = '0.0.15'

__dev__ = 'live'
# This could be 'local', 'dev', 'live'

CLIENT_ID = None
CLIENT_SECRET = None
USER = None
PASSWORD = None

TOKEN = None


def get_url(url):
    if __dev__ == 'local':
        base_url = 'http://localhost:8000'
    elif __dev__ == 'dev':
        base_url = 'https://dev.linkfusions.com'
    else:
        base_url = 'https://app.linkfusions.com'
    return base_url + url


def get_credentials():
    return {
        'grant_type': 'password',
        'username': USER,
        'password': PASSWORD,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }


def get_token():
    return TOKEN


class LinkFusions(object):
    def __init__(self):
        from .exceptions import BadRequest
        from .campaigns import EmailChannel, Campaign, MMSChannel, SMSChannel, VoiceChannel
        from .phone_numbers import Numbers, Redirect
        from .templates import Template
        from .contacts import Contact, ContactGroup

        if not get_token():
            global TOKEN
            TOKEN = self.__class__.auth().get('access_token')
        self.EmailChannel = EmailChannel(get_token())
        self.Campaign = Campaign(get_token())
        self.Numbers = Numbers(get_token())
        self.Redirect = Redirect(get_token())
        self.MMSChannel = MMSChannel(get_token())
        self.SMSChannel = SMSChannel(get_token())
        self.VoiceChannel = VoiceChannel(get_token())
        self.Template = Template(get_token())
        self.Contact = Contact(get_token())
        self.ContactGroup = ContactGroup(get_token())

    @classmethod
    def auth(cls):
        from .requestor import ApiRequestor
        from .exceptions import BadRequest, InvalidCredentialsException
        ep = '/o/token/'
        data = get_credentials()
        try:
            return ApiRequestor(endpoint=ep, data=data).send(as_json=False)
        except BadRequest as e:
            raise InvalidCredentialsException(str(e))


__all__ = [
    'LinkFusions',
    'get_url',
    '__dev__',
    '__version__'
]
