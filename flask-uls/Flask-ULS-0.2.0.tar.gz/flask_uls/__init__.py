#  Copyright (C) 2020  Kunal Mehta <legoktm@member.fsf.org>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import os
import re

from flask import Blueprint, request, current_app, send_from_directory
from flask import _app_ctx_stack  # type: ignore[attr-defined]


class ULS:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('ULS_DEFAULT_LANGUAGE', 'en')
        app.config.setdefault('ULS_ENABLED_LANGUAGES', ['en'])
        app.register_blueprint(self.blueprint())

    def blueprint(self) -> Blueprint:
        bp = Blueprint('uls', __name__, template_folder='templates')
        static_path = os.path.join(os.path.dirname(__file__), 'static')

        @bp.route('/uls-static/<path:fn>')
        def uls_static(fn: str):
            # Note: in sdist and bdist_wheel, we only bundle
            # the submodule parts that are actually needed (CSS/images/JS)
            return send_from_directory(static_path, fn)

        return bp

    def _validate_language(self, lang: str):
        if not re.match(r'^[A-z\-]{2,10}$', lang):
            # TODO: this can be improved
            raise ValueError('Language "{}" appears to be invalid'
                             .format(lang))

    def _determine_language(self) -> str:
        """
        determine the language by looking at
        * uselang= parameter
        * language cookie
        * config default

        TODO: Accept header
        """
        if 'uselang' in request.args:
            lang = request.args['uselang']
            self._validate_language(lang)
            return lang
        elif 'language' in request.cookies:
            lang = request.cookies['language']
            self._validate_language(lang)
            return lang

        # Assume this is already a valid language code
        return current_app.config['ULS_DEFAULT_LANGUAGE']

    @property
    def language(self) -> str:
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'language'):
                ctx.language = self._determine_language()
            return ctx.language
        return 'en'  # XXX: hardcoded fallback just in case?

    @language.setter
    def language(self, lang: str):
        # TODO: validation?
        ctx = _app_ctx_stack.top
        if ctx is not None:
            ctx.language = lang
