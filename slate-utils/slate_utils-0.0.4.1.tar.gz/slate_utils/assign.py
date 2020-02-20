from urllib.parse import urlencode

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from umdriver import UMDriver

from slate_utils.wait import wait_method


class Assigner:

    def __init__(self, driver: UMDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url

    @wait_method(timeout=5)
    def assign(self, application: str, bin_: str = None, reader: str = None):
        """Assign an application to a given bin and/or reader.
        
        Parameters
        ----------
        application : str (guid)
            An application guid
        bin_ : str, optional
            The bin the application will be assigned to (the default is None, 
            which will skip setting the bin assignment)
        reader : str (guid), optional
            The user guid of the reader that will be assigned (the default is 
            None, which will omit assigning a reader)
        
        """
        application = application.lower()
        qs = {'tab': 'Application/Workflows',
              'id': application}
        uri = '/manage/lookup/record'
        url = f'{self.base_url}{uri}?{urlencode(qs)}'
        self.driver.get(url)
        # find the edit bin link for the default workflow via href xpath
        xpath_href = f'{uri}?cmd=edit_bin&id={application}&workflow='
        xpath = f'//a[@data-href="{xpath_href}"]'
        wait = WebDriverWait(self.driver, 10)
        el = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        el.click()
        # modal is now open, begin filling fields.
        if bin_:
            bin_loc = (By.ID, 'edit_bin')
            bin_el = wait.until(EC.visibility_of_element_located(bin_loc))
            bin_select = Select(bin_el)
            bin_select.select_by_visible_text(bin_)
        if reader:
            reader_loc = (By.ID, 'queue_user')
            reader_el = wait.until(EC.presence_of_element_located(reader_loc))
            # input is hidden, so must be filled by javascript
            js = "el = arguments[0]; el.value = arguments[1];"
            self.driver.execute_script(js, reader_el, reader)
        # save the modal
        self.driver.find_element_by_xpath('//button[text()="Save"]').click()
