"""
This module constains the flask server and the classes for rendering live and static HTML
"""


import os
import codecs
import datetime
import shutil
import re
from copy import deepcopy, copy
import flask
from flask import request, jsonify
import yaml
from markdown import markdown
import requests
import gitbuilding as gb
from gitbuilding import warn


class GBServer(flask.Flask):
    """
    GBServer is the Git Building server it uses Flask to render documentation
    """

    def __init__(self, conf, dev=False):

        self.homepath = '.server_output'
        if os.path.exists(self.homepath):
            shutil.rmtree(self.homepath)
        self.doc = gb.Documentation(conf, self.homepath)
        self.doc.buildall()
        self.dev = dev

        self.unsaved_dropped_files = []

        if self.doc.landing is not None:
            self.homepage = os.path.join(self.homepath, self.doc.landing)
        else:
            self.homepage = None

        self.gbpath = os.path.dirname(gb.__file__)
        self.read_project_data()

        super(GBServer, self).__init__(__name__)

        # allow hot-reloading of live-editor in development mode
        if dev:
            self.add_url_rule('/static/live-editor/<path:subpath>',
                              'dev_editor_static',
                              self._dev_editor_static)
            self.add_url_rule('/static/<path:subpath>',
                              'dev_other_static',
                              self._dev_other_static)
            self.add_url_rule('/sockjs-node/<path:subpath>',
                              'dev_editor_sockjs',
                              self._dev_editor_sockjs)
            self.add_url_rule('/__webpack_dev_server__/<path:subpath>',
                              'dev_editor_webpack',
                              self._dev_editor_webpack)

        # Define URL rules!
        self.add_url_rule('/', 'render', self._render_page)
        self.add_url_rule('/render_markdown',
                          'live_render',
                          self._live_render,
                          methods=['POST'])
        self.add_url_rule('/<path:subpath>', 'render', self._render_page)
        self.add_url_rule('/assets/<path:subpath>',
                          'assets',
                          self._return_assets)
        self.add_url_rule('/editor/', 'editor', self._edit_page)
        self.add_url_rule('/editor/save',
                          'save',
                          self._save_edit,
                          methods=['POST'])
        self.add_url_rule('/editor/raw', 'raw', self._raw_md)
        self.add_url_rule('/editor/<path:subpath>',
                          'editor_redirect',
                          self._editor_redirect)
        self.add_url_rule('/<path:subpath>/editor/', 'editor', self._edit_page)
        self.add_url_rule('/<path:subpath>/editor/raw', 'raw', self._raw_md)
        self.add_url_rule('/<path:subpath>/editor/save',
                          'save',
                          self._save_edit,
                          methods=['POST'])
        self.add_url_rule('/<path:subpath>/editor/dropped-file',
                          'droppedfile',
                          self._dropped_file,
                          methods=['POST'])
        self.add_url_rule('/editor/dropped-file',
                          'droppedfile',
                          self._dropped_file,
                          methods=['POST'])
        self.add_url_rule('/<path:otherpath>/editor/<path:subpath>',
                          'editor_redirect',
                          self._editor_redirect)

        #Two render objects, one for static one for live
        self.renderer = GBRenderer(self.project_data)
        self.live_renderer = GBRenderer(deepcopy(self.project_data))

    def read_project_data(self):
        """
        Reads the project data generated when converting BuildUp to markdown
        """

        with open(os.path.join(self.homepath, '_data', 'project.yaml'), 'r') as stream:
            self.project_data = yaml.load(stream, Loader=yaml.SafeLoader)

    def _get_docpage(self, subpath):
        """
        Gets a Page object from the Documentation object
        """
        if len(subpath) == 0:
            return None

        if subpath in self.doc.pages:
            ind = self.doc.pages.index(subpath)
            return self.doc.pages[ind]
        return gb.Page(subpath, self.doc, empty=True)

    def _raw_md(self, subpath=None):
        """
        Get the raw markdown for pages in the documentation
        Returns this in JSON
        """
        if subpath is None and request.path == '/editor/raw':
            if self.homepage is not None:
                md = self.doc.landing_page.get_raw()
                return jsonify({'md': md})
            return jsonify({'md': ""})

        if subpath in self.doc.pages:
            page = self._get_docpage(subpath)
            if page is None:
                md = ''
            else:
                md = page.get_raw()
            return jsonify({'md': md, 'page': subpath})
        return jsonify({'md': "# Empty page\n\nEdit me", 'page': subpath})

    def _save_edit(self, subpath=None):
        """
        Saves the edits from the live editor and full rebuilds the documentation
        """
        content = request.get_json()
        #TODO: better checking of uploaded files from other open editors
        for uploaded_file in content['uploadedFiles']:
            if uploaded_file in content['md']:
                if not os.path.isfile(uploaded_file):
                    shutil.copyfile(
                        os.path.join(
                            self.homepath,
                            uploaded_file),
                        uploaded_file)
                else:
                    warn(f"{uploaded_file} already exists perhaps an issue when editing two files at once.")
        self.unsaved_dropped_files = []

        if content['md'] is not None:
            if subpath is None:
                if self.homepage is not None:
                    saved = self.doc.landing_page.save(content['md'])
            else:
                page = self._get_docpage(subpath)
                saved = page.save(content['md'])

            if saved:
                self.doc.buildall(force=True)
                self.read_project_data()
                self.renderer.project_data = self.project_data
                self.renderer.populate_vars()
                return jsonify({'saved': True})

        return jsonify({'saved': False})

    def _dropped_file(self, subpath=None):
        """
        This gets run if a file gets dragged and dropped into the editor
        """
        files = request.files
        # loop through all but return after first image.
        for file in files:
            if files[file].mimetype.startswith('image'):
                files[file].filename = files[file].filename.replace(' ','')
                fname = os.path.join('images', files[file].filename)
                fpath = os.path.join(self.homepath, fname)
                if not os.path.isfile(fname):
                    files[file].save(fpath)
                self.unsaved_dropped_files.append(fname)
                return jsonify({'received': True, 'filename': fname})
            else:
                warn(f"Cannot upload file of mimtype: {files[file].mimetype}")


        # if not returned yet nothing was an image
        return flask.abort(405)

    def _live_render(self):
        """
        Runs the live renderer and returns the html as well as warnings
        in JSON format
        """
        content = request.get_json()
        if content['md'] is None:
            return jsonify({'html': '', 'log': '', 'number': 0})

        loglength = self.doc.get_log_length()
        if not 'page' in content:
            if self.homepage is not None:
                page = self.doc.landing_page
                processed_text = page.rebuild(content['md'])
                title = page.title
                self.live_renderer.project_data['Title'] = title
                self.live_renderer.populate_vars()
            else:
                processed_text = ""
        else:
            page = self._get_docpage(content['page'])
            if page is None:
                return jsonify({'html': '', 'log': '', 'number': 0})
            processed_text = page.rebuild(content['md'])
        html = self.live_renderer.render_md(
            processed_text, page.filepath, fullpage=False, nav=False)
        log = self.doc.get_log(loglength)

        #Catching warnings that should not have been generated for
        #missing dropped files.
        poplist = []
        for n, log_entry in enumerate(log):
            error_info = log_entry['error_info']
            if error_info is not None:
                if error_info['error_type'] == 'missing':
                    if error_info['file'] in self.unsaved_dropped_files:
                        poplist.append(n)

        if len(poplist) > 0:
            for n in reversed(poplist):
                log.pop(n)

        return jsonify({'html': html,
                        'log': self.live_renderer.format_warnings(log),
                        'number': len(log)})

    def _edit_page(self, subpath=None):
        """
        Starts the live editor for a particular page
        """
        if (subpath is None and request.path == "/editor/") or subpath.endswith('.md'):
            self.live_renderer.project_data = deepcopy(self.project_data)
            self.live_renderer.populate_vars()
            if self.dev:  # for hot-reloading
                url = "http://localhost:8080/static/live-editor/"
                try:
                    req = requests.get(url)
                except requests.exceptions.RequestException:
                    msg = (f"ERROR: Could not connect to live-editor dev server"
                           f" on '{url}', did you forget to start it?")
                    return flask.abort(flask.Response(msg, status=500))
                return req.text

            page = os.path.join(self.gbpath, 'static', 'live-editor', 'index.html')
            return flask.send_file(page)

        html = self.renderer.render("<h1>Sorry. Cannot edit this file!</h1>")
        return html

    def _editor_redirect(self, subpath=None, otherpath=None):
        """
        Relative links inside the editor will go to here instead of their intended
        desitination. This redirects them to the correct place.
        """
        return flask.redirect(f'/{subpath}')

    def _render_page(self, subpath=None):
        """
        Renders the static version of a page
        """
        # define special page for missing
        if subpath == 'missing':
            return self.renderer.missing_page()
        if subpath is None:
            if self.homepage is not None:
                page = self.homepage
            else:
                return self.renderer.render_md(
                    "No homepage set", editorbutton=False)
        else:
            page = os.path.join(self.homepath, subpath)

        if os.path.isfile(page):
            if page.endswith('.md'):
                editorbutton = bool((subpath is None) or subpath in self.doc.pages)
                return self.renderer.render_md_file(page, subpath, editorbutton=editorbutton)
            return flask.send_file(os.path.abspath(page))

        if page.endswith('.md'):
            return self.renderer.render_md(
                f"# Page not found\n Do you want to [create it](/{subpath}/editor)",
                subpath,
                editorbutton=True)

        return flask.abort(404)

    def _return_assets(self, subpath):
        """
        returns file from the assets directory
        """
        page = os.path.join('assets', subpath)
        if os.path.isfile(page):
            return flask.send_file(os.path.abspath(page))

        return flask.abort(404)

    def run(self, host='localhost', port=6178):
        """
        Starts the flask server
        """
        super(GBServer, self).run(host, port)

    def _dev_editor_static(self, subpath):
        url = "http://localhost:8080/static/live-editor/" + subpath
        try:
            req = requests.request(flask.request.method, url)
        except requests.exceptions.RequestException:
            msg = f"ERROR: Could not connect to live-editor dev server for '{url}', did you forget to start it?"
            return flask.abort(flask.Response(msg, status=500))
        return req.text

    def _dev_editor_sockjs(self, subpath):
        url = "http://localhost:8080/sockjs-node/" + \
            subpath + flask.request.query_string.decode()
        try:
            req = requests.request(flask.request.method, url)
        except requests.exceptions.RequestException:
            msg = f"ERROR: Could not connect to live-editor dev server for '{url}', did you forget to start it?"
            return flask.abort(flask.Response(msg, status=500))
        return req.text

    def _dev_editor_webpack(self, subpath):
        url = "http://localhost:8080/__webpack_dev_server__/" + \
            subpath + flask.request.query_string.decode()
        try:
            req = requests.request(flask.request.method, url)
        except requests.exceptions.RequestException:
            msg = f"ERROR: Could not connect to live-editor dev server for '{url}', did you forget to start it?"
            return flask.abort(flask.Response(msg, status=500))
        return req.text

    def _dev_other_static(self, subpath):
        return flask.send_from_directory('static', subpath)


