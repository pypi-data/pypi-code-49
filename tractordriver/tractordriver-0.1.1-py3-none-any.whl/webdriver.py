from selenium import webdriver
from webdrivermanager import ChromeDriverManager, OperaChromiumDriverManager, GeckoDriverManager, EdgeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.microsoft import IEDriverManager
import os
from tractordriver.TractorScripts import TractorDriver


class Firefox(TractorDriver, webdriver.Firefox):
    def __init__(self, manual_mode=False, firefox_profile=None, firefox_binary=None,
                 timeout=30, capabilities=None, proxy=None,
                 executable_path="geckodriver", options=None,
                 log_path="geckodriver.log", firefox_options=None,
                 service_args=None, desired_capabilities=None):
        if not manual_mode:
            executable_path = GeckoDriverManager().download_and_install()[0]
            os.environ["webdriver.firefox.driver"] = executable_path
        super(Firefox, self).__init__(firefox_profile=firefox_profile, firefox_binary=firefox_binary,
                                      timeout=timeout, capabilities=capabilities, proxy=proxy,
                                      executable_path=executable_path, options=options,
                                      log_path=log_path, firefox_options=firefox_options,
                                      service_args=service_args, desired_capabilities=desired_capabilities)


class Chrome(TractorDriver, webdriver.Chrome):
    def __init__(self, executable_path=None, port=0,
                 options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None, version='latest'):
        if not executable_path:
            executable_path = ChromeDriverManager().download_and_install(version=version)[0]
            # os.environ["webdriver.chrome.driver"] = executable_path
        super(Chrome, self).__init__(executable_path=executable_path, port=port,
                                     options=options, service_args=service_args,
                                     desired_capabilities=desired_capabilities, service_log_path=service_log_path,
                                     chrome_options=chrome_options)


class Safari(TractorDriver, webdriver.Safari):
    pass


class Ie(TractorDriver, webdriver.Ie):
    def __init__(self, executable_path=None):
        if not executable_path:
            executable_path = IEDriverManager().install()
            os.environ["webdriver.ie.driver"] = executable_path
        super(Ie, self).__init__(executable_path=executable_path)


class Edge(TractorDriver, webdriver.Edge):

    def __init__(self, executable_path=None):
        if not executable_path:
            executable_path = EdgeDriverManager().download_and_install()[0]
            os.environ["webdriver.edge.driver"] = executable_path
        super(Edge, self).__init__(executable_path=executable_path)


class Opera(TractorDriver, webdriver.Opera):
    def __init__(self, executable_path=None,
                 desired_capabilities=None,
                 port=0,
                 service_log_path=None,
                 service_args=None,
                 options=None):
        if not executable_path:
            executable_path = OperaChromiumDriverManager().download_and_install()[0]
            os.environ["webdriver.opera.driver"] = executable_path
        super(Opera, self).__init__(executable_path=executable_path,
                                    desired_capabilities=desired_capabilities,
                                    port=port,
                                    service_log_path=service_log_path,
                                    service_args=service_args,
                                    options=options)


class BlackBerry(TractorDriver, webdriver.BlackBerry):
    pass


class PhantomJS(TractorDriver, webdriver.PhantomJS):
    pass


class Android(TractorDriver, webdriver.Android):
    pass


class WebKitGTK(TractorDriver, webdriver.WebKitGTK):
    pass


class Remote(TractorDriver, webdriver.Remote):
    pass
