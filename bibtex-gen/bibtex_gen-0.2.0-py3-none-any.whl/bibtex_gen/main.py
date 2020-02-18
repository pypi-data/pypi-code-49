from typing import List, Dict, Sequence, Optional
from mendeley2 import Mendeley
from mendeley2.auth import MendeleySession
from pyexlatex.models.references.bibtex.base import BibTexEntryBase
from pyexlatex.texparser.references.bibtex.extract import extract_bibtex_str
from bibtex_gen.mendeley import bib_tex_from_mendeley_doc


class BibTexGenerator:
    """
    Get BibTeX objects from DOIs using the Mendeley API

    :Examples:

        >>> import bibtex_gen
        >>> # Note: these are fake credentials. You need to sign up for a Mendeley account, go to Mendeley Developers,
        >>> # and create an "app" which will give you this info.
        >>> mendeley_client_id: str = '9871'
        >>> mendeley_client_secret: str = 'sdfa4dfDSSDFasda'
        >>> btg = bibtex_gen.BibTexGenerator(mendeley_client_id, mendeley_client_secret)
        >>> # This object contains all the article data and can be used directly with pyexlatex
        >>> bibtex_obj = btg.generate('10.1111/j.1540-6261.2011.01679.x', 'da-engelberg-gao-2011')
        >>> # Or, multiple at once with a dict
        >>> item_doi_dict = {
        >>> 'da-engelberg-gao-2011': '10.1111/j.1540-6261.2011.01679.x',
        >>> 'barber-odean-2008': '10.1093/rfs/hhm079',
        >>> }
        >>> # These objects contain all the article data and can be used directly with pyexlatex
        >>> bibtex_objs = btg.generate_from_dict(item_doi_dict)
    """

    def __init__(self, mendeley_client_id: str, mendeley_client_secret: str):
        self.mendeley_client_id = mendeley_client_id
        self.mendeley_client_secret = mendeley_client_secret
        mendeley = Mendeley(mendeley_client_id, mendeley_client_secret)
        self.session = mendeley.start_client_credentials_flow().authenticate()

    def generate(self, doi: str, item_accessor: str) -> BibTexEntryBase:
        return bib_tex_from_doi(self.session, doi, item_accessor)

    def generate_from_dict(self, item_doi_dict: Dict[str, str]) -> List[BibTexEntryBase]:
        return item_accessor_doi_dict_to_bib_tex(
            item_doi_dict,
            self.mendeley_client_id,
            self.mendeley_client_secret,
        )


def _item_accessor_doi_dict_to_bib_tex(item_doi_dict: Dict[str, str], mendeley_client_id: str,
                                       mendeley_client_secret: str) -> List[BibTexEntryBase]:
    btg = BibTexGenerator(
        mendeley_client_id,
        mendeley_client_secret
    )
    bib_texs = [btg.generate(doi, item_accessor) for item_accessor, doi in item_doi_dict.items()]
    return bib_texs


def bib_tex_from_doi(mendeley_session: MendeleySession, doi: str, item_accessor: str) -> BibTexEntryBase:
    mendeley_doc = mendeley_session.catalog.by_identifier(doi=doi, view='bib')
    return bib_tex_from_mendeley_doc(mendeley_doc, item_accessor)


def item_accessor_doi_dict_to_bib_tex(item_doi_dict: Dict[str, str], mendeley_client_id: str,
                                      mendeley_client_secret: str,
                                      extra_bibtex_objs: Optional[Sequence[BibTexEntryBase]] = None,
                                      extract_from_str: Optional[str] = None
                                      ) -> List[BibTexEntryBase]:
    """
    Gets multiple BibTex objects from DOIs using the Mendeley API

    :param item_doi_dict:
    :param mendeley_client_id:
    :param mendeley_client_secret:
    :param extra_bibtex_objs:
    :param extract_from_str:
    :return:

    :Examples:

        >>> # Note: these are fake credentials. You need to sign up for a Mendeley account, go to Mendeley Developers,
        >>> # and create an "app" which will give you this info.
        >>> mendeley_client_id: str = '9871'
        >>> mendeley_client_secret: str = 'sdfa4dfDSSDFasda'
        >>> # Keys are name by which reference will be accessed, values are DOIs
        >>> item_doi_dict = {
        >>> 'da-engelberg-gao-2011': '10.1111/j.1540-6261.2011.01679.x',
        >>> 'barber-odean-2008': '10.1093/rfs/hhm079',
        >>> }
        >>> # These objects contain all the article data and can be used directly with pyexlatex
        >>> bibtex_objs = bibtex_gen.item_accessor_doi_dict_to_bib_tex(item_doi_dict, mendeley_client_id, mendeley_client_secret)


    """
    bib_texs = _item_accessor_doi_dict_to_bib_tex(
        item_doi_dict,
        mendeley_client_id,
        mendeley_client_secret
    )
    if extra_bibtex_objs:
        bib_texs.extend(extra_bibtex_objs)
    if extract_from_str:
        bib_texs.extend(extract_bibtex_str(extract_from_str))
    return bib_texs