def html_build(conf, build_dir=None):
    """
    This function builds static HTML from the built markdown in the build_dir directory
    """

    if build_dir is None:
        build_dir = 'Output'

    if conf is None:
        settings = {}
    else:
        with open(conf, 'r') as stream:
            settings = yaml.load(stream, Loader=yaml.SafeLoader)

    if 'WebsiteRoot' in settings:
        root = settings['WebsiteRoot']
    else:
        root = '/'

    assert os.path.exists(
        os.path.join(
            build_dir, "_data", "project.yaml")), "Build directory to be a Git Building output."
    with open(os.path.join(build_dir, '_data', 'project.yaml'), 'r') as stream:
        project_data = yaml.load(stream, Loader=yaml.SafeLoader)
    renderer = GBRenderer(project_data, root=root)

    # Dont make site dir setable unless we want to do checks that the
    # directory is correct before removing the whole tree
    site_dir = '_site'
    if os.path.exists(site_dir):
        shutil.rmtree(site_dir)
    os.mkdir(site_dir)
    with open(os.path.join(site_dir, 'missing.html'), 'w') as html_file:
        html_file.write(renderer.missing_page())
    for filename in project_data['FileList']:
        build_file = os.path.join(build_dir, filename)
        link, fextension = os.path.splitext(filename)
        out_dir = os.path.join(site_dir, os.path.dirname(filename))
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        if fextension == '.md':
            if filename == project_data['Homepage']:
                out_file = os.path.join(site_dir, 'index.html')
            else:
                out_file = os.path.join(site_dir, link + '.html')
            with open(out_file, 'w') as html_file:
                page_html = renderer.render_md_file(build_file, filename, editorbutton=False)
                html_file.write(fix_md_links(page_html))
        else:
            out_file = os.path.join(site_dir, filename)
            shutil.copy(build_file, out_file)

    gbpath = os.path.dirname(gb.__file__)
    static_dir = os.path.join(gbpath, 'static')
    for root, dirs, files in os.walk(static_dir): # pylint: disable=unused-variable
        for filename in files:
            if not 'live-editor' in root:
                filepath = os.path.join(root, filename)
                out_file = os.path.join(
                    site_dir, os.path.relpath(
                        filepath, gbpath))
                out_dir = os.path.dirname(out_file)
                if not os.path.exists(out_dir):
                    os.makedirs(out_dir)
                shutil.copy(filepath, out_file)
    if os.path.exists('assets'):
        for root, dirs, files in os.walk('assets'):
            for filename in files:
                filepath = os.path.join(root, filename)
                out_file = os.path.join(site_dir, filepath)
                out_dir = os.path.dirname(out_file)
                if not os.path.exists(out_dir):
                    os.makedirs(out_dir)
                shutil.copy(filepath, out_file)


