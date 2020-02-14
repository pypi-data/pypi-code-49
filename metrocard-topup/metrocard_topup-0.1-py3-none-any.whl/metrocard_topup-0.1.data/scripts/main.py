#!python

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import sys
import time

from xpaths import *
from credentials import (
    credit_card_number,
    credit_card_name,
    credit_card_expiry_month,
    credit_card_expiry_year,
    credit_card_cvc,
    metrocard_number,
    metrocard_password,
)

from utils import send_email

METROCARD_URL = "https://metrocard.metroinfo.co.nz"
TOPUP_PAGE = "https://metrocard.metroinfo.co.nz/#/profile/topup"


class MetroTopup:
    def __init__(self, username, password):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.username = username
        self.password = password
        self.current_balance = -1

    def open_metroinfo_page(self):
        self.driver.get(METROCARD_URL)

    def login(self):

        self.driver.find_element_by_xpath(username_input_xpath).send_keys(self.username)
        self.driver.find_element_by_xpath(password_input_xpath).send_keys(self.password)
        self.driver.find_element_by_xpath(login_button_xpath).click()

    def wait_for_main_page(self):
        self.wait.until(
            ec.visibility_of_element_located((By.XPATH, greeting_text_xpath))
        )

    def get_current_balance(self):
        current_balance = self.driver.find_element_by_xpath(current_balance_xpath).text
        self.current_balance = float(current_balance[1:])
        return self.current_balance

    def open_top_up_page(self):
        self.driver.get(TOPUP_PAGE)
        self.wait.until(
            ec.visibility_of_element_located((By.XPATH, top_up_checkout_xpath))
        )
        self.driver.find_element_by_xpath(top_up_button_xpath).click()

    def _slow_type(self, element, text):
        for letter in text:
            element.send_keys(letter)
            time.sleep(0.03)

        time.sleep(1)

    def top_up(self):
        self.wait.until(
            ec.visibility_of_element_located((By.XPATH, payment_header_xpath))
        )
        element = self.driver.find_element_by_xpath(payment_credit_card_xpath)
        self._slow_type(element, credit_card_number)

        element = self.driver.find_element_by_xpath(payment_credit_name_xpath)
        self._slow_type(element, credit_card_name)

        element = self.driver.find_element_by_xpath(payment_credit_expiry_month_xpath)
        starting_month = 1
        for _ in range(credit_card_expiry_month - starting_month):
            element.send_keys(Keys.DOWN)

        element = self.driver.find_element_by_xpath(payment_credit_expiry_year_xpath)
        self._slow_type(element, credit_card_expiry_year)

        element = self.driver.find_element_by_xpath(payment_credit_cvc_xpath)
        self._slow_type(element, credit_card_cvc)

        self.driver.find_element_by_css_selector("button.DpsButton1").click()

        time.sleep(2)

        self.wait.until(
            ec.visibility_of_element_located((By.XPATH, payment_header_xpath))
        )

    def close(self):
        time.sleep(3)
        self.driver.quit()


def main():
    if len(sys.argv) != 2:
        print("Takes exactly 1 argument: \"check\"")
        sys.exit(1)
    m = MetroTopup(metrocard_number, metrocard_password)
    m.open_metroinfo_page()
    print("Logging in")
    m.login()
    m.wait_for_main_page()
    print("Checking balance")
    current_balance = m.get_current_balance()

    if current_balance < 10:
        send_email(sender="nudnateiznek@gmail.com",
                   to="nudnateiznek@gmail.com",
                   person="Kenzie",
                   balance=current_balance)

    if sys.argv[1] == "check":
        sys.exit(0)

    print("Opening top up page")
    m.open_top_up_page()
    print("Topping up")
    m.top_up()
    print("Finishing")
    m.close()
    print("Done")

if __name__ == "__main__":
    main()
