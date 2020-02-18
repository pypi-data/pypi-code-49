import os
from queue import Queue

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType

from simple_proxy.proxy_info import ProxyInfo
from simple_proxy.proxy_pool import ProxyPool

EXEC_PATH = os.getcwd() + "/chromedriver"


class ProxiedSeleniumPool:
    def __init__(self, proxy_pool: ProxyPool, pool_size: int = 8, headless=True):
        self.__proxy_pool = proxy_pool
        self.__pool_size = pool_size
        self.__headless = headless

        self.__sessions = Queue()
        for _ in range(pool_size):
            self.__sessions.put(self.__build_session(Service(EXEC_PATH)))

    def notify(self, selenium_session):
        self.__sessions.put(selenium_session)

    def get_session(self):
        return self.__sessions.get(True)

    def __build_session(self, service):
        service.start()

        chrome_options = Options()
        chrome_options.add_argument("--window-size=860,908")
        if self.__headless:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--no-default-browser-check')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-default-apps')
        chrome_options.add_argument("ignore-certificate-errors")

        return SeleniumSession(self, self.__proxy_pool, service, chrome_options)

    def __del__(self):
        while self.__sessions.empty():
            self.__sessions.get(True).stop()


class SeleniumSession():
    def __init__(self, observer: ProxiedSeleniumPool, proxy_pool: ProxyPool, service: Service, options: Options):
        self.__observer = observer
        self.__proxy_pool = proxy_pool
        self.__service = service
        self.__options = options

    def __capabilities_for_proxy(self, proxy_info: ProxyInfo):
        capabilities = webdriver.DesiredCapabilities.CHROME
        proxy_info.apply_to_selenium_capabilities(ProxyType.MANUAL, capabilities)

        return capabilities

    def __enter__(self):
        self.__proxy_info = self.__proxy_pool.get_proxy()
        self.__options.add_argument("user-agent={}".format(self.__proxy_pool.get_random_useragent()))
        self.__options.add_argument("--proxy-server={}".format(self.__proxy_info.get_as_url()))

        self.__driver = webdriver.Remote(self.__service.service_url,
                                         options=self.__options)
        return self.__driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.__proxy_info.fail()
        else:
            self.__proxy_info.success()

        self.__proxy_info.close()
        self.__driver.close()

        del self.__proxy_info
        del self.__driver

        self.__observer.notify(self)
