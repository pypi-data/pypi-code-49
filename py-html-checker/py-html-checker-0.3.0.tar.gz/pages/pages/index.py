# -*- coding: utf-8 -*-
from optimus.pages.views.base import PageViewBase
from optimus.conf.registry import settings


class Index(PageViewBase):
    """
    Default index page
    """
    title = "Index"
    template_name = "index.html"
    destination = "index.html"
    pages = []

    def get_context(self):
        super().get_context()

        pages_map = []
        for page in self.pages:
            pages_map.append({
                "title": page.title,
                "destination": page.destination,
            })

        self.context.update({
            "DEFAULT_LANGUAGE": settings.LANGUAGE_CODE,
            "LANGUAGES": settings.LANGUAGES,
            "pages": pages_map,
        })

        return self.context
