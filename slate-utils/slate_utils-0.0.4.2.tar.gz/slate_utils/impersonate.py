from contextlib import contextmanager
from urllib.parse import urlencode

from loguru import logger

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class UserDoesNotExistException(Exception):
    pass


class NotImpersonatedSessionException(Exception):
    pass


class Impersonator:
    """Class intended to spawn impersonated driver instances.
    """

    def __init__(self, driver, base_url):
        self.d = driver
        self.base_url = base_url

    def _impersonate(self, user):
        """Impersonate the giver user account where `user` is a guid.

        Parameters
        ----------
        user : str
            The guid of the user account to impersonate.

        """
        d = self.d
        qs = {"id": user, "view": "active"}
        url = self.base_url + "/manage/database/security/user?" + urlencode(qs)
        d.get(url)
        if d.title == "503 Error":
            raise UserDoesNotExistException(f"{user}: User does not exist.")
        wait = WebDriverWait(d, 10)
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        d.find_element_by_link_text("Impersonate").click()
        alert = WebDriverWait(d, 10).until(EC.alert_is_present())
        alert.accept()
        return self.d

    def _unimpersonate(self):
        """Unimpersonate the current user.

        """
        try:
            d.find_element_by_link_text("Exit Impersonation")
        except NoSuchElementException:
            raise NotImpersonatedSessionException
        redirect = self.base_url + "/manage"
        qs = {"r": redirect}
        url = self.base_url + "/manage/logout?" + urlencode(qs)
        self.d.get(url)
        return self.d

    @contextmanager
    def impersonate(self, user):
        """Context manager that will impersonate the given `user`, returning
        a driver instance for the impersonated session.

        After the context manager is closed, the impersonated session
        will be terminated.

        Parameters
        ----------
        user : str
            The guid of the user account to impersonate.

        """
        logger.debug(f"Impersonating {user}...")
        self._impersonate(user)
        try:
            yield self.d
        finally:
            self._unimpersonate()
            logger.debug(f"Unimpersonating {user}...")
