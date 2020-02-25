import os
from pathlib import Path
import sys
from bottle import request, route, run, template, static_file
import mistune

def get_markdown_files(notepath: str) -> list:
    """takes notepath variable and generates a list of markdown files"""
    markdown_files = [] 
    for path in Path(notepath).rglob("*.md"):
        markdown_files.append(MarkdownNote(notepath, path.as_posix(), path.name))

    return markdown_files

def search_markdown_files(note: str, markdown_files: list):
    for markdown_file in markdown_files:
        if markdown_file.pretty_filename == note:
            return markdown_file

class MarkdownNote:
    """
    Simple data class to more easily work with absolute path names and filenames
    """
    def __init__(self, notepath, absolute_path, filename):
        self.notepath = notepath
        self.absolute_path = absolute_path
        self.filename = filename
        self.pretty_filename = self._get_pretty_name()
        self.url_path = self._get_url_path()
        self.rendered = ""

    def __str__(self):
        return f"{self.absolute_path}: {self.filename}"

    def _get_pretty_name(self):
        ## Need to make sure this doesn't pop a file without an md tag
        temp = self.filename.split(".")
        return temp[0]

    def _get_url_path(self):
        s = self.absolute_path.split("/")
        url_path_arr = []
        for i in s:
            if i not in self.notepath:
                url_path_arr.append(i)

        url_path_arr.pop()
        url_path_arr.append(self.pretty_filename)
        return "/".join(url_path_arr)

    def read(self):
        with open(self.absolute_path, 'r') as markdown_note:
            buf = markdown_note.read()
        return buf


    def render(self):
        buf = self.read()
        self.rendered = mistune.markdown(buf)
        return self.rendered

def create_routes(assets_path, notepath, markdown_files):
    # TODO find better way to do this
    main_template = f"{assets_path}/views/main.tpl"
    nav_template = f"{assets_path}/views/nav.tpl"
    searchbar_template = f"{assets_path}/views/searchbar.tpl"
    content_template = f"{assets_path}/views/content.tpl"
    mde_template = f"{assets_path}/views/mde.tpl"
    mde_test = f"{assets_path}/views/mde-test.tpl"
    home_template = f"{assets_path}/views/home.tpl"

    @route('/')
    @route('/home')
    @route('/index')
    def index():
        return template(
                main_template, 
                md=markdown_files, 
                f="",
                nav=nav_template,
                searchbar=searchbar_template,
                content=home_template)

    @route('/<note>')
    def r(note):
        markdown_file = search_markdown_files(note, markdown_files)
        rendered_markdown_note = markdown_file.render()
        return template(
                main_template, 
                rendered_markdown=rendered_markdown_note, 
                f=markdown_file, 
                md=markdown_files,
                nav=nav_template,
                searchbar=searchbar_template,
                content=content_template)

    @route('/static/<filename>')
    @route('/mde/static/<filename>')
    def server_static(filename):
        return static_file(
                filename, 
                root=f'{assets_path}/static')


    @route("/mde/<note>")
    def mde_note_edit(note):
        markdown_file = search_markdown_files(note, markdown_files)
        read_markdown_note = markdown_file.read()
        return template(
                main_template, 
                info=read_markdown_note, 
                md=markdown_files,
                nav=nav_template,
                searchbar=searchbar_template,
                content=mde_test)
        

def start_server(c):
    markdown_files = get_markdown_files(c.notepath)
    create_routes(c.assets_path, c.notepath, markdown_files)
    print("Starting Server")
    run(host=c.host, port=3000, reloader=True)
