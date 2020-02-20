
# -*- coding: utf-8 -*-
# to import
import regex as re
import os
import json
from typing import Dict, List
from docx import Document
from gi2pi.mappings import Mapping
from gi2pi.transducer import Transducer


def normalize_string(to_norm: str) -> str:
    ''' Strip the text and normalize it
    '''
    mappings = Mapping(
        language={'lang': 'git', 'table': 'Unicode Normalization'})
    transducer = Transducer(mappings)
    norm = transducer(to_norm.strip())
    return norm


def getText(doc: str) -> List[str]:
    ''' Parse text from docx into a list of lines.
        :param doc: Docx file to read
        :returns: List of lines with type List[str] 
    '''
    language_data = []
    doc = Document(doc)
    for para in doc.paragraphs:
      # only add text that isn't empty
        if para.text and not (re.match(r'\d\.', para.text) and len(para.text) < 3):
            language_data.append(str(para.text))  # can't be used on strings
    return language_data


def returnLines(language_data: List[str]) -> List[Dict[str, str]]:
    ''' Turn lines into a list of dicts that represent
        the interlinear nature of the documents ortho.
        :param language_data: List of strings from docx file
        :returns: List of dictionaries containing:
            - ortho (orthographic transcription)
            - morph (morphological breakdown)
            - apa (APA)
            - gloss (gloss)
            - eng (English translation)
    '''
    LINES = []
    if language_data:
        LINE_DICT = {}
        for line in language_data[1:]:
            line = normalize_string(line)
            # If we are at the beginning of a line.
            beginning = len(LINE_DICT.keys()) == 0
            # Must match FULL line, can contain any lowercase/uppercase or combining lowline \u0332
            # Must not start with an apostrophe UNLESS it is for a resonant
            ortho_text = re.search(
                r'^([^\']|(\'N|\'M|\'L|\'W))[a-zA-Z\,\.\:\'\s\u0332\-\–\…\"\?]+[^\']$', line)
            # Should match orthography line if at beginning
            if beginning and not ortho_text:
                print(
                    f'Warning! Did not match Orthography in first line of line {language_data[1:].index(line)}')
            elif ortho_text:
                # If we have already read in a line, append to the lines list and continue
                if 'ortho' in LINE_DICT and len(LINE_DICT.keys()) == 5:
                    LINES.append(LINE_DICT)
                    LINE_DICT = {}
                if 'ortho' not in LINE_DICT:
                    LINE_DICT['ortho'] = line
                    continue

            # Gloss must have a number or upper case character in contrast to morph line
            gloss_text = re.search(
                r'(\=cn|cn\=|[1-3](sg|pl)?\.i{1,3}|3sg)', line
                # r'^[a-zA-Z0-9\,\.\'\=\~\-\s]*[^\']*(cn|iii)[a-zA-Z0-9\,\.\'\=\~\-\[\]\s]*([^\']|(tl\'|t\'|k\'|k\u0332\'|ts\'))*$', line
                # r'^[^\'][a-zA-Z0-9\,\.\'\=\~\-\s]+[^\']+([1-4]|cn)[a-zA-Z0-9\,\.\'\=\~\-\[\]\s]+([^\']|(tl\'|t\'|k\'|k\u0332\'|ts\'))$', line
            )
            if gloss_text:
                if 'gloss' in LINE_DICT and LINE_DICT['gloss']:
                    LINE_DICT['gloss'] += ' ' + line
                else:
                    LINE_DICT['gloss'] = line
                continue

            # If there's a schwa, it must be APA line
            apa_text = re.search(
                r'\u0259|\u0294|\u0313|\u0259|\u026c|\u02b7|\u03A7', line)
            if apa_text:
                if 'apa' in LINE_DICT and LINE_DICT['apa']:
                    LINE_DICT['apa'] += ' ' + line
                else:
                    LINE_DICT['apa'] = line
                continue

            # Similar to orthography regex, but lower case.
            morph_text = re.search(
                r'^([^\']|(\'n|\'m|\'l|\'w))[a-zA-Z\,\.\'\=\~\-\?\s\u0332]+([^\']|(tl\'|t\'|k\'|k\u0332\'|ts\'))$', line)
            if morph_text:
                if "morph" in LINE_DICT and LINE_DICT['morph']:
                    LINE_DICT['morph'] += ' ' + line
                else:
                    LINE_DICT['morph'] = line
                continue

            # English line is contained in single quotes at the beginning and end of line
            eng_text = re.search(
                r"^\'[a-zA-Z0-9\-\,\'\?\!\"\./\:\;\s\(\)\…\u2014\u0332\u2013]+\'$", line)
            if eng_text:
                if 'eng' in LINE_DICT and LINE_DICT['eng']:
                    LINE_DICT['eng'] += ' ' + line
                else:
                    LINE_DICT['eng'] = line
                continue
    LINES.append(LINE_DICT)
    return LINES


def returnLinesFromDocuments(docs: List[str]) -> Dict[str, List[Dict[str, str]]]:
    ''' Given a list of paths to docx documents, read the lines from them and parse them
        into the interlinear formatted Dict format.
        :param docs: A list of paths to docx files
    '''
    doc_dict = {}
    for doc in docs:
        data = getText(doc)
        lines = returnLines(data)
        fn, ext = os.path.splitext(doc)
        doc_dict[fn] = lines
    return doc_dict


if __name__ == '__main__':
    formatted = returnLinesFromDocuments(
        [
            os.path.join(
                'VG - Nass Volcano', '2016-07-12 Nass River Volcano - CF edit VG check2.docx'),
            os.path.join('VG - Kitwancool Surveyed',
                         '2014-01-29 VG Kitwancool Reserve Surveyed CAF edit3 for HD.docx'),
            os.path.join('VG - Founding of Gitanyow',
                         '2017-01-27 VG The Founding of Git-anyaaw - HD comments more fixes.docx'),
            os.path.join("HH - Mystery Story",
                         "15-10-31 HH Hector's Betl'a Betl' - 4 checks_AP.docx"),
            os.path.join(
                "HH - Win Bekwhl", "2014-10-22 HH Win Bexwhl K'amk'siwaa - 2016-04-22 CAF 1st gloss.docx"),
            os.path.join(
                "BS - Dihlxw", "Dihlxw Story 2013-04-29 for HD copy - clean.docx"),
        ])
    for k, v in formatted.items():
        with open(k+'.json', 'w', encoding='utf8') as f:
            json.dump(v, f)
        with open(k+'.txt', 'w', encoding='utf8') as f:
            all_ortho = '\n'.join([l['ortho'] for l in v])
            f.write(all_ortho)
        with open(k+'.xml', 'w', encoding='utf8') as f:
            all_ortho = '\n'.join(['<s>' + l['ortho'] + '</s>' for l in v])
            xml = f"<?xml version='1.0' encoding='utf-8'?><TEI><text xml:lang='git'><body><div type='page'><p>{all_ortho}</p></div></body></text></TEI>"
            f.write(xml)
