from os.path import exists

from requests import get, post


def get_url(url, ref, resource):
    return f'{url}?ref={ref}&resource={resource}'


def download(output_file, url):
    if not exists(output_file):
        with open(output_file, 'wb') as f:
            f.write(get(url).content)


def upload(input_file, url):
    if exists(input_file):
        with open(input_file, "rb") as in_file:
            content = in_file.read()
            print(url)
            post(url, content)


upload('/Users/magnus/git/scripts/vang/artifactory/slask.txt', get_url('http://localhost:7000/', 'develop', 'slask.txt'))
