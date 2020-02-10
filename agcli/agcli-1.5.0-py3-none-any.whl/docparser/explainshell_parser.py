import urllib3
import certifi
from . import docparser
from html.parser import HTMLParser

class ExplainShellParser(docparser.DocParser):

    def __init__(self, cmd):
        """
        The 'ca_certs' arg allow to indicate where the certificate for https
        connection are stored. These certificate are located thanks to the
        "certifi.where()" function call.
        """
        self._http = urllib3.PoolManager(ca_certs=certifi.where())
        self._links_extractor = LinksExtractor()
        self._option_block_extractor = OptionsBlockExtractor()
        super().__init__(cmd)
        self._links_extractor.close()
        self._option_block_extractor.close()

    def get_command_doc(self):
        try:
            cmd_arg = self.cmd.replace(' ','+')
            r = self._http.request('GET', 'https://explainshell.com/explain?cmd='+cmd_arg)
            self._links_extractor.feed(r.data.decode('utf-8'))
            links = self._links_extractor.links
            for link in links:
                if "explain/" in link and self.cmd.replace(' ', '-') in link:
                    r = self._http.request('GET', 'https://explainshell.com/'+link)
                    return r.data.decode('utf-8')
            raise docparser.ExplainShellError(self.cmd)
            # if there is no link that match that, this is en error page
        except urllib3.exceptions.MaxRetryError as e:
            raise docparser.ExplainShellConnexionError()

    def parse(self, doc):
        self._option_block_extractor.feed(doc)
        option_list = []
        for option_block in self._option_block_extractor.option_blocks:
            current_option = {}
            for subblock in self._get_subblock(option_block):
                self._process_names(subblock, current_option)
                self._process_help(subblock, current_option)
            if len(current_option) > 0:
                option_list.append(current_option)
        self.options = option_list
        self.add_ID()
        self.format_help()

    def _get_subblock(self, option_block):
        """
        Split an option block in different subblocks to handle options written
        in several blocks.
        """
        subblocks = option_block.split('\n')
        option_subblocks = []
        for subblock in subblocks:
            #subblock = subblock.strip()
            if subblock.startswith('-') or len(subblock.split(' ')[0]) == 1:
                #First word of the block means an option
                option_subblocks.append(subblock)
            elif not len(option_subblocks)==0 :
                #Skip subtitle and stick rebuild the help block of the option
                option_subblocks[-1] += '  ' + subblock.strip()
        return option_subblocks

    def _delete_space_block(self, string):
        """
        Delete space block in the help text due to removal of line return
         and tabulation.
        """
        string_list = []
        for line in string.split('\n'):
            string_list.append(line.strip())
        new_string = ' '.join(string_list)
        return new_string

    def _process_names(self, option_block, current_option):
        """
        Extract the name from an option subblock
        """
        names = option_block.split('  ')[0].replace('[', '').replace(']', '')
        name_dict = {}
        for name in names.split(','):
            name = name.strip()
            if '=' in name:
                arg_dict = self._extract_option_argument(name, '=')
            else:
                arg_dict = self._extract_option_argument(name, ' ')
            docparser.update_parameter(name_dict, arg_dict)
        docparser.update_parameter(current_option, name_dict)
        #current_option.update(name_dict)

    def _extract_option_argument(self, str_line, separator):
        """
        Extract the argument of an option subblock if it exists.
        """
        string_list = str_line.split(separator)
        if len(string_list) == 1:
            return {'names': [string_list[0].strip()]}
        else:
            arg = string_list[1].replace('<', '').replace('>', '')
            return {
                    'names': [string_list[0].strip()],
                    'argument_name': arg, 'default_value': []
                    }

    def _process_help(self, option_block, current_option):
        """
        Extract the help message from the option subblock
        """
        _help = self._delete_space_block(' '.join(option_block.split('  ')[1:]))
        _help = _help.replace('\\', '').replace('\n', '')
        if _help == '' and 'argument_name' in current_option:
            _help = option_block.split(current_option['argument_name'])[-1]
        if 'help' in current_option:
            #Do not stick 2 helps together if they belongs to 2 different name
            current_option['help'] += "\n\n"

        current_option['help'] = current_option.get('help', '') + _help.strip()


class LinksExtractor(HTMLParser):

    def __init__(self):
        self.links = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            name, value = attrs[0]
            if name == 'href':
                self.links.append(value)

class OptionsBlockExtractor(HTMLParser):

    def __init__(self):
        self.option_blocks = []
        self.is_option_block = False
        self.current_block = ''
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == 'pre':
            self.is_option_block = True

    def handle_data(self, data):
        if self.is_option_block:
            self.current_block += data

    def handle_endtag(self, tag):
        if tag == 'pre':
            self.is_option_block = False
            self.option_blocks.append(self.current_block)
            self.current_block = ''
