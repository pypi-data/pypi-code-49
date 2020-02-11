import logging

import click

from rho_pdf_diff.image_construction.document_diff_image import DiffImageWriter
from rho_pdf_diff.document_creation import build_document
from rho_pdf_diff.filter_rules import CapitalizationFilter, PunctuationFilter, RegexFilter, SameTextFilter
from rho_pdf_diff.text_diff import DiffResult

logger = logging.getLogger('rho_pdf_diff')
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


@click.command()
@click.argument('pdf-1-path', type=str)
@click.argument('pdf-2-path', type=str)
@click.argument('output-path', type=str)
@click.option('-c', '--keep-caps', is_flag=True)
@click.option('-p', '--keep-punct', is_flag=True)
@click.option('-r', '--keep-non-alpha-numeric', is_flag=True)
@click.option('-a', '--skip-alignment', is_flag=True)
@click.option('-d', '--skip-diff-dedupe', is_flag=True)
def rho_pdf_diff(pdf_1_path: str, pdf_2_path: str, output_path: str,
                 keep_caps: bool, keep_punct: bool,
                 keep_non_alpha_numeric: bool, skip_alignment: bool,
                 skip_diff_dedupe: bool):
    doc_1 = build_document(path_to_pdf=pdf_1_path)
    doc_2 = build_document(path_to_pdf=pdf_2_path)
    filters = []
    if not keep_caps:
        filters.append(CapitalizationFilter())
    if not keep_punct:
        filters.append(PunctuationFilter())
    if not keep_non_alpha_numeric:
        filters.append(RegexFilter())
    if not skip_diff_dedupe:
        filters.append(SameTextFilter())

    diff_result = DiffResult(new_doc=doc_2, old_doc=doc_1, filter_rules=filters)
    print("Text diff finished, building image...")
    image_writer = DiffImageWriter(original_new_doc_path=pdf_2_path,
                                   original_old_doc_path=pdf_1_path,
                                   diff_result=diff_result,
                                   align_pages=not skip_alignment)
    image_writer.write_diff_pdf(output_path=output_path)
    print("Finished!")


