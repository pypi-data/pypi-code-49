import os
from concurrent.futures import ThreadPoolExecutor as Executor
from pathlib import Path

import click
import xlsxwriter
from filetype import guess

from ..services.requests import extract_invoice
from .commons import read_pdf


# TODO: Unfortunately here the list of important labels to export in Excel is hardcoded.
# Looking forward to a better solution that keeps the columns ordered in a usable way
# i.e. file path as the first column, amounts grouped together, etc.


COLUMN_ORDER = [
    "file_path",
    # 'message',
    "type",
    "number",
    "issuedAt",
    "deliveredAt",
    "recipientPoNumber",
    # TODO Client Specific Info is passed as CLIENT_NAME in yml, os.getenv, (also as CLIENT_NAME_LOCAL) in Makefile
    # https://github.com/hypatos/invoice-extractor-nextgen/blob/master/invoice_extractor/postprocessing/client_specific.py
    "osramPoNumber_01",
    "osramPoNumber_02",
    "osramPoNumber_03",
    "omyaRecipientPoNumber_01",
    "omyaRecipientPoNumber_02",
    "omyaRecipientPoNumber_03",
    "omyaOutboundDeliveryNumber_01",
    "omyaOutboundDeliveryNumber_02",
    "omyaOutboundDeliveryNumber_03",
    "omyaOrderNumber_01",
    "omyaOrderNumber_02",
    "omyaOrderNumber_03",
    "omyaShipmentNumber_01",
    "omyaShipmentNumber_02",
    "omyaShipmentNumber_03",
    "omyaServiceEntrySheetNumber_01",
    "omyaServiceEntrySheetNumber_02",
    "omyaServiceEntrySheetNumber_03",
    "city",
    "companyName",
    "address",
    "contactMail",
    "contactName",
    "contactPhone",
    "country",
    "postcode",
    "vatId",
    "taxNumber",
    "customerNumber",
    "tax_net_0",
    "tax_rate_0",
    "tax_amount_0",
    "tax_net_1",
    "tax_rate_1",
    "tax_amount_1",
    "tax_net_2",
    "tax_rate_2",
    "tax_amount_2",
    "net",
    "due",
    "gross",
    "currency",
    "bank",
    "iban",
    "bic",
    "method",
    "serviceTime",
    "taxExemption",
]

RED_TO_GREEN_GRADIENT = [
    "#FF0000",
    "#FF1100",
    "#FF2300",
    "#FF3400",
    "#FF4600",
    "#FF5700",
    "#FF6900",
    "#FF7B00",
    "#FF8C00",
    "#FF9E00",
    "#FFAF00",
    "#FFC100",
    "#FFD300",
    "#FFE400",
    "#FFF600",
    "#F7FF00",
    "#E5FF00",
    "#D4FF00",
    "#C2FF00",
    "#B0FF00",
    "#9FFF00",
    "#8DFF00",
    "#7CFF00",
    "#6AFF00",
    "#58FF00",
    "#47FF00",
    "#35FF00",
    "#24FF00",
    "#12FF00",
    "#00FF00",
]


def convert_to_xlsx(
    path,
    extractor_endpoint,
    vat_validator_endpoint=None,
    validation_endpoint=None,
    token=None,
    workers=6,
):
    types = ("*.pdf", "*.tif", "*.tiff", "*.png", "*.jpg")
    file_count = 0
    fieldnames = set()
    result = {}

    with Executor(max_workers=workers) as exe:
        for file_type in types:
            full_path = os.path.join(os.getcwd(), path)
            files = Path(full_path).rglob(file_type)
            jobs = [
                exe.submit(
                    extract_invoice,
                    read_pdf(str(filename)),
                    extractor_endpoint,
                    guess(str(filename)).mime,
                    token,
                )
                for filename in files
                if guess(str(filename)).mime
            ]
            label = f"Converting {len(jobs)} invoices with {file_type} extension"
            with click.progressbar(jobs, label=label) as bar:
                for id, job in enumerate(bar):
                    file_path, response = job.result()
                    result[file_count] = flatten_invoice(response)
                    result[file_count]["file_path"] = (file_path.split("/")[-1], None)
                    [
                        fieldnames.add(fieldname)
                        for fieldname in result[file_count].keys()
                    ]
                    file_count += 1

    if not result:
        quit(f"No files of extension: {types} found in path")

    processed_dir_name = os.path.normpath(path).split(os.path.sep)[-1]
    workbook = xlsxwriter.Workbook(f"{processed_dir_name}.xlsx")
    workbook.add_worksheet("Extraction Results")
    bold_header = workbook.add_format({"bold": True})
    red_to_green_formats = [
        workbook.add_format({"bold": True, "bg_color": color})
        for color in RED_TO_GREEN_GRADIENT
    ]
    worksheet = workbook.get_worksheet_by_name("Extraction Results")

    for col_idx, column_name in enumerate(COLUMN_ORDER):
        worksheet.write(0, col_idx, column_name, bold_header)

    for row_idx, invoice in result.items():
        for col_idx, column_name in enumerate(COLUMN_ORDER):
            if column_name in invoice:
                column_value, probability = invoice[column_name]
                if not probability:
                    worksheet.write(row_idx + 1, col_idx, column_value)
                else:
                    color_idx = int(len(red_to_green_formats) * probability)
                    worksheet.write(
                        row_idx + 1,
                        col_idx,
                        column_value,
                        red_to_green_formats[color_idx],
                    )

    workbook.close()


def flatten_invoice(invoice):
    return_dict = {"message": ("", None)}

    def traverse_items(entities, probabilities, _dict, *idx):
        for k, entity in entities.items():
            if isinstance(entity, dict):
                traverse_items(entities[k], probabilities[k], return_dict)
            elif isinstance(entity, list):
                for counter, list_item in enumerate(entity):
                    if k != "terms":
                        temp_dict = {}
                        for item, value in list_item.items():
                            temp_dict[f"{k}_{item}_{counter}"] = value
                        traverse_items(temp_dict, probabilities[k], return_dict)
            else:
                if k in probabilities and probabilities[k]:
                    _dict[k] = (entity, probabilities[k])
                else:
                    _dict[k] = (entity, None)

    try:
        traverse_items(invoice["entities"], invoice["probabilities"], return_dict)
    except Exception as e:
        return_dict["message"] = (f"Flatten error: {e}", None)
    return return_dict
