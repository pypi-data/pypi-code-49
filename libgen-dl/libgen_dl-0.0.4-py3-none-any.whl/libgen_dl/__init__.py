import argparse
import requests
from bs4 import BeautifulSoup
import lxml
import urllib


def a_has_title(tag):
    return tag.has_attr("title")


def main():
    parser = argparse.ArgumentParser(description="download from libgen")

    parser.add_argument("title", metavar="T", type=str, help="information on book")
    parser.add_argument("--ext", help="specify what file extensions to search for")

    args = parser.parse_args()

    data = {"req": args.title, "res": 25}
    r = requests.get("https://libgen.is/search.php", params=data)

    soup = BeautifulSoup(r.text, "lxml")
    table = soup.find("table", "c")

    options = []
    for tr in table.find_all("tr")[1:]:
        metadata = tr.find_all("td")
        if args.ext and args.ext != metadata[8].string:
            continue
        options.append(
            {
                "id": metadata[0].string,
                "author": metadata[1].text,
                "title": metadata[2].find(a_has_title).contents[0].string,
                "publisher": metadata[3].string,
                "year": metadata[4].string,
                "pages": metadata[5].text,
                "language": metadata[6].string,
                "size": metadata[7].string,
                "extension": metadata[8].string,
                "mirror": metadata[9].find("a")["href"],
            }
        )

    for idx, opt in enumerate(options):
        print(
            "{:3}: {} by {} ({}) [{}], {} pages".format(
                idx,
                opt["title"],
                opt["author"],
                opt["year"],
                opt["extension"],
                opt["pages"],
            )
        )
    print("Which book do you wish to download? (enter a number) ", end="")
    choice = int(input())

    mirror = options[choice]["mirror"]
    r = requests.get(mirror)
    base = "http://" + urllib.parse.urlparse(mirror).netloc
    dl_url = base + BeautifulSoup(r.text, "lxml").find("a")["href"]
    print(dl_url)
    file_name = (
        options[choice]["title"].strip() + "." + options[choice]["extension"].strip()
    )
    urllib.request.urlretrieve(dl_url, file_name)
