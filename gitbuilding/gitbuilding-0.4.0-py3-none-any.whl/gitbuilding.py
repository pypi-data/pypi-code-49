"""
This module contains the core of GitBuilding. It has a core class for the documentation
and also classes for libraries, pages, part lists, and parts as well as a number of
helper funtions
"""

import codecs
import re
import os
import sys
import shutil
from copy import deepcopy
import datetime
import yaml
from colorama import Fore, Back, Style
import gitbuilding as gb


class Config():
    """
    This class stores config information. Currently it is more of a
    big data structure than a functioning class.
    """

    def __init__(self):
        self.categories = {
            'part': {'Reuse': False, 'DisplayName': 'Parts'},
            'tool': {'Reuse': True, 'DisplayName': 'Tools'}
        }
        self.fussy = True
        self.default_category = 'part'
        self.debug = False
        self.out_dir = 'Output'
        self.page_bom_title = ""
        # TODO make exclude setable
        self.exclude = "README.md"


# global config object- I think I am OK with this!
config = Config()

warninglog = []

# used to trace warnings
activepage = ""


def warn(message, fussy=False, error_info = None):
    """
    Raises GitBuilding warning this will print the warning and log
    it in a way that it can be shown by the live editor.
    Error info is a dictionary of extra information on the error,
    this may be used to silence errors by the server.
    """
    if activepage == "":
        onpage = ""
    else:
        onpage = f"  Warning when scanning page: '{activepage}'"

    # if the warning is tagged fussy and fussy warning are on
    if fussy and config.fussy:
        print(
            Fore.YELLOW +
            "Fussy Warning: " +
            message +
            Style.RESET_ALL +
            onpage)
    else:
        print(Fore.RED + "Warning: " + message + Style.RESET_ALL + onpage)

    warninglog.append({'message': message, 'onpage': onpage, 'fussy': fussy, 'error_info': error_info})


def gberror(message, followup=""):
    """
    This throws exits the program on an error after making a bright colourful and
    clear error in the terminal
    """

    if activepage == "":
        onpage = ""
    else:
        onpage = f"Error when scanning page: '{activepage}'"
    print(Back.RED + "Fatal Error: " + message +
          Style.RESET_ALL + "\n" + followup + "\n" + onpage)
    sys.exit(1)


def make_dir_if_needed(dir_or_file, isfile=False):
    '''Makes the directory if it doesn't exist.
    Handles empty strings for directory'''
    if isfile:
        directory = os.path.dirname(dir_or_file)
    else:
        directory = dir_or_file
    if not directory == '':
        if not os.path.exists(directory):
            os.makedirs(directory)


def parse_inline_yaml(txt):
    """
    This function returns a python dictionary from inline YAML by parsing it
    with YAML flow-style.

    https://yaml.org/spec/1.2/spec.html#style/flow/

    It also puts in spaces after `:` if forgotten

    It also lowers the case of every key
    """
    try:
        in_dict = yaml.safe_load('{' + txt + '}')

        # look for errors where no space is after the key
        key_errors = False
        for key in in_dict.keys():
            # no space after key results in a key with a colon and None for a
            # result
            if ':' in key and in_dict[key] is None:
                key_errors = True
                # add in the space after colon
                txt = txt.replace(key, key.replace(':', ': '))
        # if there were key errors then run again
        if key_errors:
            in_dict = yaml.safe_load('{' + txt + '}')

        out_dict = {}
        for key in in_dict.keys():
            out_dict[key.lower()] = in_dict[key]
        return out_dict
    except BaseException:
        return None

def valid_navigation(navigation):
    '''
    Checks if navigation list is valid.
    '''

    if type(navigation) is not list:
        return False

    for nav_item in navigation:
        if type(nav_item) is not dict:
            return False

        if 'Link' not in nav_item:
            return False

        if 'Title' not in nav_item:
            return False

        if 'SubNavigation' in nav_item:
            if not valid_navigation(nav_item['SubNavigation']):
                return False

    return True

def replace_ims(text, replaceall=True, page_dir=None):
    """
    Replaces the images in a markdown file with a link to the output location
    This also copies the image to the new location. These jobs should be split

    page_dir sets directory or a page inside the GitBuilding directory
    to make relative links work. We need to do this in a less insane way
    """

    # Find images in the text
    # Group 1: all
    # Group 2: alt-text
    # Group 3: image-path
    # group 4: hover text
    ims = re.findall(r'(!\[([^\]]*)\]\(\s*([^\)\s]+)\s*(?:\"([^\"\n\r]*)\")?\))',
                     text, re.MULTILINE)
    for im in ims:
        imagepath = im[2]

        if page_dir is None:
            image_exists = os.path.isfile(imagepath)
        else:
            image_exists = os.path.isfile(os.path.join(page_dir, imagepath))

        if image_exists:
            if (page_dir is not None) and (not os.path.isabs(imagepath)):
                imagepath = os.path.normpath(os.path.join(page_dir, imagepath))
            # The images path relative to the images directory
            imrelpath = os.path.relpath(imagepath, 'images')
            if imrelpath.startswith('..'):
                warn(f"Image: {imagepath} is not in the images directory. Image will"
                     " be coppied into build but may cause unreliable behaviour")
                imrelpath = os.path.split(imagepath)[1]
            # relative to base folder
            newimrelpath = os.path.join('images', imrelpath)
            newimpath = os.path.join(config.out_dir, newimrelpath)

            if replaceall or (not os.path.isfile(newimpath)):
                try:
                    make_dir_if_needed(newimpath, isfile=True)
                    shutil.copyfile(imagepath, newimpath)
                except BaseException:
                    warn(f"Couldn't copy file '{imagepath}' to output.")
            # now relative to page
            newimrelpath = os.path.relpath(newimrelpath, page_dir)
            text = text.replace(im[0], f'![{im[1]}]({newimrelpath} "{im[3]}")')
        else:
            warn(f"'{imagepath}' is missing.",error_info={'error_type':'missing','file':imagepath})

    return text


