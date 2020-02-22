import logging
import os
import subprocess
import sys

import ruamel.yaml

from . import Collection, Entry, TemplatingError


def edit_file_in_external_editor(filepath):
    # First we try to use $EDITOR
    try:
        editor = os.environ['EDITOR']
        subprocess.call([editor, filepath])
    except FileNotFoundError as e:
        if editor in str(e):
            logging.info(
                'Could not open file {} with $EDITOR (currently {})'.format(
                    filepath,
                    editor
                    )
                )
        else:
            logging.warning("Could not open file {}".format(filepath))
            return False
    else:
        return True
    # then we try to use sensible-editor (which should be available on
    # debian and derivatives)
    try:
        subprocess.call(['sensible-editor', filepath])
    except FileNotFoundError as e:
        if 'sensible-editor' in e.strerror:
            logging.debug(
                "Could not open file {} with editor: sensible-editor".format(
                    filepath
                    )
                )
        else:
            logging.warning("Could not open file {}".format(filepath))
            return False
    else:
        return True
    # and finally we fallback to vi, because ed is the standard editor,
    # but that would be way too cruel, and vi is also in posix
    try:
        subprocess.call(['vi', filepath])
    except FileNotFoundError as e:
        if 'vi' in e.strerror:
            logging.warning(
                "Could not open file {} with any known editor".format(filepath)
                )
            return False
        else:
            logging.warning("Could not open file {}".format(filepath))
            return False
    else:
        return True


class Command():
    help = ''

    def _main(self, args):
        self.args = args
        self.main()


class New(Command):
    arguments = [
        (['--collection', '-c'], dict(
            help='The collection to work on (default .)'
            )),
        (['--no-git'], dict(
            help="Don't add the new entry to git",
            action="store_false",
            dest='git'
            )),
        ]

    def main(self):
        collection = Collection(self.args.collection)
        new_entry = Entry(collection)
        collection.save_entries([new_entry])
        filepath = os.path.join(
            collection.itemdir,
            new_entry.fname
            )
        if edit_file_in_external_editor(filepath):
            collection.update_cache([filepath])
            if self.args.git:
                collection.git_add_files([filepath])
        saved_entry = collection.entry_from_eid(new_entry.eid)
        print(saved_entry)


class Edit(Command):
    arguments = [
        (['--collection', '-c'], dict(
            help='The collection to work on (default .)'
            )),
        (['--no-git'], dict(
            help="Don't add the new entry to git",
            action="store_false",
            dest='git'
            )),
        (['eid'], dict(
            help='eid of an entry to edit',
            )),
        ]

    def main(self):
        collection = Collection(self.args.collection)
        entries = collection.entries_from_short_eid(self.args.eid)
        if len(entries) > 1:
            return "{} is not an unique eid".format(self.args.eid)
        if not entries:
            return "Could not find an entry with eid starting with: {}".format(
                self.args.eid
                )
        entry = entries[0]
        filepath = os.path.join(
            collection.itemdir,
            entry.fname
            )
        if edit_file_in_external_editor(filepath):
            collection.update_cache([filepath])
            if self.args.git:
                collection.git_add_files([filepath])
        saved_entry = collection.entry_from_eid(entry.eid)
        print(saved_entry)


class Show(Command):
    arguments = [
        (['--collection', '-c'], dict(
            help='The collection to work on (default .)'
            )),
        (['--template', '-t'], dict(
            help='Use the specified template to display results.',
            )),
        (['eid'], dict(
            help='eid of an entry to edit',
            )),
        ]

    def main(self):
        collection = Collection(self.args.collection)
        entries = collection.entries_from_short_eid(self.args.eid)
        if len(entries) > 1:
            return "{} is not an unique eid".format(self.args.eid)
        if not entries:
            return "Could not find an entry with eid starting with: {}".format(
                self.args.eid
                )
        entry = entries[0]
        if self.args.template:
            try:
                print(entry.render(self.args.template))
            except TemplatingError as e:
                logging.error("{}".format(e))
                sys.exit(1)
        else:
            print(entry.yaml_data)


