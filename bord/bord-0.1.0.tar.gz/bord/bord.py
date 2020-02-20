import asyncio

from pyppeteer import launch

from bord.config import Config


class Bord:
    def __init__(self, config: Config):
        self.config = config
        self._tab_index = 0

    async def start(self):
        self.browser = await launch(
            headless=False, dumpio=True, logLevel="INFO", autoclose=False, args=['--kiosk', '--disable-infobars'],
        )
        await self.init_tabs()
        await self.set_tab_urls()
        while True:
            await self.rotate()


    async def init_tabs(self):
        self.tabs = await self.browser.pages()

        while len(self.tabs) < len(self.config.urls):
            self.tabs.append(await self.browser.newPage())

    async def set_tab_urls(self):
        for tab, url in zip(self.tabs, self.config.urls):
            print("Set tab:", tab, " to url:", url)
            await tab.setViewport(dict(width=self.config.monitor.width, height=self.config.monitor.height))
            await tab.goto(url, timeout=0)


    async def rotate(self):
        tab = self.tabs[self._tab_index]
        await asyncio.sleep(self.config.interval)
        print(f"Switching to tab[{self._tab_index}] = {tab}")
        await self.tabs[self._tab_index].bringToFront()
        self._tab_index += 1
        if self._tab_index == len(self.tabs):
            self._tab_index = 0
