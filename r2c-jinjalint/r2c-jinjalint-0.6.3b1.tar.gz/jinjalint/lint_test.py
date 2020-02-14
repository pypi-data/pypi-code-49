import textwrap

from jinjalint import check
from jinjalint import issue
from jinjalint import lint


def get_file(html):
    config = {}

    return lint.parse_source((textwrap.dedent(html), config))


def test_check_csrf_protection_missing_token():
    html = """
    <html>
        <body>
            <form method="post">
                <input name="foo" value="bar"/>
            </form>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_csrf_protection(jl_file, {})
    expected = [
        issue.Issue(
            issue.IssueLocation(
                file_path=None,
                line=3,
                column=8
            ),
            check.FORM_MISSING_CSRF_ISSUE_MESSAGE,
            check.FORM_MISSING_CSRF_ISSUE_CODE
        )
    ]

    assert result == expected


def test_check_csrf_protection_input_field_present():
    html = """
    <html>
        <body>
            <form method="post">
                <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
            </form>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_csrf_protection(jl_file, {})
    expected = []

    assert result == expected


def test_check_csrf_protection_flask_form_present():
    html = """
    <html>
        <body>
            <form method="post">
                {{ form.csrf_token }}
            </form>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_csrf_protection(jl_file, {})
    expected = []

    assert result == expected


def test_check_anchor_target_blank_missing_rel():
    html = """
    <html>
        <body>
            <a href="https://example.com" target="_blank">Test</a>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = set(
        check.check_anchor_target_blank_noopener(jl_file, {})
        + check.check_anchor_target_blank_noreferrer(jl_file, {})
    )
    expected = {
        issue.Issue(
            issue.IssueLocation(
                file_path=None,
                line=3,
                column=8
            ),
            check.ANCHOR_TARGET_BLANK_NOOPENER_ISSUE_MESSAGE,
            check.ANCHOR_TARGET_BLANK_NOOPENER_ISSUE_CODE
        ),
        issue.Issue(
            issue.IssueLocation(
                file_path=None,
                line=3,
                column=8
            ),
            check.ANCHOR_TARGET_BLANK_NOREFERRER_ISSUE_MESSAGE,
            check.ANCHOR_TARGET_BLANK_NOREFERRER_ISSUE_CODE
        )
    }

    assert result == expected


def test_check_anchor_target_blank_missing_noreferrer():
    html = """
    <html>
        <body>
            <a href="https://example.com" target="_blank" rel="noopener">Test</a>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = set(
        check.check_anchor_target_blank_noopener(jl_file, {})
        + check.check_anchor_target_blank_noreferrer(jl_file, {})
    )
    expected = {
        issue.Issue(
            issue.IssueLocation(
                file_path=None,
                line=3,
                column=8
            ),
            check.ANCHOR_TARGET_BLANK_NOREFERRER_ISSUE_MESSAGE,
            check.ANCHOR_TARGET_BLANK_NOREFERRER_ISSUE_CODE
        )
    }

    assert result == expected


def test_check_anchor_target_blank_missing_noopener():
    html = """
    <html>
        <body>
            <a href="https://example.com" target="_blank" rel="noreferrer">Test</a>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = set(
        check.check_anchor_target_blank_noopener(jl_file, {})
        + check.check_anchor_target_blank_noreferrer(jl_file, {})
    )
    expected = {
        issue.Issue(
            issue.IssueLocation(
                file_path=None,
                line=3,
                column=8
            ),
            check.ANCHOR_TARGET_BLANK_NOOPENER_ISSUE_MESSAGE,
            check.ANCHOR_TARGET_BLANK_NOOPENER_ISSUE_CODE
        )
    }

    assert result == expected


