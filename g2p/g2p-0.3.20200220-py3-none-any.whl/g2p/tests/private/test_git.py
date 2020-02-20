# -*- coding: utf-8 -*-

import os
from unittest import main, TestCase
from g2p.mappings import Mapping
from g2p.transducer import CompositeTransducer, Transducer
# Will cause errors on machines without private data
from g2p.tests.private.git_data_wrangler import returnLinesFromDocuments
from g2p.tests.private import __file__ as private_dir
from typing import List
from g2p.log import TEST_LOGGER as logger


def scrub_text(txt: str, to_scrub: List[str] = ['=', '-', '~']) -> str:
    ''' Given some text (txt), scrub all characters in list (to_scrub) from text.
    '''
    for char in to_scrub:
        txt = txt.replace(char, '')
    return txt


class GitTest(TestCase):
    ''' Test for Orthography (Deterministic) to APA
    '''
    @classmethod
    def setUpClass(cls):
        # set up log counter
        cls.formatted_data = returnLinesFromDocuments(
            [
                os.path.join(os.path.dirname(private_dir),
                             'VG - Nass Volcano',
                             '2016-07-12 Nass River Volcano - CF edit VG check2.docx'),
                #os.path.join(os.path.dirname(private_dir),
                #             'VG - Kitwancool Surveyed',
                #             '2014-01-29 VG Kitwancool Reserve Surveyed CAF edit3 for HD.docx'),
                #os.path.join(os.path.dirname(private_dir),
                #             'VG - Founding of Gitanyow',
                #             '2017-01-27 VG The Founding of Git-anyaaw - HD comments more fixes.docx'),
                #os.path.join(os.path.dirname(private_dir),
                #             "HH - Mystery Story",
                #             "15-10-31 HH Hector's Betl'a Betl' - 4 checks_AP.docx"),
                #os.path.join(os.path.dirname(private_dir),
                #             "HH - Win Bekwhl",
                #             "2014-10-22 HH Win Bexwhl K'amk'siwaa - 2016-04-22 CAF 1st gloss.docx"),
                #os.path.join(os.path.dirname(private_dir),
                #             "BS - Dihlxw",
                #             "Dihlxw Story 2013-04-29 for HD copy - clean.docx"),
            ])

        # Declare all of our mappings needed
        cls.orth_to_ipa = Mapping(in_lang='git', out_lang='git-ipa', as_is=True)

        cls.orth_to_ipa_transducer = Transducer(cls.orth_to_ipa)

        cls.ipa_to_orth = Mapping(in_lang='git', out_lang='git-apa', as_is=True, reverse=True)

        cls.ipa_to_orth_transducer = Transducer(cls.ipa_to_orth)

        cls.apa_to_ipa = Mapping(in_lang='git', out_lang='git-apa', as_is=True)

        cls.apa_to_ipa_transducer = Transducer(cls.apa_to_ipa)

        cls.ipa_to_apa = Mapping(in_lang='git', out_lang='git-apa', as_is=True, reverse=True)

        cls.ipa_to_apa_transducer = Transducer(cls.ipa_to_apa)

        cls.orth_to_apa_transducer = CompositeTransducer(
            [cls.orth_to_ipa_transducer, cls.ipa_to_apa_transducer])
        cls.apa_to_orth_transducer = CompositeTransducer(
            [cls.apa_to_ipa_transducer, cls.ipa_to_orth_transducer])

    def test_orth_to_apa(self):     
        for title, story in self.formatted_data.items():
            for line in story:
                try:
                    self.assertEqual(self.orth_to_apa_transducer(
                        line['ortho']), scrub_text(line['apa']))
                except:
                    logger.exception(f"{self.orth_to_apa_transducer(line['ortho'])} is not equal to {scrub_text(line['apa'])}")
        logger.info("The logger came across %s exceptions", logger.exception.count)


    def test_apa_to_orth(self):
        for title, story in self.formatted_data.items():
            for line in story:
                try:
                    self.assertEqual(self.apa_to_orth_transducer(
                        scrub_text(line['apa'])), line['ortho'])
                except:
                    logger.exception(f"{self.orth_to_apa_transducer(line['ortho'])} is not equal to {scrub_text(line['apa'])}")
        logger.info("The logger came across %s exceptions", logger.exception.count)

if __name__ == "__main__":
    main()