def replace_stl_links(text, tofile=True, page_dir=None):
    """
    This functions finds any link to an STL that starts on its own line,
    copies STL to the output directory and updates the link.
    This doesn't make the part page for the STL, it is only for inline
    replacement.
    """

    # Find stls in the text
    # Group 1: all
    # Group 2: link syntax
    # Group 3: stl file
    stls = re.findall(r'(^(\[[^\]]*\])\((.+?\.stl)\))', text, re.MULTILINE)

    for stl in stls:
        stlpath = stl[2]
        if (page_dir is not None) and (not os.path.isabs(stlpath)):
            stlpath = os.path.normpath(os.path.join(page_dir, stlpath))
        # The stl path relative to the models directory
        stlrelpath = os.path.relpath(stlpath, 'models')
        if stlrelpath.startswith('..'):
            warn(
                f"STL: {stlpath} is not in the models directory. "
                "File will be copied into build but may cause unreliable behaviour")
            stlrelpath = os.path.split(stlpath)[1]
        # relative to base folder
        newstlrelpath = os.path.join('models', stlrelpath)
        newstlpath = os.path.join(config.out_dir, newstlrelpath)
        if tofile:
            try:
                make_dir_if_needed(newstlpath, isfile=True)
                shutil.copyfile(stlpath, newstlpath)
            except BaseException:
                warn(
                    f"Couldn't copy file '{stlpath}' to output, does it exist?")
        # now relative to page
        newstlrelpath = os.path.relpath(newstlrelpath, page_dir)
        text = text.replace(stl[0], f'{stl[1]}({newstlrelpath})')
    return text


def find_reference_links(text):
    """
    Function to find reference style links.
    Returns a list of dictionaries, one dictionary per link
    """

    # Looking for reference style links. These must use "*" or '*' to define alt-text not (*)
    # Group 1: link text
    # Group 2: link location
    # Group 3: either a ' or a ", captured so regex can find the equivalent
    # Group 4: alt text
    ref_link_matches = re.findall(
        r'''(^[ \t]*\[(.+)\]:[ \t]*([^\"\' \t]*)(?:[ \t]+(\"|')((?:\\\4|(?!\4).)*?)\4)?[ \t]*$)''',
        text,
        re.MULTILINE)
    ref_links = []
    for ref_link in ref_link_matches:
        alttext = ref_link[4]
        # Search for yaml in alt-text
        yaml_match = re.findall("({([^}\n]*)})", alttext)
        if len(yaml_match) == 0:
            yaml_data = None
        else:
            yaml_data = yaml_match[-1][1]
            alttext = alttext.replace(yaml_match[-1][0], '')
        if ref_link[2] == '':
            location = 'missing'
        else:
            location = os.path.normpath(ref_link[2])
        ref_links.append({'fullmatch': ref_link[0],
                          'linktext': ref_link[1],
                          'linklocation': location,
                          'alttext': alttext,
                          'yaml': yaml_data})
    return ref_links


def find_buildup_links(text):
    """
    Function to find BuildUp links (links with {} after them)
    Returns a list of dictionaries, one dictionary per link
    """

    links = []
    link_matches = re.findall(
        r'(\[([^]]+?)\](?:\(\s*(\S+)\s*(?:\"([^"]+)\")?\s*\))?{([^:][^}\n]*)})',
        text,
        re.MULTILINE)
    for link in link_matches:
        if link[2] == "":
            linklocation = ""
        else:
            linklocation = os.path.normpath(link[2])
        links.append({'fullmatch': link[0],
                      'linktext': link[1],
                      'linklocation': linklocation,
                      'alttext': link[3],
                      'yaml': link[4]})
    return links


def create_stl_page(stlfile):
    """
    This creates a markdown page for an STL file
    """

    relpath = os.path.relpath(stlfile)
    lpdir, lpname = os.path.split(relpath)
    if lpdir.startswith('..'):
        warn('Included files should be in the project directory')
    lpoutdir = os.path.join(config.out_dir, lpdir)
    make_dir_if_needed(lpoutdir)
    outpath = os.path.join(lpoutdir, lpname)
    if stlfile.endswith('.stl'):
        shutil.copyfile(stlfile, outpath)
        with codecs.open(outpath[:-3] + 'md', "w", "utf-8") as outfile:
            output = u''
            output += f'# {lpname[:-4]}\n\n'
            output += f'[Download STL]({lpname})\n\n'
            outfile.write(output)


class Libraries():
    """
    Class to handle all the part libraries for the documentation

    Note all library names are the file names of the input library
    """

    def __init__(self):
        self.libraries = []

    @property
    def library_names(self):
        """
        This is a property to give a lists of just the library names
        Calling in repeatedly is inefficient as it builds them each time
        """
        return [lib['name'] for lib in self.libraries]

    def get_library(self, library):
        """
        Returns the library dictionary structure of the named library
        """

        # not using self.listed so we don't build library names twice
        lib_names = self.library_names
        if library in lib_names:
            return self.libraries[lib_names.index(library)]['lib']
        return None

    def listed(self, library):
        """
        Checks if there is a library named <library> in the list of
        libraries. Note library names are the input file name
        """
        return library in self.library_names

    def add_library(self, library_file):
        """
        Adds the contents of library_file to the library list if it is not already in there.
        The library dictionary is identified by the file name
        """

        if not self.listed(library_file):
            if os.path.exists(library_file):
                try:
                    with open(library_file, 'r') as stream:
                        partslib = yaml.load(stream, Loader=yaml.SafeLoader)
                        self.libraries.append({'name': library_file, 'lib': partslib})
                        return True
                except BaseException:
                    warn(f"Cannot read library '{library_file}'")
            else:
                warn(f"Cannot find library '{library_file}'")
        return False

    def buildpart(self, library, partname):
        """
        This function makes a markdown page for a part in a library.
        Currently it outputs to file. These jobs should be separated.
        """

        if not self.listed(library):
            added = self.add_library(library)
            if not added:
                # if library couldn't be added we return. Warning generated by
                # add_library
                return

        partslib = self.get_library(library)

        if partname in partslib:
            try:
                part = partslib[partname]
                if 'Name' in part:
                    part_md = f'# {part["Name"]}\n\n'
                else:
                    part_md = f'# {partname}\n\n'

                if "Description" in part:
                    part_md += f'{part["Description"]}\n\n'
                if 'Specs' in part:
                    part_md += f'\n\n## Specifications\n\n|Attribute |Value|\n|---|---|\n'
                    for skey in part['Specs']:
                        part_md += f'|{skey}|{part["Specs"][skey]:}|\n'
                if 'Suppliers' in part:
                    part_md += f'\n\n## Suppliers\n\n|Supplier |Part Number|\n|---|---|\n'
                    for skey in part['Suppliers']:
                        if 'Link' in part["Suppliers"][skey]:
                            link = part["Suppliers"][skey]["Link"]
                        else:
                            link = 'missing'
                        if 'PartNo' in part["Suppliers"][skey]:
                            partno = part["Suppliers"][skey]["PartNo"]
                        else:
                            partno = 'Unknown'
                        part_md += f'|{skey}|[{partno}]({link})|\n'
            except BaseException:
                warn(
                    f"Unexpected error trying to build page for {library}#{part}")

            libdir = re.match(r"^(.+)\.ya?ml$", library).group(1)
            libpath = os.path.join(config.out_dir, libdir)
            if not os.path.isdir(libpath):
                os.mkdir(libpath)
            outfilename = os.path.join(libpath, f"{partname}.md")
            if os.path.exists(outfilename):
                outfilename_rel = os.path.join(libdir, f"{partname}.md")
                warn(
                    f"Overwriting {outfilename_rel}, is this part multiply defined?")
            with codecs.open(outfilename, "w", "utf-8") as outfile:
                outfile.write(part_md)