def test_check_anchor_target_blank_both_rel_present():
    html = """
    <html>
        <body>
            <a href="https://example.com" target="_blank" rel="noopener noreferrer">Test</a>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = set(
        check.check_anchor_target_blank_noopener(jl_file, {})
        + check.check_anchor_target_blank_noreferrer(jl_file, {})
    )
    expected = set()

    assert result == expected


def test_check_anchor_target_blank_missing_target_blank():
    html = """
    <html>
        <body>
            <a href="https://example.com">Test</a>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = set(
        check.check_anchor_target_blank_noopener(jl_file, {})
        + check.check_anchor_target_blank_noreferrer(jl_file, {})
    )
    expected = set()

    assert result == expected


def test_check_anchor_target_blank_url_for():
    html = """
    <html>
        <body>
            <a href="{{ url_for('foo') }}">Test</a>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = set(
        check.check_anchor_target_blank_noopener(jl_file, {})
        + check.check_anchor_target_blank_noreferrer(jl_file, {})
    )
    expected = set()

    assert result == expected


def test_check_anchor_href_template_present():
    html = """
    <html>
        <body>
            <a href="{{ value }}">Test</a>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_anchor_href_template(jl_file, {})
    expected = [
        issue.Issue(
            issue.IssueLocation(
                file_path=None,
                line=3,
                column=8
            ),
            check.ANCHOR_HREF_TEMPLATE_ISSUE_MESSAGE,
            check.ANCHOR_HREF_TEMPLATE_ISSUE_CODE
        )
    ]

    assert result == expected


def test_check_anchor_href_template_url_for():
    html = """
    <html>
        <body>
            <a href="{{ url_for('foo') }}">Test</a>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_anchor_href_template(jl_file, {})
    expected = []

    assert result == expected


def test_check_unquoted_attributes_present():
    html = """
    <html>
        <body>
            <input name={{ value }} value="foo" />
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_unquoted_attributes(jl_file, {})
    expected = [
        issue.Issue(
            issue.IssueLocation(
                file_path=None,
                line=3,
                column=8
            ),
            check.UNQUOTED_ATTRIBUTE_ISSUE_MESSAGE,
            check.UNQUOTED_ATTRIBUTE_ISSUE_CODE
        )
    ]

    assert result == expected


def test_check_unquoted_attributes_single_quote():
    html = """
    <html>
        <body>
            <input name='{{ value }}' value="foo" />
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_unquoted_attributes(jl_file, {})
    expected = []

    assert result == expected


def test_check_unquoted_attributes_double_quote():
    html = """
    <html>
        <body>
            <input name="{{ value }}" value="foo" />
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_unquoted_attributes(jl_file, {})
    expected = []

    assert result == expected


def test_check_unquoted_attributes_url_for():
    html = """
    <html>
        <body>
            <input name={{ url_for('foo') }} value="foo" />
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_unquoted_attributes(jl_file, {})
    expected = []

    assert result == expected


def test_check_html_doctype_missing():
    html = """
    <html>
        <head>
        </head>
        <body>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_html_doctype(jl_file, {})
    expected = [
        issue.Issue(
            issue.IssueLocation(
                file_path=None,
                line=1,
                column=0
            ),
            check.DOCTYPE_ISSUE_MESSAGE,
            check.DOCTYPE_ISSUE_CODE
        )
    ]

    assert result == expected


def test_check_html_doctype_present():
    html = """
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_html_doctype(jl_file, {})
    expected = []

    assert result == expected


def test_check_html_charset_missing():
    html = """
    <html>
        <head>
        </head>
        <body>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_html_charset(jl_file, {})
    expected = [
        issue.Issue(
            issue.IssueLocation(
                file_path=None,
                line=1,
                column=0
            ),
            check.CHARSET_ISSUE_MESSAGE,
            check.CHARSET_ISSUE_CODE
        )
    ]

    assert result == expected


