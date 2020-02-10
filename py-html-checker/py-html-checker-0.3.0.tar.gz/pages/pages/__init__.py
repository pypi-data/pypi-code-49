# -*- coding: utf-8 -*-
"""
The project pages map for Py Html Checker pages
"""
from optimus.pages.views.base import PageViewBase
from optimus.conf.registry import settings

from .index import Index
from .page import StyleguidePage, ExportAudit, ExportSummary, ExportReport


# Available pages
BASIC_PAGES = [
    ExportAudit(),
    ExportSummary(),
    ExportReport(),
    StyleguidePage(),
]

# Enabled pages to build
PAGES = BASIC_PAGES + [
    Index(destination="index.html", pages=BASIC_PAGES),
]