class Index(Command):
    arguments = [
        (['--collection', '-c'], dict(
            help='The collection to work on (default .)'
            )),
        (['files'], dict(
            help='List of files to index (default: everything)',
            default=None,
            nargs='*',
            )),
        ]

    def main(self):
        collection = Collection(self.args.collection)
        if self.args.files:
            files = (os.path.basename(f) for f in self.args.files)
        else:
            files = None
        indexed = collection.update_cache(fnames=files)
        print("Found and indexed {} entries".format(indexed))


class Search(Command):
    arguments = [
        (['--collection', '-c'], dict(
            help='The collection to work on (default .)'
            )),
        (['--template', '-t'], dict(
            help='Template to use when displaying results',
            )),
        (['--offset'], dict(
            type=int,
            )),
        (['--pagesize'], dict(
            type=int,
            )),
        (['--all'], dict(
            action='store_true',
            help='Return all available results'
            )),
        (['query'], dict(
            help='Xapian query to search in the collection',
            nargs='+'
            )),
        ]

    def main(self):
        # TODO: implement "searching" for everything
        if self.args.offset:
            logging.warning(
                "offset exposes an internal knob and MAY BE" +
                " REMOVED from a future release of lesana"
                )
        if self.args.pagesize:
            logging.warning(
                "pagesize exposes an internal knob and MAY BE" +
                " REMOVED from a future release of lesana"
                )
        offset = self.args.offset or 0
        pagesize = self.args.pagesize or 12
        collection = Collection(self.args.collection)
        if self.args.query == ['*']:
            results = collection.get_all_documents()
        else:
            collection.start_search(' '.join(self.args.query))
            if self.args.all:
                results = collection.get_all_search_results()
            else:
                results = collection.get_search_results(
                    offset,
                    pagesize)
        if self.args.template:
            try:
                template = collection.get_template(self.args.template)
                print(template.render(entries=results))
            except TemplatingError as e:
                logging.error("{}".format(e))
                sys.exit(1)
        else:
            for entry in results:
                print("{entry}".format(
                    entry=entry,
                    ))


class Export(Command):
    arguments = [
        (['--collection', '-c'], dict(
            help='The collection to work on (default .)'
            )),
        (['--query', '-q'], dict(
            help='Xapian query to search in the collection',
            )),
        (['destination'], dict(
            help='The collection to export entries to'
            )),
        (['template'], dict(
            help='Template to convert entries',
            )),
        ]

    def main(self):
        collection = Collection(self.args.collection)
        destination = Collection(self.args.destination)
        if not self.args.query:
            results = collection.get_all_documents()
        else:
            collection.start_search(' '.join(self.args.query))
            results = collection.get_all_search_results()
        for entry in results:
            try:
                template = collection.get_template(self.args.template)
                rendered = template.render(entry=entry, **entry.data)
            except TemplatingError as e:
                logging.error("Error converting entry: {}".format(entry))
                logging.error("{}".format(e))
                sys.exit(1)
            try:
                data = ruamel.yaml.load(rendered, ruamel.yaml.RoundTripLoader)
            except ruamel.yaml.YAMLError as e:
                logging.error("Error converting entry: {}".format(entry))
                logging.error("{}".format(e))
                sys.exit(1)
            e = Entry(destination, data=data)
            destination.save_entries([e])


class Init(Command):
    arguments = [
        (['--collection', '-c'], dict(
            help='The directory to work on (default .)',
            default='.'
            )),
        (['--no-git'], dict(
            help='Skip setting up git in this directory',
            action="store_false",
            dest='git'
            )),
        ]

    def main(self):
        Collection.init(
            self.args.collection,
            git_enabled=self.args.git,
            edit_file=edit_file_in_external_editor
            )


class Remove(Command):
    arguments = [
        (['--collection', '-c'], dict(
            help='The collection to work on (default .)',
            )),
        (['entries'], dict(
            help='List of entries to remove',
            nargs='+',
            )),
        ]

    def main(self):
        collection = Collection(self.args.collection)
        collection.remove_entries(eids=self.args.entries)