def test_check_html_charset_present():
    html = """
    <html>
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_html_charset(jl_file, {})
    expected = []

    assert result == expected


def test_check_html_content_type_missing():
    html = """
    <html>
        <head>
        </head>
        <body>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_html_content_type(jl_file, {})
    expected = [
        issue.Issue(
            issue.IssueLocation(
                file_path=None,
                line=1,
                column=0
            ),
            check.CONTENT_TYPE_ISSUE_MESSAGE,
            check.CONTENT_TYPE_ISSUE_CODE
        )
    ]

    assert result == expected


def test_check_html_content_type_present():
    html = """
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        </head>
        <body>
        </body>
    </html>
    """

    errors, jl_file = get_file(html)
    result = check.check_html_content_type(jl_file, {})
    expected = []

    assert result == expected

# https://github.com/returntocorp/jinjalint/issues/3
def test_attribute_name1():
    html = """
{% block extrastyle %}
{% load i18n static %}{% get_current_language_bidi as LANGUAGE_BIDI %}
<style type="text/css">
  #{{ id }}_map { width: {{ map_width }}px; height: {{ map_height }}px; }
  #{{ id }}_map .aligned label { float:inherit; }
  #{{ id }}_admin_map { position: relative; vertical-align: top; float: {{ LANGUAGE_BIDI|yesno:"right,left" }}; }
  {% if not display_wkt %}#{{ id }} { display: none; }{% endif %}
  .olControlEditingToolbar .olControlModifyFeatureItemActive {
     background-image: url("{% static "admin/img/gis/move_vertex_on.svg" %}");
     background-repeat: no-repeat;
  }
  .olControlEditingToolbar .olControlModifyFeatureItemInactive {
     background-image: url("{% static "admin/img/gis/move_vertex_off.svg" %}");
     background-repeat: no-repeat;
  }
</style>
<!--[if IE]>
<style type="text/css">
  /* This fixes the mouse offset issues in IE. */
  #{{ id }}_admin_map { position: static; vertical-align: top; }
  /* `font-size: 0` fixes the 1px border between tiles, but borks LayerSwitcher.
      Thus, this is disabled until a better fix is found.
  #{{ id }}_map { width: {{ map_width }}px; height: {{ map_height }}px; font-size: 0; } */
</style>
<![endif]-->
{% endblock %}
<span id="{{ id }}_admin_map">
<script>
//<![CDATA[
{% block openlayers %}{% include "gis/admin/openlayers.js" %}{% endblock %}
//]]>
</script>
<div id="{{ id }}_map"{% if LANGUAGE_BIDI %} dir="ltr"{% endif %}></div>
{% if editable %}
<a href="javascript:{{ module }}.clearFeatures()">{% translate "Delete all Features" %}</a>
{% endif %}
{% if display_wkt %}<p>{% translate "WKT debugging window:" %} </p>{% endif %}
<textarea id="{{ id }}" class="vWKTField required" cols="150" rows="10" name="{{ name }}">{{ wkt }}</textarea>
<script>{% block init_function %}{{ module }}.init();{% endblock %}</script>
</span>
    """
    _, jl_file = get_file(html)
    _ = check.check_html_content_type(jl_file, {})

