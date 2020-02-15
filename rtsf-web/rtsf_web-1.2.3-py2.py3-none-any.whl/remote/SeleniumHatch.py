# -*- encoding: utf-8 -*-
'''
Current module: rock4.softtest.web.SeleniumHatch

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      rock4.softtest.web.SeleniumHatch,v 1.0 2017年2月27日
    FROM:   2017年2月27日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

import requests,re
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

        
class SeleniumHatch(object):
    ''' Hatch remote browser driver from selenium grid '''
        
    @staticmethod
    def get_remote_executors(hub_ip, port = 4444):
        ''' Get remote hosts from Selenium Grid Hub Console
        @param hub_ip: hub ip of selenium grid hub
        @param port: hub port of selenium grid hub
        '''
        resp = requests.get("http://%s:%s/grid/console" %(hub_ip, port))
        
        remote_hosts = ()
        if resp.status_code == 200:
            remote_hosts = re.findall("remoteHost: ([\w/\.:]+)",resp.text)
        return [host + "/wd/hub" for host in remote_hosts]
    
    @staticmethod
    def get_remote_browser_capabilities(browser = "chrome", download_path = None, marionette = False):
        '''        
        @param browser: firefox chrome opera safari internetexplorer edge htmlunit htmlunitwithjs
        @param marionette: use firefox's geckodriver if True. selenium 3.x开始，webdriver/firefox/webdriver.py的__init__中，executable_path="geckodriver"; 而2.x是executable_path="wires"; 也就是说， firefox 47以上版本，需要下载第三方driver，即geckodriver。
        @param download_path:  set a download path for browser.
        @return:  return the capabilities of this browser 
        '''
        
        browser = browser.upper()            
        cap = getattr(DesiredCapabilities, browser).copy() 
                
        if browser == "FIREFOX":
            cap['marionette'] = marionette;#          
            if download_path:
                fp = webdriver.FirefoxProfile() 
                fp.set_preference("browser.download.folderList", 2);# 设置Firefox的默认 下载 文件夹。0是桌面；1是“我的下载”；2是自定义
                fp.set_preference("browser.download.manager.showWhenStarting", False)
                fp.set_preference("browser.download.dir", download_path)
                fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
                cap['firefox_profile'] = fp
                                      
        elif browser == "CHROME":
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            if download_path:
                prefs = {"download.default_directory": download_path}
                options.add_experimental_option("prefs", prefs)
            cap = options.to_capabilities()
        return cap
    
    @staticmethod
    def gen_remote_driver(executor, capabilities):
        ''' Generate remote drivers with desired capabilities(self.__caps) and command_executor
        @param executor: command executor for selenium remote driver
        @param capabilities: A dictionary of capabilities to request when starting the browser session.
        @return: remote driver
        '''        
        # selenium requires browser's driver and PATH env. Firefox's driver is required for selenium3.0            
        firefox_profile = capabilities.pop("firefox_profile",None)            
        return webdriver.Remote(executor, desired_capabilities=capabilities, browser_profile = firefox_profile)
    
    @staticmethod
    def gen_local_driver(browser, capabilities):
        ''' Generate localhost drivers with desired capabilities(self.__caps)
        @param browser:  firefox or chrome
        @param capabilities:  A dictionary of capabilities to request when starting the browser session.
        @return:  localhost driver
        '''
        if browser == "firefox":
            fp = capabilities.pop("firefox_profile",None)
            return webdriver.Firefox(desired_capabilities =capabilities, firefox_profile=fp)
                   
        elif browser == "chrome":            
            return webdriver.Chrome(desired_capabilities=capabilities)
        
        else:
            raise TypeError("Unsupport browser {}".format(browser))
            
    
    