class Documentation():
    """
    This class represents the documentation in a GitBuilding project
    """

    def __init__(self, conf=None, buildDir=None):

        if buildDir is not None:
            assert isinstance(
                buildDir, str), 'the build directory must be a string'
            config.out_dir = buildDir

        self.settings = {}
        self.config_file = conf
        self.project_data = {
            'Title': None,
            'Authors': [],
            'Email': None,
            'Affiliation': None,
            'License': None,
            'Navigation': None}

        self.licence_dir = os.path.join(os.path.dirname(gb.__file__), 'licenses')
        self.landing = None
        self.pages = []
        self.libs = Libraries()
        self.landing_page = None

    def load_config(self):
        """
        This reads the buildconf.yaml file and populates the both the config object
        and the project_data dictionary
        """

        config_err_msg = "In buildconf.yaml "

        if self.config_file is not None:
            # reading config
            with open(self.config_file, 'r') as stream:
                self.settings = yaml.load(stream, Loader=yaml.SafeLoader)


        # All the settings stuff could do with tidying up, it is becoming a lot
        # of repeated code
        if 'LandingPage' in self.settings:
            self.landing = self.settings['LandingPage']
        if 'CustomCategories' in self.settings:
            if isinstance(self.settings['CustomCategories'], dict):
                # TODO: check all categories have correct reuse info.
                for category in self.settings['CustomCategories']:
                    config.categories[category.lower(
                    )] = self.settings['CustomCategories'][category]
            else:
                warn(f"{config_err_msg}`CustomCategories` should be entered as a dictionary.")
        if 'DefaultCategory' in self.settings:
            if self.settings['DefaultCategory'].lower() in config.categories:
                config.default_category = self.settings['DefaultCategory'].lower(
                )
            else:
                warn(f"{config_err_msg}The default category should be a defined category.")

        if 'Fussy' in self.settings:
            config.fussy = bool(self.settings['Fussy'])
        if 'PageBOMTitle' in self.settings:
            config.page_bom_title = str(self.settings['PageBOMTitle'])
        else:
            config.page_bom_title = ""

        # Project settings

        self.project_data['Homepage'] = self.landing

        if 'Title' in self.settings:
            if isinstance(self.settings['Title'], str):
                self.project_data['Title'] = self.settings['Title']
            else:
                warn(f"{config_err_msg}Title should be a string not "
                     f"a {type(self.project_data['Title'])}")

        if 'Authors' in self.settings:
            if isinstance(self.settings['Authors'], str):
                self.project_data['Authors'] = [self.settings['Authors']]
            elif isinstance(self.settings['Authors'], list):
                self.project_data['Authors'] = []
                for author in self.settings['Authors']:
                    if isinstance(author, str):
                        self.project_data['Authors'].append(author)
                    else:
                        warn(
                            f"{config_err_msg}Each author in Authors should be a string")
            else:
                warn(
                    f"{config_err_msg}Authors should be a list or a string not"
                    f" a {type(self.settings['Authors'])}")
        if 'Email' in self.settings:
            if isinstance(self.settings['Email'], str):
                self.project_data['Email'] = self.settings['Email']
            else:
                warn(
                    f"{config_err_msg}Email must be a string not a {type(self.settings['Email'])}")
        if 'Affiliation' in self.settings:
            if isinstance(self.settings['Affiliation'], str):
                self.project_data['Affiliation'] = self.settings['Affiliation']
            else:
                warn(f"{config_err_msg}Affiliation must be a string not"
                     f" a {type(self.settings['Affiliation'])}")
        if 'License' in self.settings:
            licence = self.settings['License']
            if isinstance(licence, str):
                self.project_data['License'] = licence

                licence_files = os.listdir(self.licence_dir)
                # TODO have a proper licence file look-up not this hack!
                try:

                    def str_simp(string):
                        return string.lower().replace('_', ' ').replace('-', ' ')

                    l_ind = [str_simp(lic)[:-4] for lic in licence_files].index(str_simp(licence))
                    self.project_data['LicenseFile'] = licence_files[l_ind]
                except ValueError:
                    pass

            else:
                warn(f"{config_err_msg}License must be a string not a {type(licence)}")
        if 'HTMLOptions' in self.settings:
            if isinstance(self.settings['HTMLOptions'], dict):
                self.project_data['HTMLOptions'] = self.settings['HTMLOptions']
            else:
                warn(f"{config_err_msg}HTMLOptions must be a dictionary"
                     f" not a {type(self.settings['HTMLOptions'])}")
        if 'Variables' in self.settings:
            if isinstance(self.settings['Variables'], dict):
                self.project_data['Variables'] = self.settings['Variables']
            else:
                warn(f"{config_err_msg}Variables must be a dictionary not"
                     f" a {type(self.settings['Variables'])}")
        if 'Navigation' in self.settings:
            navigation = self.settings['Navigation']
            if valid_navigation(navigation):
                self.project_data['Navigation'] = navigation
            else:
                warn("Couldn't understand navigation. Ignoring!")

    def prepare_directory(self, force=False):
        """
        This function prepares the output directory.
        This includes checking that the directory is the output of GitBuilding.
        This check is because all the data gets deleted and I don't want to delete
        somone's home directory. Maybe there is a better way to do this?
        `force` overrides checking the files in the output folder
        ONLY USE FORCE FOR the server, we don't want people accidentally deleting
        loads of their files!
        """

        if os.path.isdir(config.out_dir):
            curfiles = os.listdir(config.out_dir)
            if curfiles != []:

                if not os.path.exists(os.path.join(
                        config.out_dir, "_data", "project.yaml")):
                    gberror(
                        "Output directory is not empty, and doesn't appear to be a"
                        " valid Git Building output. Empty directory or choose another.",
                        "This a check so we don't delete your files. If you get this"
                        " error try deleting the output directory.")

                with open(os.path.join(config.out_dir, "_data", "project.yaml"), 'r') as stream:
                    curproject = yaml.load(stream, Loader=yaml.SafeLoader)

                if 'FileList' not in curproject:
                    gberror(
                        "Output directory doesn't appear to be a valid Git Building output.",
                        "This a check so we don't delete your files. If you get this error"
                        " try deleting the output directory.")

                outfiles = []
                for root, dirs, files in os.walk(config.out_dir): # pylint: disable=unused-variable
                    for filename in files:
                        if not filename.endswith('project.yaml'):
                            outfiles.append(os.path.relpath(
                                os.path.join(root, filename), start=config.out_dir))
                outfiles.sort()

                # Unless it is forced the GitBuilding will not delete files
                # in the output directory ready to build, unless they
                # match the files that GitBuilding built last time.
                # This way people can't accidentally point GitBuilding at an
                # important directory and delete the contents!
                if not force:
                    if not curproject['FileList'] == outfiles:
                        gberror(
                            "Output directory doesn't appear to be a valid Git Building output.",
                            "This a check so we don't delete your files. If you get this error"
                            " try deleting the output directory.")

                for item in os.listdir(config.out_dir):
                    itempath = os.path.join(config.out_dir, item)
                    if os.path.isdir(itempath):
                        shutil.rmtree(itempath)
                    else:
                        os.remove(itempath)

        else:
            os.mkdir(config.out_dir)
        os.mkdir(os.path.join(config.out_dir, "images"))
        os.mkdir(os.path.join(config.out_dir, "_data"))

    def buildall(self, force=False):
        """
        Builds every page.
        `force` overrides checking the files in the output folder
        ONLY USE FORCE FOR the server, we don't want people accidentally deleting
        loads of their files!
        """

        global activepage
        self.prepare_directory(force)
        self.load_config()
        self.pages = []
        self.libs = Libraries()

        skipdirs = ['./.git']
        for root, dirs, files in os.walk("."):
            # Check if this directory is in a directory to be skipped
            skip = False
            for skipdir in skipdirs:
                if root.startswith(skipdir):
                    skip = True
                    continue
            if skip:
                continue

            # Check if directory contains `_data`
            # If so it is a output directory and should be added to skip list
            if '_data' in dirs:
                skipdirs.append(root)
                continue

            for file in files:
                if file.endswith(".md"):
                    if not os.path.basename(file) in config.exclude:
                        self.pages.append(Page(os.path.relpath(
                            os.path.join(root, file), start="."), self))

        if 'index.md' in self.pages:
            if self.landing is None:
                self.landing = 'index.md'
                self.project_data['Homepage'] = 'index.md'
            elif self.landing != 'index.md':
                warn(f'Landing page is set to {self.landing} but also `index.md` '
                     f'exists. This may cause unreliable behaviour')

        if self.landing in self.pages:
            self.landing_page = self.pages[self.pages.index(self.landing)]
        if self.project_data['Title'] is None:
            if self.landing is None:
                self.project_data['Title'] = "Untitled project"
            else:
                self.project_data['Title'] = self.landing_page.title

        # count parts and find steps on all pages
        for page in self.pages:
            activepage = page.filename
            page.count_page()

        # build step_tree for all pages
        for page in self.pages:
            activepage = page.filename
            page.get_step_tree()

        for page in self.pages:
            activepage = page.filename
            page.count_all()

        for page in self.pages:
            activepage = page.filename
            page.finish_build()

        activepage = ""

        # Create total parts list, the count is meaningless but it is used to
        # know which parts are needed from yaml libraries
        totalpartslist = PartList(AggregateList=True)
        for page in self.pages:
            totalpartslist.merge(page.partlist)

        for part in totalpartslist:
            if part.link is not None:
                # match if the part's link is in the format `abc.yaml#abc` or
                # `abc.yml#abc`
                libmatch = re.match(r"^(.+\.ya?ml)#(.+)$", part.link)
                if libmatch is not None:
                    library = libmatch.group(1)
                    part = libmatch.group(2)
                    self.libs.buildpart(library, part)

        # Add page summary to project data
        self.project_data['PageList'] = []
        for page in self.pages:
            self.project_data['PageList'].append(page.summary())

        if self.project_data['Navigation'] == None:
            self.project_data['Navigation'] = []
            if self.landing_page is not None and len(self.landing_page.steps) > 0:
                for step in self.landing_page.steps:
                    if step in self.pages:
                        self.project_data['Navigation'].append(
                            self.pages[self.pages.index(step)].summary())
            else:
                for page_info in self.project_data['PageList']:
                    if page_info['Link'] != self.landing_page:
                        self.project_data['Navigation'].append(page_info)

        if 'LicenseFile' in self.project_data:
            license_in = os.path.join(self.licence_dir, self.project_data['LicenseFile'])
            license_out = os.path.join(config.out_dir, self.project_data['LicenseFile'])

            with open(license_out, 'w') as outfile, open(license_in, 'r') as licence_file:
                licence_text = licence_file.read()
                licence_text = licence_text.replace(
                    '[year]', str(datetime.datetime.now().year))

                if len(self.project_data['Authors']) > 0:
                    authors = ''
                    for n, author in enumerate(self.project_data['Authors']):
                        if n:
                            if n == len(self.project_data['Authors']) - 1:
                                authors += ', and '
                            else:
                                authors += ', '
                        authors += author
                else:
                    authors = 'Unknown'
                licence_text = licence_text.replace('[fullname]', authors)
                outfile.write(licence_text)

        outfiles = []
        for root, dirs, files in os.walk(config.out_dir):
            for file in files:
                outfiles.append(os.path.relpath(
                    os.path.join(root, file), start=config.out_dir))
        outfiles.sort()
        self.project_data['FileList'] = outfiles

        with open(os.path.join(config.out_dir, "_data", "project.yaml"), 'w') as outfile:
            yaml.dump(self.project_data, outfile, default_flow_style=False)

    def get_log_length(self):
        """
        Returns the length of the warning log
        This function is in Documentation so it can be accessed by the server
        """

        global warninglog
        return len(warninglog)

    def get_log(self, starting=0):
        """
        Returns the warning log entries from `starting` onwards
        This function is in Documentation so it can be accessed by the server
        """

        global warninglog
        return warninglog[starting:]