def test_attribute_name2():
    html = """
{% load i18n static %}<!DOCTYPE html>
{% get_current_language as LANGUAGE_CODE %}{% get_current_language_bidi as LANGUAGE_BIDI %}
<html lang="{{ LANGUAGE_CODE|default:"en-us" }}" {% if LANGUAGE_BIDI %}dir="rtl"{% endif %}>
<head>
<title>{% block title %}{% endblock %}</title>
<link rel="stylesheet" type="text/css" href="{% block stylesheet %}{% static "admin/css/base.css" %}{% endblock %}">
{% block extrastyle %}{% endblock %}
{% if LANGUAGE_BIDI %}<link rel="stylesheet" type="text/css" href="{% block stylesheet_rtl %}{% static "admin/css/rtl.css" %}{% endblock %}">{% endif %}
{% block extrahead %}{% endblock %}
{% block responsive %}
    <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{% static "admin/css/responsive.css" %}">
    {% if LANGUAGE_BIDI %}<link rel="stylesheet" type="text/css" href="{% static "admin/css/responsive_rtl.css" %}">{% endif %}
{% endblock %}
{% block blockbots %}<meta name="robots" content="NONE,NOARCHIVE">{% endblock %}
</head>
{% load i18n %}

<body class="{% if is_popup %}popup {% endif %}{% block bodyclass %}{% endblock %}"
  data-admin-utc-offset="{% now "Z" %}">

<!-- Container -->
<div id="container">

    {% if not is_popup %}
    <!-- Header -->
    <div id="header">
        <div id="branding">
        {% block branding %}{% endblock %}
        </div>
        {% block usertools %}
        {% if has_permission %}
        <div id="user-tools">
            {% block welcome-msg %}
                {% translate 'Welcome,' %}
                <strong>{% firstof user.get_short_name user.get_username %}</strong>.
            {% endblock %}
            {% block userlinks %}
                {% if site_url %}
                    <a href="{{ site_url }}">{% translate 'View site' %}</a> /
                {% endif %}
                {% if user.is_active and user.is_staff %}
                    {% url 'django-admindocs-docroot' as docsroot %}
                    {% if docsroot %}
                        <a href="{{ docsroot }}">{% translate 'Documentation' %}</a> /
                    {% endif %}
                {% endif %}
                {% if user.has_usable_password %}
                <a href="{% url 'admin:password_change' %}">{% translate 'Change password' %}</a> /
                {% endif %}
                <a href="{% url 'admin:logout' %}">{% translate 'Log out' %}</a>
            {% endblock %}
        </div>
        {% endif %}
        {% endblock %}
        {% block nav-global %}{% endblock %}
    </div>
    <!-- END Header -->
    {% block breadcrumbs %}
    <div class="breadcrumbs">
    <a href="{% url 'admin:index' %}">{% translate 'Home' %}</a>
    {% if title %} &rsaquo; {{ title }}{% endif %}
    </div>
    {% endblock %}
    {% endif %}

    {% block messages %}
        {% if messages %}
        <ul class="messagelist">{% for message in messages %}
          <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message|capfirst }}</li>
        {% endfor %}</ul>
        {% endif %}
    {% endblock messages %}

    <!-- Content -->
    <div id="content" class="{% block coltype %}colM{% endblock %}">
        {% block pretitle %}{% endblock %}
        {% block content_title %}{% if title %}<h1>{{ title }}</h1>{% endif %}{% endblock %}
        {% block content %}
        {% block object-tools %}{% endblock %}
        {{ content }}
        {% endblock %}
        {% block sidebar %}{% endblock %}
        <br class="clear">
    </div>
    <!-- END Content -->

    {% block footer %}<div id="footer"></div>{% endblock %}
</div>
<!-- END Container -->

</body>
</html>
"""
    _, jl_file = get_file(html)
    _ = check.check_html_content_type(jl_file, {})


def test():
    test_check_csrf_protection_missing_token()
    test_check_csrf_protection_input_field_present()
    test_check_csrf_protection_flask_form_present()

    test_check_anchor_target_blank_missing_rel()
    test_check_anchor_target_blank_missing_noreferrer()
    test_check_anchor_target_blank_missing_noopener()
    test_check_anchor_target_blank_both_rel_present()
    test_check_anchor_target_blank_missing_target_blank()

    test_check_anchor_href_template_present()
    test_check_anchor_href_template_url_for()

    test_check_unquoted_attributes_present()
    test_check_unquoted_attributes_single_quote()
    test_check_unquoted_attributes_double_quote()
    test_check_unquoted_attributes_url_for()

    test_check_html_doctype_missing()
    test_check_html_doctype_present()

    test_check_html_charset_missing()
    test_check_html_charset_present()

    test_check_html_content_type_missing()
    test_check_html_content_type_present()

    test_attribute_name1()
    test_attribute_name2()

test()