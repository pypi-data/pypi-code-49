from mendeley2.models.catalog import CatalogBibDocument
from pyexlatex.models.references.bibtex.base import BibTexEntryBase
import pyexlatex as pl


def bib_tex_from_mendeley_doc(mendeley_doc: CatalogBibDocument, item_accessor: str) -> BibTexEntryBase:
    if mendeley_doc.type != 'journal':
        raise NotImplementedError('cannot handle reference types other than journal yet')

    ref = pl.BibTexArticle(
        item_accessor,
        authors_str_from_mendeley_doc(mendeley_doc),
        mendeley_doc.title,
        mendeley_doc.source,
        mendeley_doc.year,
        volume=mendeley_doc.volume,
        number=mendeley_doc.issue,
        pages=mendeley_doc.pages,
        month=mendeley_doc.month
    )

    return ref


def authors_str_from_mendeley_doc(mendeley_doc: CatalogBibDocument) -> str:
    author_names = [f'{author.first_name} {author.last_name}' for author in mendeley_doc.authors]
    return ' and '.join(author_names)