class Page():
    """
    This class represents one build up page. It can be used to
    track its relation to other pages. To count the parts in the page
    and to export a pure markdown page.
    """

    def __init__(self, filepath, doc, empty=False):
        self.filepath = os.path.relpath(filepath)
        self.pagedir, self.filename = os.path.split(filepath)
        self.doc = doc

        if empty:
            self.raw_text = ""
        else:
            self.raw_text = self.get_raw()
        self.processed_text = ''

        self.partlist = PartList()
        self.all_parts = None
        self.partlinks = []
        self.reflinks = []

        self.steps = []
        self.steplinks = []
        self._step_tree = None

        self.get_title()
        self.reflinks = []

    def rebuild(self, md):
        """
        This is to replace the raw text and rebuild.
        This is used by the live-editor to update a page.
        """

        global activepage
        activepage = self.filename
        self.raw_text = md
        self.processed_text = ''

        self.partlist = PartList()
        self.all_parts = None
        self.partlinks = []
        self.reflinks = []

        self.steps = []
        self.steplinks = []
        self._step_tree = None

        self.get_title()
        self.count_page()
        self.get_step_tree()
        self.count_all()
        result = self.finish_build(tofile=False)
        activepage = ""
        return result

    def save(self, md):
        """
        This saves over the original BuildUp file. It is used by the live editor to save
        changes to the page.
        """
        make_dir_if_needed(self.filepath, isfile=True)
        try:
            with codecs.open(self.filepath, "w", "utf-8") as outfile:
                outfile.write(md)
            return True
        except BaseException:
            return False

    def get_title(self):
        """
        Gets the page title by looking for the first heading with a single #
        """
        headings = re.findall(r'^#(?!#)[ \t]*(.*)$', self.raw_text, re.MULTILINE)

        if len(headings) > 0:
            self.title = headings[0]
        else:
            self.title = ''

    def get_page_steps(self, raw_text):
        """
        Finds h2 headings with yaml info afterwards. Used to locate page steps.
        """

        page_steps = []
        step_ids = []

        # regex:
        # Group 1 (heading[0]) Full match
        # Group 2 (heading[1]) is the heading text
        # Group 3 (heading[2]) is the inline yaml
        headings = re.findall(r'^(##(?!#)[ \t]*(.*)[ \t]*{([^:][^}\n]*)})$', raw_text, re.MULTILINE)
        for heading in headings:
            heading_info = parse_inline_yaml(heading[2])

            if 'pagestep' in heading_info:
                step_id = heading_info['pagestep']
                if step_id is not None:
                    if step_id not in step_ids:
                        step_ids.append(step_id)
                    else:
                        step_id = None
                        warn(f"Step ID {step_id} is already used, ignoring.")
                page_steps.append({'heading': heading[1],
                                   'id': step_id,
                                   'fullmatch': heading[0]})
                del heading_info['pagestep']

            if len(heading_info.keys()) > 0:
                keynames = ''
                for key in heading_info:
                    keynames += key + ', '
                warn(
                    f"Unused keys '{keynames[:-2]}' in heading [{heading[1]}]",
                    fussy=True)
        return page_steps

    def __eq__(self, other):
        """
        Checks for equality using the file name. Used to find pages in lists.
        """
        return self.filepath == other

    def get_raw(self):
        """
        Returns the raw BuildUp file contents.
        """
        try:
            with codecs.open(self.filepath, mode="r", encoding="utf-8") as input_file:
                text = input_file.read()
        except BaseException:
            warn(f"Failed to load a page from {self.filepath}")
            raise
        return text

    def summary(self):
        """
        Page summary used to identify pages for navigation.
        """
        return {'Title': self.title, 'Link': self.filepath}

    def count_page(self):
        """
        Counts all of the part on the page and puts them into a PartList object
        """

        self.reflinks = find_reference_links(self.raw_text)

        for reflink in self.reflinks:
            if not reflink['yaml'] is None:
                rellinklocation = os.path.normpath(
                    os.path.join(self.pagedir, reflink['linklocation']))
                self.partlist.append(
                    Part([reflink['linktext'], rellinklocation, reflink['yaml']]))
        refnames = [reflink['linktext'] for reflink in self.reflinks]

        links = find_buildup_links(self.raw_text)

        # Loop through each part ref
        for link in links:
            if link['linklocation'] == "" and link["linktext"] in refnames:
                link['linklocation'] = self.reflinks[refnames.index(
                    link["linktext"])]['linklocation']
            link_prop = parse_inline_yaml(link['yaml'])
            if link_prop is None:
                warn(
                    f'Broken part reference: "{link["fullmatch"]}" needs fixing.')
            else:
                if 'step' in link_prop and link_prop['step']:
                    if link['linklocation'] == '':
                        warn(
                            f"The link '{link['fullmatch']}' is a step, but links to nowhere.")
                    else:
                        self.steps.append(link['linklocation'])
                    self.steplinks.append(link)
                else:
                    if link['linklocation'] == "":
                        rellinklocation = ""
                    else:
                        rellinklocation = os.path.normpath(
                            os.path.join(self.pagedir, link['linklocation']))
                    self.partlist.countpart(
                        [link["linktext"], rellinklocation, link["yaml"]])
                    self.partlinks.append(link)

        # Once part refs all scanned, if qty for page was undefined initially
        # set to quantity used.
        self.partlist.finishcounting()

        if config.debug:
            print(f"\n\n***** PAGE: {self.title}*****\n")
            for part in self.partlist:
                print(part)

    def count_all(self):
        """
        Creates an aggregate list of parts for the page.
        This aggregate lists if for parts on the page and for any parts in pages
        linked to with a step link. This counting is recursive through step links.
        """

        if self.all_parts is None:
            self.all_parts = PartList(AggregateList=True)
            self.all_parts.merge(self.partlist)
            for step in self.steps:
                if step in self.doc.pages:
                    step_page = self.doc.pages[self.doc.pages.index(step)]
                    step_page.count_all()
                    self.all_parts.merge(step_page.all_parts)

    def finish_build(self, tofile=True):
        """
        Does the final stages of building the output markdown
        and can write it to a file. This is very much a smorgasbord of things
        that need doing. It should be split up.
        """

        self.processed_text = self.raw_text
        # tofile is set to false if you don't want the builds to be produced
        # (this is used in the live preview)
        self.processed_text = replace_ims(
            self.processed_text, replaceall=tofile, page_dir=self.pagedir)
        self.processed_text = replace_stl_links(
            self.processed_text, tofile=tofile, page_dir=self.pagedir)

        # Find {{BOM}} syntax to replace with bill of materials text
        boms = re.findall(r'(\{\{[ \t]*BOM[ \t]*\}\})',
                          self.processed_text, re.MULTILINE)

        # If bill of material is needed for this page, generate the markdown
        # for it
        if len(boms) > 0:
            bom_text = self.all_parts.bom_md(config.page_bom_title)
            extra_reflinks = self.all_parts.partlinkmd(
                excludelist=self.partlist)
            if len(extra_reflinks) > 0:
                self.processed_text += '\n\n' + extra_reflinks

        # Place bill of materials into page
        for bom in boms:
            self.processed_text = self.processed_text.replace(bom, bom_text)

        # Find {{BOMlink}} syntax to replace with link to Bill of materials
        # page
        bom_links = re.findall(r'(\{\{[ \t]*BOMlink[ \t]*\}\})',
                               self.processed_text, re.MULTILINE)

        # If bill of material is needed for this page, generate the markdown
        # for it
        if len(bom_links) > 0:
            bom_page_name = self.make_bom_page()

        # Place bill of materials into page
        for bomlink in bom_links:
            self.processed_text = self.processed_text.replace(
                bomlink, f"[bill of materials]({bom_page_name})")

        page_steps = self.get_page_steps(self.processed_text)

        for n, page_step in enumerate(page_steps):
            kramdown_block = "{:"
            if page_step['id'] is not None:
                kramdown_block += f'id="{page_step["id"]}" '
            kramdown_block += 'class="page-step"}'
            self.processed_text = self.processed_text.replace(
                page_step['fullmatch'],
                f"## Step {n+1}: {page_step['heading']} {kramdown_block}")

        for link in self.steplinks:
            if link["linktext"] == '.' and link["linklocation"] in self.doc.pages:
                linktext = self.doc.pages[self.doc.pages.index(
                    link["linklocation"])].title
            else:
                linktext = link["linktext"]
            if link["linklocation"] == '':
                self.processed_text = self.processed_text.replace(
                    link['fullmatch'], f'[{linktext}]')
            else:
                self.processed_text = self.processed_text.replace(
                    link['fullmatch'],
                    f'[{linktext}]({link["linklocation"]} "{link["alttext"]}")')

        for link in self.partlinks:
            rep_text = f'[{link["linktext"]}]'
            part = self.partlist.getpart(link["linktext"])
            if part is not None:
                if part.link in [None, '', 'missing']:
                    rep_text += '{: Class="missing"}'
            self.processed_text = self.processed_text.replace(
                link['fullmatch'], rep_text)

        # make page for directly linked stls
        for link in self.partlist.links():
            if link.endswith('.stl'):
                if os.path.exists(link):
                    create_stl_page(link)
                else:
                    warn(f'Cannot find {link}')

        # process reflinks
        for reflink in self.reflinks:
            location = reflink["linklocation"]
            if location.endswith('.stl'):
                location = location[:-3] + "md"
            libpartmatch = re.match(r"^(.+)\.ya?ml#(.+)$", location)
            if libpartmatch is not None:
                location = os.path.join(
                    libpartmatch.group(1),
                    libpartmatch.group(2) + ".md")
            clean_reflink = f'[{reflink["linktext"]}]:{location} "{reflink["alttext"]}"'
            self.processed_text = self.processed_text.replace(
                reflink['fullmatch'], clean_reflink)

        # Add reference style link for anything that doesn't have one
        for part in self.partlist:
            refnames = [reflink['linktext'] for reflink in self.reflinks]
            if part.name not in refnames:
                self.processed_text += "\n" + part.reflinkmd()

        if tofile:
            outfilename = os.path.join(config.out_dir, self.filepath)
            make_dir_if_needed(outfilename, isfile=True)
            # Write to file in Output folder
            with codecs.open(outfilename, "w", "utf-8") as outfile:
                outfile.write(self.processed_text)
            return None
        return self.processed_text

    def get_step_tree(self, breadcrumbs=None):
        """
        This function traverses the steps in the page to create a complete downward step tree
        it uses the same function of other steps until all pages downstream have completed.
        Checking for loops in the step definition stops infinite loops occurring.
        """
        if self._step_tree is None:
            if breadcrumbs is None:
                breadcrumbs = [self.filepath]
            else:
                if self.filepath in breadcrumbs:
                    gberror(f"The step in this document form a loop!",
                            str(breadcrumbs))
                breadcrumbs.append(self.filepath)
            outlist = []
            if self.steps != []:
                for step in self.steps:
                    if step in self.doc.pages:
                        step_page = self.doc.pages[self.doc.pages.index(step)]
                        outlist.append(step_page.get_step_tree(breadcrumbs))
                    else:
                        warn(f'Missing instructions {step}')
            self._step_tree = {self.filepath: outlist}
        return self._step_tree

    def make_bom_page(self):
        """
        Makes separate Bill of materials page for the all parts on this page (including those
        in steps). Returns the file path of the resulting file.
        """
        output = u''
        # Bill of material markdown
        output += self.all_parts.bom_md("# Bill of Materials", reflinks=True)
        filename = self.filepath[:-3] + "_BOM.md"
        bom_filename = os.path.join(config.out_dir, self.pagedir, filename)
        with codecs.open(bom_filename, "w", "utf-8") as outfile:
            outfile.write(output)
        return filename


