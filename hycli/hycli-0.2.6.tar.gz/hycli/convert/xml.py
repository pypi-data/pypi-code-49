import xmltodict

from ..services.requests import extract_invoice, validate_vat, validation
from .commons import read_pdf


def convert_to_xml(
    path,
    output_path,
    extractor_endpoint,
    vat_validator_endpoint=None,
    validation_endpoint=None,
    token=None,
):
    result = {}
    _, pdf = read_pdf(path)

    # Extraction
    _, result["invoiceExtractor"] = extract_invoice(
        (path, pdf), extractor_endpoint, "application/pdf", token
    )

    # Validation
    if validation_endpoint:
        validation(result, validation_endpoint)

    # Vat validation
    if vat_validator_endpoint:
        validate_vat(result, vat_validator_endpoint)

    merge_validation(result)
    clean_datastructure(result)

    file_name = path.split("/")[-1]
    file_name = file_name.split(".")[0]
    xmltodict.unparse(
        {"hypatosResults": result},
        output=open(f"{output_path}/{file_name}.xml", "w+"),
        pretty=True,
    )


def merge_validation(result):
    return_dict = {}

    def traverse_merge_items(entities, _dict, *validation):
        for entity, value in entities.items():
            if isinstance(value, dict):
                _dict[entity] = {}
                traverse_merge_items(
                    entities[entity],
                    _dict[entity],
                    validation[0][entity][0] if validation else None,
                )
            elif isinstance(value, list):
                _dict[entity] = []
                for idx in range(0, len(value)):
                    # Try hack when there is a validation error for a item and previous has not.
                    try:
                        _dict[entity].append({})
                        traverse_merge_items(
                            entities[entity][idx],
                            _dict[entity][idx],
                            validation[0][entity][0][str(idx)][0]
                            if validation[0] and entity in validation[0]
                            else None,
                        )
                    except (KeyError, IndexError):
                        _dict[entity].pop(-1)
            else:
                if validation[0] and entity in validation[0]:
                    # Entity was in validation schema and has errors
                    if str(validation[0][entity][0]) != "unknown field":
                        _dict[entity] = {
                            "@risk": create_risk(entity, validation[0][entity]),
                            "#text": str(value),
                        }
                    # Entity was not in validation schema
                    else:
                        _dict[entity] = {"#text": str(value)}
                else:
                    # Entity was in validation schema but no errors
                    _dict[entity] = {"@risk": "low", "#text": str(value)}

    if "validation" in result:
        traverse_merge_items(
            result["invoiceExtractor"]["entities"], return_dict, result["validation"]
        )
    else:
        traverse_merge_items(result["invoiceExtractor"]["entities"], return_dict)

    result["invoiceExtractor"]["entities"] = return_dict


def clean_datastructure(result):
    result["invoiceExtractor"]["entities"]["lineItems"] = {}
    result["invoiceExtractor"]["entities"]["lineItems"]["item"] = result[
        "invoiceExtractor"
    ]["entities"]["items"]

    del (
        result["invoiceExtractor"]["entities"]["items"],
        result["invoiceExtractor"]["probabilities"],
        result["invoiceExtractor"]["infos"],
    )


def create_risk(entity, validation_errors):
    """ Create risk flag """
    err_amount = len(validation_errors)

    if err_amount == 0:
        return "low"
    elif err_amount == 1:
        return "med"
    else:
        return "high"