def fix_md_links(html):
    """
    This function finds links to markdown files in the static
    documentation pages and removes the .md
    """
    links = re.findall(r'((href="[^"]*?)(\.md)("))', html, re.MULTILINE)
    for link in links:
        html = html.replace(link[0], link[1] + link[3])
    return html


def is_active_nav_item(nav_item,link):
    if nav_item["Link"] == link:
        return True
    if 'SubNavigation' in nav_item:
        for sub_nav_item in nav_item['SubNavigation']:
            if is_active_nav_item(sub_nav_item,link):
                return True
    return False

class GBRenderer():
    """
    This class is the renderer for GitBuilding HTML
    """

    def __init__(self, project_data, root='/'):
        self.gbpath = os.path.dirname(gb.__file__)
        self.project_data = project_data
        self.root = root

        self.custom_style = []
        self.custom_favicons = []

        # set default values which may be overriddent by HTML options
        self.reference_gb = True
        self.custom_footer = ""
        self.custom_header = ""

        # Variables that can be accessed by custom Footer/Header
        self.populate_vars()

        if 'HTMLOptions' in self.project_data:
            options = self.project_data['HTMLOptions']
            if 'AcknowledgeGitBuilding' in options and not options['AcknowledgeGitBuilding']:
                self.reference_gb = False
            if 'CustomFooter' in options:
                self.custom_footer = str(options['CustomFooter'])
            if 'CustomHeader' in options:
                self.custom_header = str(options['CustomHeader'])

        self.scan_assets()

    def populate_vars(self):
        """
        This function populates the list of variables that can be used in
        custom headers and footers
        """
        self.variables = {
            'Title': self.project_data['Title'],
            'Year': datetime.datetime.now().year,
            'Root': self.root
        }
        if 'Authors' in self.project_data:
            self.variables['Authors'] = self.authorlist()
        if 'Email' in self.project_data:
            self.variables['Email'] = self.project_data['Email']
        if 'Affiliation' in self.project_data:
            self.variables['Affiliation'] = self.project_data['Affiliation']
        if 'License' in self.project_data:
            if 'LicenseFile' in self.project_data:
                self.variables['License'] = f'<a href="{self.root}{self.project_data["LicenseFile"]}">{self.project_data["License"]}</a>'
            else:
                self.variables['License'] = self.project_data['License']

        if 'Variables' in self.project_data:
            for key in self.project_data['Variables'].keys():
                self.variables[key] = self.project_data['Variables'][key]

    def scan_assets(self):
        """
        This scans the assets folder of the project to look for custom CSS and favicons
        """
        if os.path.exists('assets'):
            for root, dirs, files in os.walk('assets'): # pylint: disable=unused-variable
                for filename in files:
                    filepath = os.path.join(root, filename)
                    if filepath.endswith('.css'):
                        self.custom_style.append(filepath)
                    if filename == 'favicon.ico':
                        self.custom_favicons.append(filepath)
                    if re.match(r"^favicon-[0-9]+x[0-9]+\.png$", filename):
                        self.custom_favicons.append(filepath)

    def safe_format(self, text, warn_intro="Problem formatting string - "):
        """
        Safely formats code as though it was an f-string but only allows a restricted variable set
        """

        # find all text inside braces
        matches = re.findall(r'((?<!\{)\{([^\{\}\n]+)\}(?!\}))', text)
        # Replace valid matches
        for match in matches:
            var = match[1].strip()
            if var in self.variables:
                text = text.replace(match[0], f'{self.variables[var]}')
            else:
                text = text.replace(match[0], '???')
                warn(warn_intro + f'Variable "{var}" not valid in this context.')

        # Find odd numbers of braces together

        cleantext = re.sub(r'(?<!\{)((?:\{\{)*)(\{)(?!\{)', r'\g<1>', text)
        cleantext = re.sub(
            r'(?<!\})((?:\}\})*)(\})(?!\})',
            r'\g<1>',
            cleantext)

        if not cleantext == text:
            warn(warn_intro + 'Unmatched braces removed from format string')
        text = cleantext.replace('{{', '{')
        text = text.replace('}}', '}')

        return text

    def header(self, fullpage=True, nav=True, link=None, editorbutton=False):
        """
        This function returns the full top of the HTML page including the <head> section
        It inludes the code from the project_header function and also the navigation.
        It opens the <div> for page content
        """

        output = ''
        if link is None:
            edlink = 'editor'
        else:
            edlink = f'/{link}/editor'
        if fullpage:
            output += f"""<!DOCTYPE html>
<html>
<head>
    <title>{self.project_data['Title']}</title>"""
            if self.custom_favicons:
                for favicon in self.custom_favicons:
                    if favicon.endswith("favicon.ico"):
                        output += f"""    <link rel="shortcut icon" href="{self.root}{favicon}" />"""
                    else:
                        output += f"""    <link rel="icon" type="image/png" href="{self.root}{favicon}" sizes="{re.findall('[0-9]+x[0-9]+',favicon)[-1]}" />"""
            else:
                output += f"""    <link rel="shortcut icon" href="{self.root}static/Logo/favicon.ico" />
    <link rel="icon" type="image/png" href="{self.root}static/Logo/favicon-32x32.png" sizes="32x32" />
    <link rel="icon" type="image/png" href="{self.root}static/Logo/favicon-16x16.png" sizes="16x16" />"""
            output += f"""    <link href="{self.root}static/style.css" rel="stylesheet">\n"""
            for sheet in self.custom_style:
                output += f'    <link href="{self.root}{sheet}" rel="stylesheet">\n'
            output += f"""<script type="text/javascript" src="{self.root}static/3d-viewer.js"></script>
</head>
<body>"""
        else:
            for sheet in self.custom_style:
                output += f'''<style>{codecs.open(sheet, mode="r", encoding="utf-8").read()}</style>'''
        output += f"""<header class="site-header">
<div class="wrapper">
{self.project_header()}"""
        if editorbutton:
            output += f"""<div class=header-buttons><button onclick="window.location.href = '{edlink}';">Edit</button></div>"""
        output += f"""</div>
</header>
<div class="page-content">"""
        if nav and (len(self.project_data['Navigation']) > 0):
            output += f"""
            <div>
<nav class="sidebar">
    <a href="#" class="menu-icon">
    <svg viewBox="0 0 18 15">
        <path fill="#424242" d="M18,1.484c0,0.82-0.665,1.484-1.484,1.484H1.484C0.665,2.969,0,2.304,0,1.484l0,0C0,0.665,0.665,0,1.484,0 h15.031C17.335,0,18,0.665,18,1.484L18,1.484z"/>
        <path fill="#424242" d="M18,7.516C18,8.335,17.335,9,16.516,9H1.484C0.665,9,0,8.335,0,7.516l0,0c0-0.82,0.665-1.484,1.484-1.484 h15.031C17.335,6.031,18,6.696,18,7.516L18,7.516z"/>
        <path fill="#424242" d="M18,13.516C18,14.335,17.335,15,16.516,15H1.484C0.665,15,0,14.335,0,13.516l0,0 c0-0.82,0.665-1.484,1.484-1.484h15.031C17.335,12.031,18,12.696,18,13.516L18,13.516z"/>
    </svg>
    </a>
    <ul class="nav-list">
    {self.nav_links(link=link)}
    </ul>
</nav></div>"""
        output += f"""
<div class="wrapper">
"""
        return output

    def nav_links(self, link=None):
        """
        This function returns the side navigation
        """
        html = f'<li><a class="navhome" href="{self.root}">{self.project_data["Title"]}</a></li>'
        for nav_item in self.project_data['Navigation']:
            li_class_txt = ''
            a_class_txt = ''
            if is_active_nav_item(nav_item,link):
                li_class_txt = ' class="active"'
                if nav_item["Link"] == link:
                  a_class_txt = 'class="active "'
            html += f'<li{li_class_txt}><a {a_class_txt}href="{self.root}{nav_item["Link"]}">{nav_item["Title"]}</a>'
            if 'SubNavigation' in nav_item:
                html += '<ul class="sub-nav-list">'
                for sub_nav_item in nav_item['SubNavigation']:
                    if is_active_nav_item(sub_nav_item,link):
                        a_class_txt = 'class="active "'
                    else:
                        a_class_txt = ''
                    html += f'<li><a {a_class_txt}href="{self.root}{sub_nav_item["Link"]}">{sub_nav_item["Title"]}</a></li>'
                html += "</ul>"
            html += "</li>"
        return html

    def authorlist(self):
        """
        This function returns a rendered authour list
        """
        text = ''
        for i, author in enumerate(self.project_data['Authors']):
            if i == 0:
                pass
            elif i == len(self.project_data['Authors']) - 1:
                text += ', and '
            else:
                text += ', '
            text += f'{author}'
        return text

    def project_header(self):
        """
        This is the project header that can be customised.
        """
        html = '<div class=header-text>'
        if self.custom_header:
            html += self.safe_format(self.custom_header,
                                     warn_intro="Problem formatting custom header - ")
        else:
            if self.project_data['Title'] is not None:
                html += f'<a class="site-title" href="{self.root}">{self.project_data["Title"]}</a>'
            if self.project_data['Authors'] is not None:
                html += '<p class="author">by '
                html += self.authorlist()
                html += '</p>'
            if self.project_data['Affiliation'] is not None:
                html += f'<p class="affiliation">{self.project_data["Affiliation"]}</p>'
        html += '</div>'
        return html

    def footer(self, fullpage=True):
        """
        This function closes the container div and includes the reference to GitBuilding (if used) and the
        project footer
        """
        output = """</div>
</div>
<footer class="site-footer">
<div class="wrapper">"""
        if self.reference_gb:
            output += f"""<a target="_blank" rel="noopener noreferrer" href="https://gitlab.com/bath_open_instrumentation_group/git-building"><span class="icon">{codecs.open(os.path.join(self.gbpath,'static','Logo','GitBuilding.svg'), mode="r", encoding="utf-8").read()}</span>
<span class="info">Documentation powered by Git Building</span></a>"""
        output += f"""{self.project_footer()}
</div>
</footer>"""
        if fullpage:
            output += """</body>
</html>"""
        return output

    def project_footer(self):
        """
        This returns either the standard project footer or the customised footer
        """
        if self.custom_footer:
            return self.safe_format(
                self.custom_footer, warn_intro="Problem formatting custom footer - ")
        html = ''
        if self.project_data['Authors'] is not None:
            html += '<p class="author">© '
            html += self.authorlist()
            html += f' {datetime.datetime.now().year}</p>'
        if self.project_data['Email'] is not None:
            html += f'<p class="email">Contact: <a href="mailto:{self.project_data["Email"]}">{self.project_data["Email"]}</a></p>'
        if self.variables['License'] is not None:
            html += f'<p class="license">{self.project_data["Title"]} is released under {self.variables["License"]}</p>'
        return html

    def render_md_file(self, page, link, editorbutton=False):
        """
        This function returns the rendered HTML for a given md file
        """
        with codecs.open(page, mode="r", encoding="utf-8") as md_file:
            return self.render_md(md_file.read(), link=link, editorbutton=editorbutton)

    def render_md(self, md, link=None, fullpage=True, nav=True, editorbutton=False):
        """
        This function returns the rendered HTML for input markdown
        """

        # find more than one image on a line and replace with gallery
        imlines = re.findall(
            r'^((?:[ \t]*!\[[^\]]*\]\(\s*[^\)\s]+\s*(?:\"[^\"\n\r]*\")?\)){2,}[ \t]*)$',
            md,
            re.MULTILINE)

        for n, imline in enumerate(imlines):
            gallery = '\n\n<div class="gallery-thumb">'

            ims = re.findall(
                r'!\[[^\]]*\]\(\s*([^\)\s]+)\s*(?:\"([^\"\n\r]*)\")?\)', imline)

            for im in ims:
                gallery += f'''<img onmouseover="getElementById('gallery-show{n}').src=this.src" src="{im[0]}" alt="{im[1]}" />'''

            gallery += f'</div><div class="gallery-show"><img id="gallery-show{n}" src="{ims[0][0]}" alt="{ims[0][1]}"/></div>'

            md = md.replace(imline, gallery)

        stls = re.findall(r'(^(\[[^\]]*\])\((.+?\.stl)\))', md, re.MULTILINE)
        for stl in stls:
            md = md.replace(
                stl[0],
                f'{stl[1]}({stl[2]})\n<stl-part-viewer src="{stl[2]}" width="500" height="500" floorcolor="0xf1f1f1"></stl-part-viewer>')

        content_html = markdown(md, extensions=['tables', 'attr_list'])
        return self.render(content_html,
                           link=link,
                           fullpage=fullpage,
                           nav=nav,
                           editorbutton=editorbutton)

    def render(self, html, link=None, fullpage=True, nav=True, editorbutton=False):
        """
        This function creates the full HTML page from the input HTML generated from BuildUp
        """

        # Fix rel links as they can do funny things
        rellinks = re.findall(
            r'((href|src)="(\.\.\/[^"]*?)")',
            html,
            re.MULTILINE)
        if link is not None:
            linkdir = os.path.dirname(link)
        else:
            linkdir = ""
        for rellink in rellinks:
            rootedlink = os.path.normpath(os.path.join(linkdir, rellink[2]))
            html = html.replace(
                rellink[0], f'{rellink[1]}="{self.root}{rootedlink}"')

        output = self.header(fullpage=fullpage,
                             nav=nav,
                             link=link,
                             editorbutton=editorbutton)
        output += html
        output += self.footer(fullpage=fullpage)
        return output

    def missing_page(self):
        """
        This returns an HTML page for missing parts.
        """
        return self.render('<h1>Git Building Missing Part</h1>')

    def format_warnings(self, warnings):
        """
        Returns warnings for the live renderer to display
        """
        output = ""
        for warning in warnings:
            if warning['fussy']:
                cssclass = 'fussywarning'
                warntype = "FussyWarning"
            else:
                cssclass = 'warning'
                warntype = "Warning"
            output += f'<p class="{cssclass}">{warntype}: {warning["message"]}</p>\n'
        return output
