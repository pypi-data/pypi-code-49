import pkg_resources

from directory_client_core.base import AbstractAPIClient
from directory_client_core.helpers import fallback

from django.conf import settings
from django.core.cache import caches


def build_params(language_code=None, draft_token=None, fields=None, region=None, industry=None, limit=None,
                 offset=None):
    params = {'fields': fields or ['*']}
    if language_code:
        params['lang'] = language_code
    if draft_token:
        params['draft_token'] = draft_token
    if region:
        params['region'] = region
    if industry:
        params['industry'] = industry
    if limit:
        params['limit'] = limit
    if offset:
        params['offset'] = offset
    return params


class DirectoryCMSClient(AbstractAPIClient):
    endpoints = {
        'ping': '/healthcheck/ping/',
        'page-by-type': '/api/pages/lookup-by-type/{page_type}/',
        'page-by-slug': '/api/pages/lookup-by-slug/{slug}/',
        'page-by-path': '/api/pages/lookup-by-path/{site_id}/{path}',
        'pages-by-type': '/api/pages/',
        'industry-tags': '/api/pages/industry-tags/',
        'countries-by-tag': '/api/pages/lookup-countries-by-tag/{tag_id}/',
        'regions': '/api/regions/',
        'country-guides': '/api/pages/lookup-countries/'
    }

    version = pkg_resources.get_distribution(__package__).version

    def __init__(
        self, base_url, api_key, sender_id, timeout, default_service_name,
    ):
        super().__init__(base_url, api_key, sender_id, timeout)
        self.default_service_name = default_service_name

    @fallback(cache=caches['cms_fallback'])
    def fallback_cache_get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get(self, *args, use_fallback_cache=False, **kwargs):
        if use_fallback_cache:
            return self.fallback_cache_get(*args, **kwargs)
        return super().get(*args, **kwargs)

    def ping(self, authenticator=None):
        return self.get(url=self.endpoints['ping'], authenticator=authenticator)

    def list_industry_tags(
        self,
        limit=None,
        offset=None,
        authenticator=None,
    ):
        base_params = build_params(
            limit=limit,
            offset=offset
        )
        return self.get(
            url=self.endpoints['industry-tags'],
            params=base_params,
            use_fallback_cache=True,
            authenticator=authenticator,
        )

    def lookup_countries_by_tag(
        self,
        tag_id,
        fields=None,
        draft_token=None,
        language_code=None,
        service_name=None,
        authenticator=None,
    ):
        base_params = build_params(
            fields=fields, language_code=language_code, draft_token=draft_token
        )
        return self.get(
            url=self.endpoints['countries-by-tag'].format(tag_id=tag_id),
            params={
                **base_params,
                'service_name': service_name or self.default_service_name,
            },
            use_fallback_cache=True,
            authenticator=authenticator,
        )

    def lookup_by_slug(
        self,
        slug,
        fields=None,
        draft_token=None,
        language_code=None,
        service_name=None,
        region=None,
        authenticator=None,
    ):
        base_params = build_params(
            fields=fields,
            language_code=language_code,
            draft_token=draft_token,
            region=region,
        )

        return self.get(
            url=self.endpoints['page-by-slug'].format(slug=slug),
            params={
                **base_params,
                'service_name': service_name or self.default_service_name,
            },
            use_fallback_cache=True,
            authenticator=authenticator,
        )

    def lookup_by_path(
        self,
        site_id,
        path,
        fields=None,
        draft_token=None,
        language_code=None,
        region=None,
        authenticator=None,
    ):
        base_params = build_params(
            fields=fields,
            draft_token=draft_token,
            language_code=language_code,
            region=region,
        )
        url = self.endpoints['page-by-path'].format(site_id=site_id, path=path)
        return self.get(
            url=url,
            params=base_params,
            use_fallback_cache=True,
            authenticator=authenticator,
        )

    def list_by_page_type(
        self,
        page_type,
        fields=None,
        draft_token=None,
        language_code=None,
        limit=None,
        offset=None,
        authenticator=None,
    ):
        base_params = build_params(
            fields=fields, language_code=language_code,
            draft_token=draft_token,
            limit=limit,
            offset=offset
        )
        return self.get(
            url=self.endpoints['pages-by-type'],
            params={
                **base_params,
                'type': page_type,
            },
            use_fallback_cache=True,
            authenticator=authenticator,
        )

    def list_regions(self, authenticator=None):
        return self.get(
            url=self.endpoints['regions'],
            use_fallback_cache=True,
            authenticator=authenticator,
        )

    def lookup_country_guides(self, industry=None, region=None, authenticator=None):
        base_params = build_params(industry=industry, region=region)
        return self.get(
            url=self.endpoints['country-guides'],
            params=base_params,
            use_fallback_cache=True,
            authenticator=authenticator,
        )


cms_api_client = DirectoryCMSClient(
    base_url=settings.DIRECTORY_CMS_API_CLIENT_BASE_URL,
    api_key=settings.DIRECTORY_CMS_API_CLIENT_API_KEY,
    sender_id=settings.DIRECTORY_CMS_API_CLIENT_SENDER_ID,
    timeout=settings.DIRECTORY_CMS_API_CLIENT_DEFAULT_TIMEOUT,
    default_service_name=settings.DIRECTORY_CMS_API_CLIENT_SERVICE_NAME,
)
