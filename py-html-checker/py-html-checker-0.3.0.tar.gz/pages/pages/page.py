# -*- coding: utf-8 -*-
import datetime
import io
import json
import os

from optimus.pages.views.base import PageViewBase
from optimus.conf.registry import settings

from py_css_styleguide.model import Manifest


class BasicPage(PageViewBase):
    """
    Basic page
    """
    title = "Basic page"
    template_name = "page.html"
    destination = "page.html"
    css_bundle = "main_css" # Selected value from settings.BUNDLES

    def get_context(self):
        super().get_context()

        self.context.update({
            "DEFAULT_LANGUAGE": settings.LANGUAGE_CODE,
            "LANGUAGES": settings.LANGUAGES,
            "CSS_BUNDLE": self.css_bundle,
        })

        return self.context


class StyleguideMixin:
    """
    A mixin which include method to get styleguide manifest
    """
    def get_styleguide(self):
        manifest = Manifest()
        manifest_filepath = os.path.join(settings.SOURCES_DIR, "css", "styleguide_manifest.css")
        with io.open(manifest_filepath, "r") as fp:
            manifest.load(fp)

        return manifest


class StyleguidePage(StyleguideMixin, BasicPage):
    """
    Styleguide page
    """
    title = "Styleguide"
    template_name = "styleguide/index.html"
    destination = "styleguide.html"
    css_bundle = "styleguide_css" # Selected value from settings.BUNDLES

    def get_context(self):
        super().get_context()

        self.context.update({
            "STYLEGUIDE": self.get_styleguide(),
        })

        return self.context


class ExportBase(BasicPage):
    """
    Exported document base is wired to load JSON document.
    """
    export_name = None

    def get_export(self):
        exports_path = os.path.join(settings.SOURCES_DIR, "exports")
        export_filepath = os.path.join(exports_path, self.export_name)

        # TODO: Document object should be modified to turn datetime string to
        # datetime object like on "metas.created" attribute.
        with io.open(export_filepath, "r") as fp:
            document = json.load(fp)

        return document

    def get_context(self):
        super().get_context()

        # NOTE: Temporary dummy source code until reports contain it
        sample_path = os.path.join(settings.SOURCES_DIR, "exports", "source.html")
        with io.open(sample_path, "r") as fp:
            sample_source = fp.read()

        self.context.update({
            "export": self.get_export(),
            "sample_source": sample_source,
        })

        return self.context


class ExportAudit(ExportBase):
    """
    Exported Audit document prototype
    """
    title = "Audit"
    template_name = "exports/audit.html"
    destination = "audit.html"
    css_bundle = "main_css"
    export_name = "audit.json"


class ExportSummary(ExportBase):
    """
    Exported Summary document prototype
    """
    title = "Summary"
    template_name = "exports/summary.html"
    destination = "summary.html"
    css_bundle = "main_css"
    export_name = "summary.json"


class ExportReport(ExportBase):
    """
    Exported Report document prototype
    """
    title = "Report"
    template_name = "exports/report.html"
    destination = "report.html"
    css_bundle = "main_css"
    export_name = "report.json"
