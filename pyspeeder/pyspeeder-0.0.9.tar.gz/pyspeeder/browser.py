from copy import deepcopy
import os
import time
from platform import system

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class Chrome:
    def __init__(self,
                 driver_path=None,
                 headless=False,
                 no_image=False,
                 user_agent=None,
                 http_proxy=None,
                 lang=None):
        options = Options()
        options.add_argument('--headless') if headless else None
        options.add_argument(f'user-agent={user_agent}') if user_agent else None
        options.add_argument(f'lang={lang}') if lang else None
        options.add_argument('--no-sandbox') if system() == 'Linux' else None
        options.add_argument(f'--proxy-server={http_proxy}') if http_proxy else None
        if no_image:
            option_load_img = {'profile.managed_default_content_settings.images': 2}
            options.add_experimental_option('prefs', option_load_img)
        path = '/lib/chromedriver' if system() == 'Linux' else 'chromedriver'
        self.driver = webdriver.Chrome(
            executable_path=path if driver_path is None else driver_path,
            chrome_options=options
        )

    def get(self, url, timeout=0, switch=True, keep_cookie=False):
        self.driver.set_page_load_timeout(timeout) if timeout else None
        self.driver.set_script_timeout(timeout) if timeout else None
        if not keep_cookie:
            self.driver.delete_all_cookies()
        self.driver.execute_script(f'window.open("{url}")')
        if switch:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    def get_cookies(self):
        return {item['name']: item['value'] for item in self.driver.get_cookies()}

    def set_cookies(self, cookie, keep_cookie=False):
        if not keep_cookie:
            self.driver.delete_all_cookies()
        for key, value in cookie.items():
            self.driver.add_cookie({'name': key, 'value': value})

    def screen_crop(self, xpath):
        image_path = 'screen_shoot.png'
        self.driver.get_screenshot_as_file(image_path)
        element = self.driver.find_element_by_xpath(xpath)
        x = element.location['x']
        y = element.location['y']
        w = element.size['width']
        h = element.size['height']
        image = Image.open(image_path)
        region = image.crop((x, y, x + w, y + h))
        region.save(image_path)

        with open(image_path, 'rb') as file:
            image_bytes = deepcopy(file.read())
        os.remove(image_path)
        return image_bytes

    def wait_until(self, keyword, timeout=30):
        if timeout <= 0:
            return False
        elif keyword in self.driver.page_source:
            return True
        else:
            time.sleep(1)
            return self.wait_until(keyword, timeout - 1)

    def select_by_value(self, xpath, value):
        select = Select(self.driver.find_element_by_xpath(xpath))
        select.select_by_value(value)
