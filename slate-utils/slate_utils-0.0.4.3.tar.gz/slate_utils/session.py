from umdriver import UMDriver
from selenium.webdriver.chrome.options import Options
import requests


def get_session(hostname: str, username: str, password: str) -> requests.Session:
    """Returns an authenticated session for an internal user.

    Parameters
    ----------
    hostname : str
        The hostname of the slate environment to use, including protocol (eg, https://slateuniversity.net)
    username : str
        The user's username
    password : str
        The user's password
    """
    hostname = parse_hostname(hostname)
    opts = Options()
    opts.headless = True
    with UMDriver(options=opts) as d:
        d.login(username, password)
        d.get(f"{hostname}/manage")
        session = requests.session()
        for c in d.get_cookies():
            session.cookies.set(c["name"], c["value"])
    headers = {"Host": hostname.replace("https://", ""), "Origin": hostname}
    session.headers.update(headers)
    return session


def get_external_session(
    hostname: str, username: str, password: str
) -> requests.Session:
    """Returns an authenticated session for an external user.

    Parameters
    ----------
    hostname : str
        The hostname of the slate environment to use, including protocol (eg, https://slateuniversity.net)
    username : str
        The username to use for authentication
    password : str
        The password to use for authentication
    """
    hostname = parse_hostname(hostname)
    url = f"{hostname}/manage/login?cmd=external"
    session = requests.session()
    session.headers.update({"Origin": hostname})
    r1 = session.get(url)
    r2 = session.post(r1.url, data={"user": username, "password": password})
    r2.raise_for_status()
    return session


def steal_cookies(driver: UMDriver, session: requests.Session) -> requests.Session:
    """Steals the cookies from `driver` and adds them to `session`.

    Parameters
    ----------
    driver : webdriver
        Selenium webdriver instance where cookies will be taken from.
    session : requests.Session
        Session instance where cookies will be added.
    """
    for cookie in driver.get_cookies():
        session.cookies.set(cookie["name"], cookie["value"])
    return session


def parse_hostname(hostname: str) -> str:
    if hostname.lower().startswith('http'):
        return hostname.rstrip('/')
    return f"https://{hostname}".rstrip('/')