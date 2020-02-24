#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# This file is part of Mentat system (https://mentat.cesnet.cz/).
#
# Copyright (C) since 2011 CESNET, z.s.p.o (http://www.ces.net/)
# Use of this source is governed by the MIT license, see LICENSE file.
#-------------------------------------------------------------------------------


"""
This file contains pluggable module for Hawat web interface containing features
related to `IDEA <https://idea.cesnet.cz/en/index>`__ event timeline based
visualisations.
"""


__author__ = "Jan Mach <jan.mach@cesnet.cz>"
__credits__ = "Pavel Kácha <pavel.kacha@cesnet.cz>, Andrea Kropáčová <andrea.kropacova@cesnet.cz>"


import datetime
import pytz

#
# Flask related modules.
#
import flask
from flask_babel import lazy_gettext

#
# Custom modules.
#
import mentat.stats.idea
import mentat.services.eventstorage
from mentat.const import tr_

import hawat.const
import hawat.events
import hawat.acl
from hawat.base import HTMLMixin, PsycopgMixin, AJAXMixin,\
    BaseSearchView, HawatBlueprint, URLParamsBuilder
from hawat.blueprints.timeline.forms import SimpleTimelineSearchForm


BLUEPRINT_NAME = 'timeline'
"""Name of the blueprint as module global constant."""


def _get_search_form(request_args = None):
    choices = hawat.events.get_event_form_choices()

    form = SimpleTimelineSearchForm(
        request_args,
        meta = {'csrf': False},
        choices_source_types    = choices['source_types'],
        choices_target_types    = choices['target_types'],
        choices_host_types      = choices['host_types'],
        choices_detectors       = choices['detectors'],
        choices_detector_types  = choices['detector_types'],
        choices_categories      = choices['categories'],
        choices_severities      = choices['severities'],
        choices_classes         = choices['classes'],
        choices_protocols       = choices['protocols'],
        choices_inspection_errs = choices['inspection_errs'],
    )

    # In case no time bounds were set adjust them manually.
    if request_args and not ('dt_from' in request_args or 'dt_to' in request_args or 'st_from' in request_args or 'st_to' in request_args):
        form.dt_from.process_data(hawat.forms.default_dt_with_delta())

    return form


class AbstractSearchView(PsycopgMixin, BaseSearchView):  # pylint: disable=locally-disabled,abstract-method
    """
    Base class for view responsible for searching `IDEA <https://idea.cesnet.cz/en/index>`__
    event database and presenting the results in timeline-based manner.
    """
    authentication = True

    authorization = [hawat.acl.PERMISSION_ANY]

    url_params_unsupported = ('page', 'limit', 'sortby')

    @classmethod
    def get_menu_title(cls, **kwargs):
        """*Implementation* of :py:func:`hawat.base.BaseView.get_menu_title`."""
        return lazy_gettext('Timeline')

    @classmethod
    def get_view_title(cls, **kwargs):
        """*Implementation* of :py:func:`hawat.base.BaseView.get_view_title`."""
        return lazy_gettext('Search event timeline')

    @staticmethod
    def get_search_form(request_args):
        """
        *Interface implementation* of :py:func:`hawat.base.SearchView.get_search_form`.
        """
        return _get_search_form(request_args)

    def do_before_search(self, form_data):  # pylint: disable=locally-disabled,no-self-use,unused-argument
        """
        *Interface implementation* of :py:func:`hawat.base.SearchView.do_before_search`.
        """
        form_data['groups'] = [item.name for item in form_data['groups']]

    def do_after_search(self, items):
        """
        *Interface implementation* of :py:func:`hawat.base.SearchView.do_after_search`.
        """
        self.logger.debug(
            "Calculating IDEA event timeline from %d records.",
            len(items)
        )
        if items:
            dt_from = self.response_context['form_data'].get('dt_from', None)
            if dt_from:
                dt_from = dt_from.astimezone(pytz.utc)
                dt_from = dt_from.replace(tzinfo = None)
            dt_to   = self.response_context['form_data'].get('dt_to', None)
            if dt_to:
                dt_to = dt_to.astimezone(pytz.utc)
                dt_to = dt_to.replace(tzinfo = None)

            if not dt_from and items:
                dt_from = self.get_db().search_column_with('detecttime')
            if not dt_to and items:
                dt_to = datetime.datetime.utcnow()

            self.response_context.update(
                statistics = mentat.stats.idea.evaluate_timeline_events(
                    items,
                    dt_from = dt_from,
                    dt_to = dt_to,
                    max_count = flask.current_app.config['HAWAT_CHART_TIMELINE_MAXSTEPS']
                )
            )
            self.response_context.pop('items', None)

    def do_before_response(self, **kwargs):
        """*Implementation* of :py:func:`hawat.base.RenderableView.do_before_response`."""
        self.response_context.update(
            quicksearch_list = self.get_quicksearch_by_time()
        )

    @staticmethod
    def get_qtype():
        """
        Get type of the event select query.
        """
        return mentat.services.eventstorage.QTYPE_SELECT_GHOST


