import json

import curlify


def export_curl(response):
    try:
        with open('curl.txt', 'w+') as file:
            text = curlify.to_curl(response.request)
            text = text.replace(
                " -H 'Accept: */*'", ''
            ).replace(
                " -H 'Accept-Encoding: gzip, deflate'", ''
            ).replace(
                " -H 'Connection: keep-alive'", ''
            ).replace(
                " -H 'Content-Length: 267'", ''
            ).replace(
                " -H 'User-Agent: python-requests/2.19.1'", ''
            ).replace(
                "GPj7I9FxcybyHCEeZ50UQ84LMmjhTOU0MzlIIhjh", '<client_id>'
            ).replace(
                "RrAcveMhXdQC7rPMTqqzuLbe05zRtEVIM6HmV3U8DxlXTnJW3QPDQBZAymAh6TBmV9O1ie9U21xxrfhGVbBL5CuPQm5YaSxyImxcJIIBKOkAg28dlQZKWsnR2Mgb5MAb",
                '<client_secret>'
            ).replace(
                "admin%40localhost.com", '<email_address>'
            ).replace(
                "greatness2011", '<your_password>'
            ).replace(
                "http://localhost:8000", "https://app.linkfusions.com"
            ).replace('dUgTK8subOCjS4aNqfSmhG7vR4Kha5', '<access_token>')
            file.write(text)
    except UnicodeDecodeError as e:
        print('Could not convert this request to curl')

    with open('result.json', 'w+') as file:
        text = json.dumps(response.json(), ensure_ascii=False, indent=4)
        file.write(text)
