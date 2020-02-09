from datetime import datetime

from jezdzenka.classes.Pkpass import Pkpass, Special
from jezdzenka.console.forms import new_empty_prompt, type_prompt
from jezdzenka.database import collection
from jezdzenka.database.manipulation import add_new_from_form, update_object


def create(args):
    pkp = Pkpass(args.new)
    if pkp.is_valid():
        transit = Special(pkp.copied_data, pkp.get_type()[1])
        information = new_empty_prompt({'description': '', 'tags': []})
        information.update(transit.special_data(pkp.regular_data(), pkp.get_special_values()))
        add_new_from_form(information, args.new)
    else:
        type = type_prompt()
        information = new_empty_prompt({
            'id': '', 'description': '', 'organization': '', 'relevant_date': datetime.now(), 'colour': '', 'tags': []
        })
        information.update(type)
        add_new_from_form(information, args.new)


def modify(args):
    element = dict(collection.get_object_by_id(args.modify))
    del element['filename']
    del element['archived']
    element = new_empty_prompt(element)
    update_object(args.modify, element)