class SearchView(HTMLMixin, AbstractSearchView):  # pylint: disable=locally-disabled,too-many-ancestors
    """
    View responsible for querying `IDEA <https://idea.cesnet.cz/en/index>`__
    event database and presenting the results in the form of HTML page.
    """
    methods = ['GET']

    @classmethod
    def get_breadcrumbs_menu(cls):
        """
        *Interface implementation* of :py:func:`hawat.base.SearchView.get_breadcrumbs_menu`.
        """
        breadcrumbs_menu = hawat.menu.Menu()
        breadcrumbs_menu.add_entry(
            'endpoint',
            'home',
            endpoint = flask.current_app.config['HAWAT_ENDPOINT_HOME']
        )
        breadcrumbs_menu.add_entry(
            'endpoint',
            'search',
            endpoint = '{}.search'.format(cls.module_name)
        )
        return breadcrumbs_menu


class APISearchView(AJAXMixin, AbstractSearchView):  # pylint: disable=locally-disabled,too-many-ancestors
    """
    View responsible for querying `IDEA <https://idea.cesnet.cz/en/index>`__
    event database and presenting the results in the form of JSON document.
    """
    methods = ['GET','POST']

    @classmethod
    def get_view_name(cls):
        """*Implementation* of :py:func:`hawat.base.BaseView.get_view_name`."""
        return 'apisearch'


#-------------------------------------------------------------------------------


class TimelineBlueprint(HawatBlueprint):
    """
    Hawat pluggable module - IDEA event timelines.
    """

    @classmethod
    def get_module_title(cls):
        """*Implementation* of :py:func:`hawat.base.HawatBlueprint.get_module_title`."""
        return lazy_gettext('IDEA event timelines pluggable module')

    def register_app(self, app):
        """
        *Callback method*. Will be called from :py:func:`hawat.base.HawatApp.register_blueprint`
        method and can be used to customize the Flask application object. Possible
        use cases:

        * application menu customization

        :param hawat.base.HawatApp app: Flask application to be customize.
        """
        app.menu_main.add_entry(
            'view',
            'dashboards.{}'.format(BLUEPRINT_NAME),
            position = 30,
            view = SearchView,
            resptitle = True
        )

        # Register context actions provided by this module.
        app.set_csag(
            hawat.const.HAWAT_CSAG_ADDRESS,
            tr_('Search for source <strong>%(name)s</strong> on IDEA event timeline'),
            SearchView,
            URLParamsBuilder({'submit': tr_('Search')}).add_rule('source_addrs', True).add_kwrule('dt_from', False, True).add_kwrule('dt_to', False, True)
        )

#-------------------------------------------------------------------------------


def get_blueprint():
    """
    Mandatory interface and factory function. This function must return a valid
    instance of :py:class:`hawat.base.HawatBlueprint` or :py:class:`flask.Blueprint`.
    """

    hbp = TimelineBlueprint(
        BLUEPRINT_NAME,
        __name__,
        template_folder = 'templates'
    )

    hbp.register_view_class(SearchView,    '/{}/search'.format(BLUEPRINT_NAME))
    hbp.register_view_class(APISearchView, '/api/{}/search'.format(BLUEPRINT_NAME))

    return hbp