def add_quantities(q1, q2):
    """
    This function adds two quantities of any class.
    This is done by trying it's level best to add them and if it fails it
    returns the string "Some"
    """

    if q1 is None:
        return q2
    if q2 is None:
        return q1

    # This is horrible!
    try:
        return q1 + q2
    except BaseException:
        pass
    try:
        return q2 + q1
    except BaseException:
        pass
    try:
        return q1 + type(q1)(q2)
    except BaseException:
        pass
    try:
        return q2 + type(q2)(q1)
    except BaseException:
        return 'Some'


def largest_quantity(q1, q2):
    """
    This function finds the maximum of two quantities of any class.
    This is done by trying it's level best compare them and if it fails it
    returns the string "Some"
    """
    if q1 is None:
        return q2
    if q2 is None:
        return q1

    # This is also horrible!
    try:
        return max(q1, q2)
    except BaseException:
        pass
    try:
        return max(q2, q1)
    except BaseException:
        pass
    try:
        return max(q1, type(q1)(q2))
    except BaseException:
        pass
    try:
        return max(q2, type(q2)(q1))
    except BaseException:
        return 'Some'


class Part():
    """
    This module handles a particular part such as "M3x6mm Cap Head Screws".
    It handles counting the quantity of the part used, its category, and notes
    about usage etc.
    """

    def __init__(self, info, indexed=True):
        self.valid = True
        # An indexed part is one that has been added to a partlist
        self.indexed = indexed
        self.name = info[0]
        # set Part defaults
        self.link = None
        self.cat = config.default_category
        self.reuse = False
        # None for total quantity would mean that no total is defined and it is
        # calculated from number used
        self.total_qty = None
        # qty_used is set as None because type has not yet been set
        self.qty_used = None
        self.note = None

        self.construct_part(info[1], info[2])

    def construct_part(self, partlink, partyaml):
        """
        Strips the important part information from the data in a buildup file
        """

        if partyaml != '':
            part_info = parse_inline_yaml(partyaml)
            if part_info is None:
                warn('Cannot parse {%s}.' % partyaml)
                self.valid = False
                return
        else:
            part_info = dict()

        # Set link
        if not partlink == '':
            partlink = os.path.normpath(partlink)
            if not os.path.isabs(partlink):
                if partlink.startswith('..'):
                    warn(f'Link to "{partlink}" removed as path must be within documentation dir')
                else:
                    self.link = partlink
            else:
                warn(
                    f'Link to "{partlink}" removed as only relative paths are supported')

        # interpret YAML differently for reference style links or links in the
        # text
        if self.indexed:
            # if Qty not defined or set as ?, leave qty as None
            if 'totalqty' in part_info:
                self.total_qty = part_info['totalqty']
                del part_info['totalqty']
            if 'cat' in part_info:
                if part_info['cat'].lower() in config.categories:
                    self.cat = part_info['cat'].lower()
                    self.reuse = config.categories[self.cat]['Reuse']
                else:
                    warn(
                        f"No valid category {part_info['cat']}. You can define custom categories"
                        " in the config file.")
                del part_info['cat']
            if 'note' in part_info:
                if isinstance(part_info['note'], str):
                    self.note = part_info['note']
                else:
                    warn(
                        f"Ignoring the Note '{part_info['note']}' I expected a string not"
                        f" a {type(part_info['note'])}.")
                del part_info['note']
        else:
            if 'qty' in part_info:
                self.qty_used = part_info['qty']
            else:
                self.valid = False
                warn(
                    f"Part link without quantity [{self.name}]. This will be ignored")
                return
            del part_info['qty']
        if len(part_info.keys()) > 0:
            keynames = ''
            for key in part_info:
                keynames += key + ', '
            warn(
                f"Unused keys '{keynames[:-2]}' in part [{self.name}]",
                fussy=True)

    def __eq__(self, obj):
        """
        Checks is two parts are equal.
        This one is super complicated as it depends on what is being compared:
        * String input checks the name.
        * If both parts are indexed (i.e. on part lists) then they are from different
          pages in the documentation. These need to be checked carefully to avoid clashes
          between parts on different pages in a total Bill of Materials
        * If only one part is indexed (on a part list) then the check is within a page
        More details about how the checks are done is in the comments of the function
        """

        if isinstance(obj, str):
            return obj == self.name
        if isinstance(obj, Part):
            # Check type depends on if an indexed part (one in a PartList) is
            # compared to another indexed part or one not yet indexed (see
            # below)
            check_type = self.indexed + obj.indexed
            assert check_type in [1, 2], "Part comparison failed, are you trying to compare two non-indexed Parts?"

            if check_type == 1:
                # Non indexed part compared to an indexed one.
                # This will be for checking whether to increment the parts used or to
                # index the part as a new part
                # Categories don't need to match here as using "qty" for a part
                # to be counted shouldn't set the category

                if self.name != obj.name:
                    # names must match
                    return False

                if self.link == obj.link:
                    # categories, names and links match
                    return True

                if obj.link is None or self.link is None:
                    return True

                warn(f"Parts on same page have the same name: '{obj.name}'"
                     f" and different links [{self.link}, {obj.link}]. "
                     f"This may cause weird Bill of Materials issues.")
                return False

            #This is check_type 2
            # comparing two parts already in parts lists on different
            # pages.

            # categories must match
            if self.cat != obj.cat:
                # names must match
                return False

            if (self.link is not None) and (obj.link is not None):
                # If links match then they are referring to the same part
                if self.link == obj.link:
                    if self.name != obj.name:
                        if self.link == 'missing':
                            # If two parts don't have links they can be
                            # ignored
                            return False
                        warn(f"Two have same link '{obj.link}' and different names "
                             f"[{self.name}, {obj.name}]. One name will be picked for"
                             f" the total Bill of Materials."
                             f"You can ignore fussy warnings by editing your config",
                             fussy=True)
                    return True
                return False
            # if either link is None check name
            if self.name == obj.name:
                # items with the same name is a match if at least one
                # link is None
                return True
        return False

    def __str__(self):
        return f'''{self.name:}
    link:      {self.link}
    category:  {self.cat}
    reuse:     {self.reuse}
    Total Qty: {self.total_qty}
    Qty Used:  {self.qty_used}
'''

    def combine(self, part):
        """
        Combines two parts of the same part
        Combine is different from counting, combine is the operation when two lists are merged
        as such all parts should be indexed (i.e. on parts lists)
        """

        assert isinstance(part, Part), "Can only add a Part to a Part"
        assert self.indexed, "Part must be indexed to be added to"
        assert part.indexed, "Can only add indexed parts"
        assert part == self, "Parts must match to be added"

        if self.reuse:
            self.qty_used = largest_quantity(self.qty_used, part.qty_used)
        else:
            self.qty_used = add_quantities(self.qty_used, part.qty_used)

        if self.reuse:
            self.total_qty = largest_quantity(self.total_qty, part.total_qty)
        else:
            self.total_qty = add_quantities(self.total_qty, part.total_qty)

        if self.note is None:
            self.note = part.note
        elif part.note is not None:
            self.note += '  ' + part.note

    def count(self, part):
        """
        Counts more of the same part on a page. This is not used when merging two lists of parts
        for merging lists see combine
        """

        assert self.indexed, "Only indexed parts can count other parts"
        assert not part.indexed, "Can only count non indexed parts"

        if self.qty_used is None:
            self.qty_used = part.qty_used
        else:
            if self.reuse:
                self.qty_used = largest_quantity(self.qty_used, part.qty_used)
            else:
                self.qty_used = add_quantities(self.qty_used, part.qty_used)

    def reflinkmd(self):
        """
        Creates the reference link for this part.
        """

        if self.link is None:
            link = 'missing'
        elif self.link.endswith('.stl'):
            link = self.link[:-3] + 'md'
        else:
            libpartmatch = re.match(r"^(.+)\.ya?ml#(.+)$", self.link)
            if libpartmatch is not None:
                link = os.path.join(libpartmatch.group(
                    1), libpartmatch.group(2) + ".md")
            else:
                link = self.link
        return f'[{self.name}]:{link}'


