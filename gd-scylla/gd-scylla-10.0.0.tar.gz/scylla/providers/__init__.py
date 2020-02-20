from scylla.providers.proxy_list_provider import ProxyListProvider
from scylla.providers.proxy_scraper_provider import ProxyScraperProvider
from scylla.providers.proxylists_provider import ProxylistsProvider
from scylla.providers.proxynova_provider import ProxyNovaProvider
from scylla.providers.pubproxy_provider import PubproxyProvider
from scylla.providers.rmccurdy_provider import RmccurdyProvider
from scylla.providers.rudnkh_provider import RudnkhProvider
from scylla.providers.the_speedX_provider import TheSpeedXProvider
from .a2u_provider import A2uProvider
from .base_provider import BaseProvider
from .cool_proxy_provider import CoolProxyProvider
from .data5u_provider import Data5uProvider
from .free_proxy_list_provider import FreeProxyListProvider
from .http_proxy_provider import HttpProxyProvider
from .ipaddress_provider import IpaddressProvider
from .kuaidaili_provider import KuaidailiProvider
from .spys_me_provider import SpyMeProvider
from .spys_one_provider import SpysOneProvider
from .xici_provider import XiciProvider
from .github_fate0_provide import GithubFate0Provider
from .proxy11_provider import ProxyElevenProvider
from .proxy_list_download_provider import ProxyListDownloadProvider
from .proxy_us_provider import ProxyUSProvider
from .hidemyname_provider import HideMyNameProvider
from .hidemyip_provider import HideMyIpProvider
from .checkerproxy_provider import CheckerProxyProvider
from .proxyrack_provider import ProxyRackProvider
from .proxydaily_provider import ProxyDailyProvider
from .sslproxies_provider import SslProxiesProvider
from .seotoolsblog_provider import SeoToolsProvider
from .proxylisticu_provider import ProxyListIcuProvider
from .freeproxylist_appspot_provider import FreeProxyListAppspotProvider


all_providers = [
    A2uProvider,
    CoolProxyProvider,
    Data5uProvider,
    FreeProxyListProvider,
    HttpProxyProvider,
    # KuaidailiProvider,
    SpyMeProvider,
    SpysOneProvider,
    # XiciProvider
    IpaddressProvider,
    ProxyListProvider,
    ProxyScraperProvider,
    ProxylistsProvider,
    ProxyNovaProvider,
    PubproxyProvider,
    RmccurdyProvider,
    RudnkhProvider,
    TheSpeedXProvider,
    GithubFate0Provider,
    ProxyElevenProvider, #working,50
    ProxyListDownloadProvider, #not working ,50
    ProxyUSProvider, #working ,0
    HideMyIpProvider, #working
    CheckerProxyProvider,
    ProxyRackProvider,
    ProxyDailyProvider, #working
    SslProxiesProvider, #working , 100
    SeoToolsProvider, #working , 51, one error2
    ProxyListIcuProvider, #working, 25
    FreeProxyListAppspotProvider, #working, 175
    
]

# Provider references:
# https://github.com/franklingu/proxypool/issues/2
