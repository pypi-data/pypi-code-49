
#!/usr/bin/python3

import sys
import requests
import json
import re
import time
from packaging import version


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


noLineWarning = 0

get_inside_app_resource_base_url = "https://cdn.zalopay.com.vn/cpscdn/app/getinsideappresource"


def build_url(version, platform, screentype):
    return f"{get_inside_app_resource_base_url}?appversion={version}&platformcode={platform}&dscreentype={screentype}"


def load_data(url):
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        if data["returncode"] != 1:
            raise ValueError("Server response error code: " +
                             str(data["returncode"]))
        return data
    except Exception as e:
        print(f"\n{bcolors.FAIL}error{bcolors.ENDC} Load data failed:", e)
        sys.exit()


def get_timestamps(filename):
    datematch = re.search('\d{8}', filename)
    if(datematch == None):
        print(
            f"\n{bcolors.FAIL}error{bcolors.ENDC} The filename invalid in url: {url}")
        sys.exit()
    strdate = datematch.group()
    timestamp = time.mktime(time.strptime(strdate, '%Y%m%d'))
    return timestamp


def get_resource_name(input):
    name = re.search(r'[\d,.]+\d{8}[_,.]*\d*.zip$', input)
    if name:
        return name.group()
    return None


def compare(resource1, resource2, ver1, ver2, platform):
    appid = resource1["appid"]

    imageurl1 = resource1["imageurl"] if "imageurl" in resource1 else ""
    jsurl1 = resource1["jsurl"] if "jsurl" in resource1 else ""

    imageurl2 = resource2["imageurl"] if "imageurl" in resource2 else ""
    jsurl2 = resource2["jsurl"] if "jsurl" in resource2 else ""

    image1 = get_resource_name(imageurl1)
    js1 = get_resource_name(jsurl1)
    image2 = get_resource_name(imageurl2)
    js2 = get_resource_name(jsurl2)

    if not image1 and not js1 and not image2 and js2:
        return (True, 'Skip')

    if image1 != js1:
        return (False, f'{bcolors.WARNING}resource app {appid} do not match at version {ver1} in platform {platform}\n{bcolors.ENDC}')
    if image2 != js2:
        return (False, f'{bcolors.WARNING}resource app {appid} do not match at version {ver2} in platform {platform}\n{bcolors.ENDC}')
    if image1 != image2:
        time1 = get_timestamps(image1)
        time2 = get_timestamps(image2)
        if time1 > time2:
            messages = [
               f'{bcolors.FAIL}Resource app {appid} is an old version: {bcolors.ENDC}',
               f'{bcolors.HEADER}at version {ver1}: {bcolors.BOLD}{image1} {bcolors.ENDC}',
               f'{bcolors.HEADER}at version {ver2}: {bcolors.BOLD}{image2} {bcolors.ENDC}',
               f'{bcolors.HEADER}in platform {platform}\n{bcolors.ENDC}',
            ]
            return (False, "\n".join(messages))
        else:
            messages = [
               f'{bcolors.WARNING}Warning{bcolors.ENDC} resource app {appid} is updated:',
               f'at version {ver1}: {bcolors.BOLD}{image1} {bcolors.ENDC}',
               f'at version {ver2}: {bcolors.BOLD}{image2} {bcolors.ENDC}',
               f'in platform {platform}\n{bcolors.ENDC}',
            ]
            return (False, "\n".join(messages))
    return (True, '')

def diff(ver1, ver2, platform, screentype):
    url1 = build_url(ver1, platform, screentype)
    url2 = build_url(ver2, platform, screentype)
    data1 = load_data(url1)
    data2 = load_data(url2)

    resourceList1 = data1["resourcelist"]
    resourceList2 = data2["resourcelist"]
    appids = []
    for resource1 in resourceList1:
        for resource2 in resourceList2:
            if resource1["appid"] == resource2["appid"]:
                result, message = compare(resource1, resource2, ver1, ver2, platform)
                if not result:
                    global noLineWarning
                    noLineWarning = noLineWarning + 1
                    print(message)
                break
    return appids

def input_version(message):
    while True:
        version = input(message)
        match = re.match(r"^\d+\.\d+(\.?\d+)?$", version)
        if match:
            return version
        print(f"{bcolors.FAIL}Version input is invalid (please input with format: 4.22.1 or 4.22) {bcolors.ENDC}")

def main():
    global noLineWarning
    start_time = time.time()
    old_version = input_version(f"{bcolors.BOLD}Enter the old version: {bcolors.ENDC}")
    new_version = input_version(f"{bcolors.BOLD}Enter the new version: {bcolors.ENDC}")
    if version.parse(old_version) > version.parse(new_version): 
        print(f"{bcolors.FAIL}The old version must be smaller than the new version {bcolors.ENDC}")
        sys.exit()

    # Android compare
    diff(old_version, new_version, "android", "hdpi")
    # iOS compare
    diff(old_version, new_version, "ios", "iphone1x")
    if(noLineWarning == 0):
        print(f"{bcolors.OKGREEN}success{bcolors.ENDC} Don't have any warnings.")

    print(f"\n✨ Done in {round(time.time() - start_time, 2)}s.\n")
    sys.exit()

if __name__ == '__main__':
    main() 