class PartList():
    """
    PartLists are lists of Part objects. They have functions that allow them to
    safely add parts and to be merged.
    Lists start of not "counted". Once all parts in a page have been added into the list
      it can be "counted" to create total quantities for each part
    Lists can also be created as Aggregate lists, these are used to merge multiple lists
      together for making total bills of materials.
    The main reasons for this distinction is so that the software can separate information
    that is assumed from information that is read. Assumptions are then made when the list
    is counted.
    """

    def __init__(self, AggregateList=False):
        # aggregate lists are summed lists, a non aggregate list cannot become
        # an aggregate
        self.aggregate = AggregateList
        # All aggregate lists are counted, normal lists should be counted before
        # merging into aggregates or calculating a bill of materials
        self.counted = AggregateList
        self.parts = []

    def __getitem__(self, ind):
        return self.parts[ind]

    def __setitem__(self, ind, part):
        assert isinstance(
            part, Part), "Can only store Part objects in a PartList"
        self.parts[ind] = part

    def __len__(self):
        return len(self.parts)

    def append(self, part):
        """
        Appends a new part into the list, this is only done by `countpart` and `merge`
        """

        assert isinstance(part, Part), "Can only append Part objects to a PartList"
        # TODO: Check if parts clash

        # If there was a yaml error the part is not valid and wont be appended
        if part.valid:
            self.parts.append(deepcopy(part))

    def index(self, part):
        """
        Works as index for a list but uses the __eq__ method of Part objects
        in the part list
        """
        return self.parts.index(part)

    def getpart(self, part):
        """
        Returns the part object from the list that matches input "part"
        uses the __eq__ method of Parts, so this input could be a Part
        object or a string
        """
        try:
            return self.parts[self.index(part)]
        except ValueError:
            return None

    def merge(self, inputlist):
        """
        If this is an aggregate list then it merges in another partlist
        """
        assert isinstance(
            inputlist, PartList), "Can only merge a PartList to another PartList"
        assert self.aggregate, "Only aggregate lists can merge other lists into them"
        assert inputlist.counted, "List must be counted before being merged into an aggregate"
        for part in inputlist:
            if part in self:
                ind = self.parts.index(part)
                self[ind].combine(part)
            else:
                self.append(part)

    def countpart(self, info):
        """
        Takes the information for another part and counts it.
        If the part already exists then counting rules are used to add the quantities
        If it doesn't exist we append it
        """
        assert not self.counted, "Cannot count part, counting has finished"
        part = Part(info, indexed=False)
        if part.valid:
            # if the part is already listed, update quantites
            if part in self.parts:
                ind = self.parts.index(part)
                self[ind].count(part)
            else:
                part.indexed = True
                self.append(part)

    def finishcounting(self):
        """
        Calculates the total quantities for each part on the list and
        then marks the list as "counted"
        """
        if self.counted:
            return
        # once counting is finished, if the total quantity was undefined set it
        # to the quantity used
        for part in self.parts:
            if part.total_qty is None:
                part.total_qty = part.qty_used
            if not part.total_qty == part.qty_used:
                warn(f"{part.name} has a total quantity of {part.total_qty}"
                     f" specified but only {part.qty_used} are used.",
                     fussy=True)
        self.counted = True

    def partlinkmd(self, excludelist=None):
        "Returns the markdown down for the links to each part. Each part on a new line"
        linktext = u''

        for part in self.parts:
            if (excludelist is not None) and (part not in excludelist):
                linktext += f'{part.reflinkmd()}\n'
        return linktext

    def links(self):
        """
        Returns the a list of of links to each part
        """
        links = []
        for part in self.parts:
            if part.link is not None:
                links.append(part.link)
        return links

    def bom_md(self, title, divide=True, reflinks=False):
        """
        Creates the bill of materials in markdown format.
        Can set whether it also includes the reference links for each
        part, and whether they are divided by categories
        """

        #TODO: Made divide=False work (no categories)
        assert self.counted, "Cannot calculate bill of materials for uncounted partlist."
        bom_text = ''
        if title != "":
            bom_text += f'{title}\n\n'
        # Loop through parts and put quantities and names in/
        for cat in config.categories:
            if "DisplayName" in config.categories[cat]:
                catname = config.categories[cat]["DisplayName"]
            else:
                catname = cat
            first = True
            for part in self.parts:
                if part.cat == cat:
                    appended_class = ''
                    if first:
                        first = False
                        bom_text += f'\n\n### {catname}\n\n'

                    if part.total_qty is None:
                        continue
                    if isinstance(part.total_qty, int):
                        qty_str = str(part.total_qty) + ' x '
                    elif isinstance(part.total_qty, float):
                        qty_str = str(part.total_qty) + ' of '
                    else:
                        qty_str = str(part.total_qty)

                    if part.link in [None, '', 'missing']:
                        appended_class = '{: Class="missing"}'

                    if part.note is None:
                        note_txt = ''
                    else:
                        note_txt = '  ' + part.note
                    bom_text += f'* {qty_str} [{part.name}]{appended_class} {note_txt}\n'
        if reflinks:
            for part in self.parts:
                bom_text += self.partlinkmd()
        return bom_text
