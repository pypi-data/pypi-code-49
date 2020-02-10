#auto facebook login.
from tkinter import *  #GUI
from selenium import webdriver

class AutoBrowser():
    def __init__(self,username,password,url="https://facebook.com",username_element="email",password_element="pass",login_button_element="u_0_b"):
        self.username = username
        self.password = password
        self.url = url
        self.username_element = username_element
        self.password_element = password_element
        self.login_button_element = login_button_element

    def login(self):
        browser=webdriver.Chrome()
        browser.get(self.url)
        login=browser.find_element_by_id(self.username_element)
        passw=browser.find_element_by_id(self.password_element)
        login.send_keys(self.username)
        passw.send_keys(self.password)
        login_button = browser.find_element_by_id(self.login_button_element)
        login_button.click()