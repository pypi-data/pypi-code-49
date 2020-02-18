from .exceptions import ParameterIncompleteException
from .generics import CrudEntity


class Campaign(CrudEntity):
    def create(self, **kwargs):
        self.endpoint = '/api/marketing/campaigns/'
        return super(Campaign, self).create(**kwargs)

    def list(self, url_params=None, **kwargs):
        self.endpoint = '/api/marketing/campaigns/'
        return super(Campaign, self).list(url_params, **kwargs)

    def retrieve(self, url_params=None, **kwargs):
        id_ = kwargs.pop('id', None)
        if not id_:
            raise ParameterIncompleteException('Campaign ID {} is invalid'.format(id_))
        self.endpoint = '/api/marketing/campaigns/' + str(id_) + '/'
        return super(Campaign, self).retrieve(url_params, **kwargs)

    def update(self, url_params=None, **kwargs):
        id_ = kwargs.pop('id', None)
        if not id_:
            raise ParameterIncompleteException('Campaign ID {} is invalid'.format(id_))
        self.endpoint = '/api/marketing/campaigns/' + str(id_) + '/'
        return super(Campaign, self).update(url_params, **kwargs)

    def archive(self, **kwargs):
        id_ = kwargs.pop('id', None)
        if not id_:
            raise ParameterIncompleteException('Campaign ID {} is invalid'.format(id_))
        self.endpoint = '/api/marketing/campaigns/' + str(id_) + '/archive_campaign/'
        return super(Campaign, self).retrieve(None, **kwargs)

    def delete(self, url_params=None, **kwargs):
        id_ = kwargs.pop('id', None)
        if not id_:
            raise ParameterIncompleteException('Campaign ID {} is invalid'.format(id_))
        self.endpoint = '/api/marketing/campaigns/' + str(id_) + '/'
        return super(Campaign, self).delete(url_params)

    def trigger(self, **kwargs):
        kwargs['skip_inspect'] = True
        campaign_id = kwargs.pop('id', None)
        if not campaign_id:
            raise ParameterIncompleteException('Campaign ID {} is invalid'.format(campaign_id))
        self.endpoint = '/api/marketing/campaigns/' + str(campaign_id) + '/trigger/'
        return super(Campaign, self).create(None, **kwargs)


class CampaignChannel(CrudEntity):
    channel = None
    endpoint = '/api/marketing/campaigns/cp_id/cp_chan/'

    """
        The methods of this class take in 'campaign_id': The id of the parent campaign and then any other attributes of
        the channel.
        e.g. LinkFusions(token).EmailChannel.create(campaign_id=345, email_type='basic', template=1)
    """

    def inspect_endpoint(self, **kwargs):
        campaign_id = kwargs.pop('campaign_id', None)
        if not campaign_id:
            raise ParameterIncompleteException('Campaign ID {} is invalid'.format(campaign_id))
        self.endpoint = self.endpoint.replace('cp_id', str(campaign_id)).replace('cp_chan', self.channel)


class EmailChannel(CampaignChannel):
    channel = 'email'


class VoiceChannel(CampaignChannel):
    channel = 'voice'


class SMSChannel(CampaignChannel):
    channel = 'sms'


class MMSChannel(CampaignChannel):
    channel = 'mms'


