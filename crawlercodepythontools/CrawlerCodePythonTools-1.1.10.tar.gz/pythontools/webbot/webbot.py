import time, pickle, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pythontools.core import tools, logger


class WebBot:

    def Chrome(self, chromedriver, hide=False, user_agent=None):
        chrome_options = Options()
        if hide is True:
            chrome_options.add_argument("--headless")
        if user_agent is not None:
            chrome_options.add_argument("user-agent=" + user_agent)
        if tools.existFile(chromedriver):
            if user_agent is not None or hide is True:
                self.driver = webdriver.Chrome(executable_path=chromedriver.replace(".exe", ""), chrome_options=chrome_options)
            else:
                self.driver = webdriver.Chrome(executable_path=chromedriver.replace(".exe", ""))
            return self
        else:
            logger.error(chromedriver + " not found")
            exit(1)
            return None

    def Firefox(self, geckodriver):
        if tools.existFile(geckodriver):
            self.driver = webdriver.Firefox(executable_path=geckodriver.replace(".exe", ""))
            return self
        else:
            logger.error(geckodriver + " not found")
            return None

    def setImplicitlyWait(self, wait):
        self.driver.implicitly_wait(wait)

    def get(self, link, waitTime=1.5):
        self.driver.get(link)
        time.sleep(waitTime)

    def openNewTab(self):
        self.driver.execute_script("window.open('');")

    def switchToWindow(self, i):
        self.driver.switch_to.window(self.driver.window_handles[i])

    def close(self):
        self.driver.close()
        self.driver.quit()

    def click(self, xpath,  waitTime=1.0):
        button = self.driver.find_element_by_xpath(xpath)
        button.click()
        time.sleep(waitTime)

    def tryClick(self, xpath, waitTime=1.0):
        try:
            button = self.driver.find_element_by_xpath(xpath)
            button.click()
            time.sleep(waitTime)
        except:
            pass

    def input(self, xpath, text, waitTime=0.2):
        inputObj = self.driver.find_element_by_xpath(xpath)
        inputObj.clear()
        inputObj.send_keys(text)
        time.sleep(waitTime)

    def getText(self, xpath):
        return self.driver.find_element_by_xpath(xpath).text

    def getLink(self, xpath):
        return self.driver.find_element_by_xpath(xpath).get_attribute('href')

    def saveCookies(self, name):
        pickle.dump(self.driver.get_cookies(), open(name + ".pkl", "wb"))

    def loadCookies(self, name):
        for cookie in pickle.load(open(name + ".pkl", "rb")):
            self.driver.add_cookie(cookie)

    def addCookie(self, cookie):
        self.driver.add_cookie(cookie)