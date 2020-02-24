#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Craigslist search.

Objects that search for housing on Craigslist and scrape the data.
"""
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
from random import uniform
from re import findall
from requests import get
from requests.exceptions import RequestException
from sys import exit
from time import sleep


class CLSearch:
    """Search and scrape Craigslist.

    A CLSearch object represents a search on Craigslist.com. Upon
    initialization, the first page of search results is requested from the CL
    website. If the search is empty or invalid, user is warned. If valid, the
    search is executed, all pages of search results are requested and scraped,
    and the scraped data is stored in the `data` attribute as a DataFrame.

    In the scraped `data`, each record represents an ad. The "bundle
    duplicates" option is selected when executing the search.

    Arguments:
        `geo`: str
            From which geographical area do you want data? See a list of
            available geographies and their Craigslist aliases here:
            <link>
        `query`: str, default ""
            Words for text search. Put exact phrases in quotes.
        `deep`: bool, default False
            Navigate to each individual ad and scrape the following additional
            variables: Address, bathroom count, attributes (pet-friendly, etc),
            post ID.
        `body`: bool, default False
            Can only be True if `deep` is True. Scrape the body text of each
            ad, if available. Note: This will significantly increase the data's
            memory footprint.

    Example:
        c1 = CLSearch(geo="sfbay", query="'no section 8'")
        print(c1.data)
    """

    def __init__(self, geo, query="", deep=False, body=False):
        """Start the search.

        Navigates to the first page of search results.
        """
        self.geo = geo
        self.board = "apa"
        self.deep = deep
        self.body = body
        self.url = None
        self.next_page_url = self.__build_url(
            f"/search/{self.board}?query={query}&bundleDuplicates=1")
        self.reqc = None
        self.soup = None
        self.data = []

        self.__scrape_all_pages()

    # scraping methods

    def __scrape_all_pages(self):
        """Drive the scraper.

        Navigates to and scrapes all pages of search results.
        """
        n = 0
        while self.next_page_url:
            self.__goto_next_page()
            self.__scrape_page()
            n += 1
        print(f"Finished scraping {n} pages of results.")
        self.__clean_data()

    def __scrape_page(self):
        """Scrape a page of search results.

        Stores all scraped data in a DataFrame and appends it to the `data`
        list attribute. Also navigates to and scrapes data from every ad on a
        given results page, if told.
        """
        # Some ads have no BR info. Some have no SQFT info. Some have neither.
        # So some info must be extracted from the text of the node it might
        # appear in.
        # This regex gets all non-whitespace between {1} and {2}.
        bw_rgx = r"(?<={0})\S+(?={1})"
        # If search results are few, CL shows ads from nearby geographies. We
        # want to scrape only the ads associated w/ the present search. Get a
        # count of them.
        try:
            n_ads = int(self.soup.select(".rangeTo")[0].text)
        except IndexError:
            raise Exception("No results for that search.") from None

        # scrape data available on current results page
        df_pg = pd.DataFrame({
            "date": self.__get_info_from(".result-date"),
            "title": self.__get_info_from(".hdrlnk"),
            "link": self.__get_info_from(".hdrlnk", attr="href"),
            "rent": self.__get_info_from(".result-meta .result-price"),
            "beds": self.__get_info_from(".result-meta",
                                         pat=bw_rgx.format(" ", "br ")),
            "sqft": self.__get_info_from(".result-meta",
                                         pat=bw_rgx.format(" ", "ft2 ")),
            "hood": self.__get_info_from(".result-meta",
                                         pat=bw_rgx.format(r"\(", r"\)"))
            })[:n_ads]

        if self.deep:
            # attrs: misc attributes listed on the side of an ad
            cols_ads = ["link", "addr", "baths", "attrs", "post_id",
                        "datetime_scr"]
            if self.body:
                cols_ads.append("body")
            data_ads = []
            # navigate to & scrape each ad on current results page
            for link in df_pg["link"]:
                self.url = link
                self.__navigate()
                dta_ad = [
                    self.url,
                    self.__get_info_from("div.mapaddress")[0],
                    self.__get_info_from(".shared-line-bubble:nth-child(1)",
                                         pat=bw_rgx.format("/ ", "Ba"))[0],
                    self.__get_info_from(".attrgroup:nth-child(3) span")[0],
                    self.__get_info_from(".postinginfo:nth-child(1)",
                                         pat=r"\d+")[0],
                    self.__get_datetime()
                    ]
                if self.body:
                    dta_ad.append(
                        self.__get_info_from("#postingbody")[0]
                        )
                data_ads.append(dta_ad)
            df_ads = pd.DataFrame(data_ads, columns=cols_ads)
            df_pg = pd.merge(df_pg, df_ads, how="left", on="link")
        else:
            df_pg["datetime_scr"] = self.__get_datetime()
        # append page"s DataFrame to instance"s `data` list
        self.data.append(df_pg)

    def __find_next_page(self):
        """Find link to next results page.

        Scrapes URL for the next page of search results from the "Next" button,
        & sets the `next_page_url` attribute to that.
        """
        try:
            sfx = self.__get_info_from(
                # This is prob the most fragile CSS selector of the bunch.
                # Expect it to change frequently.
                ("div.search-legend:nth-child(3) > div:nth-child(3)"
                 "> span:nth-child(2) > a:nth-child(6)"),
                attr="href"
                )[0]
        except KeyError or IndexError:
            sfx = ""
        finally:
            self.next_page_url = self.__build_url(sfx) if sfx else None

    def __get_info_from(self, css, attr=None, pat=".*"):
        """Scrape HTML nodes.

        Scrapes data from nodes identified by given CSS selector, HTML
        attribute, and/or regex pattern.

        Return value:
            A list, where each element contains info from a node.
        """
        nodes = self.soup.select(css)
        info = [n.text if attr is None else n[attr] for n in nodes]
        if pat != ".*":
            info = ["".join(findall(pat, i)) for i in info]
        info = [None if i == "" else i for i in info]
        return info or [None]

    # navigation methods

    def __goto_next_page(self):
        """Go to next results page."""
        self.url = self.next_page_url
        self.__navigate()

    def __navigate(self):
        """Navigate the scraper.

        Gets content from webpage at `url` attribute. Waits a few seconds b/w
        requests.
        """
        try:
            r = get(self.url)
        except RequestException as e:
            exit(f"Error when requesting {self.url} : {str(e)}")
        else:
            print(f"Parsing {self.url}\n")
            self.reqc = r.content
            self.soup = BeautifulSoup(self.reqc, "html.parser")
            self.__find_next_page()
            sleep(1 + uniform(1, 5))  # be polite

    def __build_url(self, suffix):
        """Build URL for search results from template."""
        return f"https://{self.geo}.craigslist.org{suffix}"

    # data methods

    def __clean_data(self):
        """Combine and clean scraped data.

        `data` attribute is a list of DataFrames, one for each page of search
        results. Concatenate them into one big DF. Convert certain variables to
        numeric.
        """
        self.data = pd.concat(self.data)
        self.data["rent"].replace(regex=r"\$", value="", inplace=True)
        num = {"rent", "beds", "sqft", "baths"}
        num = list(
            num.intersection(self.data.columns)
            )
        self.data[num] = self.data[num].apply(pd.to_numeric, errors="coerce")

    @staticmethod
    def __get_datetime():
        return datetime.now().strftime("%Y-%m-%d %H:%M")


if __name__ == "__main__":
    pass
