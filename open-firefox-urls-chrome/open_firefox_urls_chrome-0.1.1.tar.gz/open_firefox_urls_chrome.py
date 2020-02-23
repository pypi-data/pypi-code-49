import os
import json
import lz4.block
import webbrowser
import psutil


# Get Firefox URLs largely taken from https://github.com/luismsgomes/get-firefox-urls

def get_firefox_urls(mozzila_adr=os.getenv('APPDATA') + "\\Mozilla"):
    parent_dir = check_recovery_exists(mozzila_adr)

    if parent_dir is None:
        print("Could not find recovery.jsonlz4 in %appdata%\\Mozilla")
        return

    filename = os.path.join(parent_dir, "recovery.jsonlz4")

    with open(filename, "rb") as f:
        # the first 8 bytes in recovery.jsonlz4 should contain
        # the string mozLz40
        assert f.read(8) == b"mozLz40\0"
        # after these 8 bytes the file is a lz4 stream
        compressed_data = f.read()

    data = lz4.block.decompress(compressed_data)
    root = json.loads(data.decode("utf-8"))

    for w, window in enumerate(root["windows"]):
        for t, tab in enumerate(window["tabs"]):
            yield w, t, tab["entries"][tab["index"]-1]["url"]


def check_recovery_exists(mozzila_adr):
    for parent_dir, dirs, files in os.walk(os.path.expanduser(mozzila_adr)):
        if "recovery.jsonlz4" in files:
            return parent_dir


def is_chrome_running():
    try:
        for process in psutil.process_iter():
            if "chrome" in process.name().lower():
                return True
    except psutil.AccessDenied:
        print("psutil AccessDenied. Browser not running")
    return False


def open_chrome(chrome_running):
    if not chrome_running:
        os.startfile("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")


def open_tabs_in_chrome(chrome_running):
    while not chrome_running:
        chrome_running = is_chrome_running()

    window = -1
    for w, t, url in get_firefox_urls():
        if window != w:
            window = w
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new(url)
        else:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab(url)


def main():
    chrome_running = is_chrome_running()
    open_chrome(chrome_running)
    open_tabs_in_chrome(chrome_running)