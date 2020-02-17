from urllib.request import urlopen, Request
from urllib import error
import ssl
from dns import resolver
import dns.rdatatype


def main():
    # url = "https://ppg.guavaandnobi.tw/softwares/2y10gHHP2voOcC8wJKPivS05NuQXeNxxMqkSGSFwv4TSjlW4XIu0yMq"
    #
    # html = view_http_content(url)
    # if html is None:
    #     print("404")
    # else:
    #     print(html.decode('utf-8'))
    # with open("./test.msi", "wb") as f:
    #     f.write(html)
    # flag, ans = dns_query('ppg.guavaandnobi.tw')
    # print(check_ip_or_hostname("ppg.guavaandnobi.tw"))
    # flag, msg = check_software_version()
    # if flag and msg is not None:
    #     print(msg)
    # else:
    #     print(msg)
    return


def view_http_content(url: str):
    if not isinstance(url, str):
        return None
    context = ssl._create_unverified_context()

    try:
        request = Request(url)
        response = urlopen(request, context=context)
        result = response.read()
        response.close()
        return result
    except (error.HTTPError, error.URLError):
        return None


def dns_query(hostname: str, dns_server=None, limit=1):
    if not isinstance(hostname, str):
        return False, ()
    try:
        res = resolver.Resolver()
        res.nameservers = ['8.8.8.8', '140.124.13.1'] if dns_server is None or not isinstance(dns_server, str) \
            else ['8.8.8.8', '140.124.13.1', dns_server]
        answers = res.query(hostname)

        if len(answers) >= 1 and limit == 1:
            return True, answers[0]
        else:
            return True, answers
    except (resolver.NoNameservers, resolver.NXDOMAIN):
        return False, ()


def check_ip_or_hostname(ip_or_host: str):
    str_split = ip_or_host.split('.')
    if len(str_split) == 4:
        for i in str_split:
            try:
                int(i)
            except ValueError:
                return "IS_HOST"
        return "IS_IP"
    else:
        return "IS_HOST"


if __name__ == '__main__':
    main()
