import os

from pyexlatex import BibTexArticle

from bibtex_gen import BibTexGenerator


class BibTexTest:
    item_accessor = 'da-engelberg-gao-2011'
    item_accessor2 = 'barber-odean-2008'
    doi = '10.1111/j.1540-6261.2011.01679.x'
    doi2 = '10.1093/rfs/hhm079'
    doi_dict = {
        item_accessor: doi,
        item_accessor2: doi2,
    }
    expect_bibtex = BibTexArticle(
        item_accessor,
        'Zhi Da and Joseph Engelberg and Pengjie Gao',
        'In Search of Attention',
        'Journal of Finance',
        2011,
        volume='66',
        number='5',
        pages='1461-1499',
        month=10
    )
    expect_bibtex2 = BibTexArticle(
        item_accessor2,
        'Brad M. Barber and Terrance Odean',
        'All that glitters: The effect of attention and news on the buying '
        'behavior of individual and institutional investors',
        'Review of Financial Studies',
        2008,
        volume='21',
        number='2',
        pages='785-818',
        month=4
    )

    def client_id_and_secret_from_env(self):
        client_id = os.environ['MENDELEY_CLIENT_ID']
        secret = os.environ['MENDELEY_SECRET']
        return client_id, secret

    def create_bibtex_gen(self) -> BibTexGenerator:
        client_id, secret = self.client_id_and_secret_from_env()
        btg = BibTexGenerator(client_id, secret)
        return btg


class TestBibtexGenerator(BibTexTest):

    def test_create_bibtex_gen(self):
        btg = self.create_bibtex_gen()
        assert isinstance(btg, BibTexGenerator)

    def test_get_one_bibtex(self):
        btg = self.create_bibtex_gen()
        bibtex = btg.generate(self.doi, self.item_accessor)
        assert bibtex == self.expect_bibtex

    def test_get_multiple_bibtex_objs(self):
        btg = self.create_bibtex_gen()
        bibtex_objs = btg.generate_from_dict(self.doi_dict)
        assert self.expect_bibtex in bibtex_objs
        assert self.expect_bibtex2 in bibtex_objs

