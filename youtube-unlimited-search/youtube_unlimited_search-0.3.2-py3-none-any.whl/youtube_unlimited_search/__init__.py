import requests
from bs4 import BeautifulSoup
import urllib.parse


class YoutubeUnlimitedSearch:

    def __init__(self, search_terms: str, max_results=None):
        self.search_terms = search_terms
        self.max_results = max_results
        self.videos = self.search()

    def search(self):
        encoded_search = urllib.parse.quote(self.search_terms)
        BASE_URL = "https://youtube.com"
        url = f"{BASE_URL}/results?search_query={encoded_search}&pbj=1"
        response = BeautifulSoup(requests.get(url).text, "html.parser")
        results = self.parse_html(response)
        if self.max_results is not None and len(results) > self.max_results:
            return results[:self.max_results]
        return results

    def parse_html(self, soup):
        results = []
        for tile in soup.select(".yt-uix-tile"):
            videoLink = tile.select('.yt-uix-tile-link')[0]
            if videoLink["href"].startswith("/watch?v="):
                link = videoLink["href"]
                extraData = tile.select('.yt-lockup-meta-info li')
                thumb = tile.find('img')
                if 'http' in thumb.attrs['src']:
                    thumb = thumb.attrs['src']
                elif thumb.attrs['data-thumb'] is not None:
                    thumb = thumb.attrs['data-thumb']

                views = ""
                published = ""
                duration = ""
                channel = ""
                description = ""
                try:
                    views = extraData[1].getText()
                    published = extraData[0].getText()
                except:
                    print("Can't catch views and published time")
                try:
                    duration = tile.select('.video-time')[0].getText()
                except:
                    print("can't catch duration")
                try:
                    channel = tile.select('.yt-lockup-byline .spf-link')[0].getText()
                except:
                    print("can't catch channel")
                try:
                    description = tile.find('div', {'class': 'yt-lockup-description'}).getText()
                except:
                    print("can't catch channel")
                try:
                    video_info = {
                        "title": videoLink["title"],
                        "thumbnail": thumb,
                        "description": description,
                        "link": link,
                        "id": link[videoLink["href"].index("=") + 1:],
                        "views": views,
                        "published": published,
                        "duration": duration,
                        "channel": channel
                    }
                    results.append(video_info)
                except:
                    print("skip this")
        return results

    def get(self):
        return self.videos
