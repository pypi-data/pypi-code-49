from flask import flash
import os
import markdown
import bleach
from bs4 import BeautifulSoup
from ctrlv_client.app import SITE_CONFIG_FILE
from ctrlv_client.app.models import Tag as tag
temp_site_config_file = os.path.join(
    os.path.dirname(SITE_CONFIG_FILE),
    'site-config-testing.json'
)


def truncate_snippet(html, length):
    truncated = False
    # 'html5lib' truncates properly and produces valid html
    # But adds html, head and body tags which we have to remove
    soup = BeautifulSoup(html[:length], 'html5lib')
    # unwarp does not work for some reason!
    soup.find('html').replaceWithChildren()
    soup.head.replaceWithChildren()
    soup.body.replaceWithChildren()
    if len(html) > length:
        truncated = True
    return_val = str(soup)
    return (return_val, truncated)


def error_flasher(form):
    for field, message_list in form.errors.items():
        for message in message_list:
            flash(form[field].label.text + ': ' + message, 'error')


def mask_config_file():
    if os.path.isfile(SITE_CONFIG_FILE):
        os.rename(SITE_CONFIG_FILE, temp_site_config_file)


def unmask_config_file():
    # Remove temporary site-config.json
    if os.path.isfile(SITE_CONFIG_FILE):
        os.remove(SITE_CONFIG_FILE)
    # Restore original site-config.json
    if os.path.isfile(temp_site_config_file):
        os.rename(temp_site_config_file, SITE_CONFIG_FILE)


def get_sanitized_html(markdown_text):
    html = markdown.markdown(
        markdown_text,
        extensions=['nl2br', 'smarty', 'pymdownx.tilde', 'extra']
    )
    # Tags deemed safe
    allowed_tags = [
        'a', 'abbr', 'acronym', 'b', 'blockquote', 'br',
        'code', 'dd', 'del', 'div', 'dl', 'dt', 'em',
        'em', 'h1', 'h2', 'h3', 'hr', 'i', 'img', 'li',
        'ol', 'p', 'pre', 's', 'strong', 'sub', 'sup',
        'table', 'tbody', 'td', 'th', 'thead', 'tr', 'ul'
    ]
    # Attributes deemed safe
    allowed_attrs = {
        '*': ['class'],
        'a': ['href', 'rel'],
        'img': ['src', 'alt']
    }
    # Sanitize the html using bleach &
    # Convert text links to actual links
    html_sanitized = bleach.clean(
        bleach.linkify(html),
        tags=allowed_tags,
        attributes=allowed_attrs
    )
    return html_sanitized


def get_tag_names(snippet_obj):
    # SELECT tags.tag_name
    # FROM tags
    # WHERE tags.tag_id IN (
    #    select tag_id
    #    from snippet_tags
    #    where
    #    snippet_id = ?
    # )
    tag_names = tag.query.with_entities(
        tag.tag_name
    ).filter(
        tag.tag_id.in_(
            # 'snippet.tags' returns the SnippetTags for the snippet
            st.tag_id for st in snippet_obj.tags
        )
    ).all()
    # ^ [('sql',), ('python',)]
    tag_names = [tup[0] for tup in tag_names]
    # ^ ['sql', 'python']
    return tag_names
