import re
from dynamodb_python_lib.utilities.synonym_map import *

ENTITY_VALUE_COLUMN = "entity_value"
ENTITY_CLASS_COLUMN = "entity_class"
ENTITY_START_COLUMN = "entity_start_index"


def get_synonym_map(category: str) -> dict:
    if category not in map_data:
        return {}
    synonym_map = map_data.get(category)["enumerationValues"]

    temp_values = []
    temp_synonyms = []
    temp_dict = {}
    for item in synonym_map:
        temp_dict.update(item)
        temp_values.append(temp_dict["value"].upper())
        temp_synonyms.append(temp_dict["synonyms"])
    synonym_map = dict(zip(temp_values, temp_synonyms))
    return synonym_map


LODGING_MAP = get_synonym_map("LodgingAmenities")
FLIGHT_MAP = get_synonym_map("FlightAmenities")


def execute(text: str, product: str):
    entity_values = []
    entity_classes = []
    entity_start_indices = []
    entity_end_indices = []

    data = {
        ENTITY_VALUE_COLUMN: "",
        ENTITY_CLASS_COLUMN: "",
        ENTITY_START_COLUMN: ""
    }

    if product == "flight":
        synonyms = FLIGHT_MAP
    elif product == "lodging":
        synonyms = LODGING_MAP
    else:
        return data

    for key in synonyms:
        for term in synonyms[key]:
            # regex to capture term with word boundaries
            my_regex = r"\b" + re.escape(term) + r"\b"
            re_term = re.compile(my_regex, re.IGNORECASE)

            for m in re.finditer(re_term, text):
                if m.start() not in entity_start_indices and m.end() not in entity_end_indices:
                    entity_values.append(m.group(0))
                    entity_classes.append(key.upper())
                    entity_start_indices.append(m.start())
                    entity_end_indices.append(m.end())

    if len(entity_start_indices) > 1:
        zipped = sorted(zip(entity_start_indices, entity_values, entity_classes), key=lambda x: x[0])
        entity_start_indices, entity_values, entity_classes = list(zip(*zipped))

    values = ""
    classes = ""
    indices = ""
    fill_count = 0
    for ev, ec, esi in zip(entity_values, entity_classes, entity_start_indices):
        if fill_count == 0:
            values += ev
            classes += ec
            indices += str(esi)
        else:
            values += "|" + ev
            classes += "|" + ec
            indices += "|" + str(esi)
        fill_count = fill_count + 1

    data[ENTITY_VALUE_COLUMN] = values
    data[ENTITY_CLASS_COLUMN] = classes
    data[ENTITY_START_COLUMN] = indices

    return data
