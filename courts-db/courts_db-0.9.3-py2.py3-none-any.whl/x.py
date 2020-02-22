# -*- coding: utf-8 -*-
from unittest import TestCase
import unittest
import json
from string import Template, punctuation
from datetime import datetime as dt
import re
from glob import iglob
import pandas
import unicodedata
import six
import os
from utils import load_courts_db, gather_regexes, db_root

import collections

reg_punc = re.compile('[%s]' % re.escape(punctuation))
combined_whitespace = re.compile(r"\s+")
accents = re.compile('([^\w\s%s]+)' % re.escape(punctuation))
local_path = "/Users/Palin/Code/courtlistener/cl/assets/media/opinion_metadata/lexis/%s.csv"

courts = load_courts_db()
regexes = gather_regexes(courts)


def find_court(court_str, filed_date=None, bankruptcy=False):
    """
    :param court_str:
    :param filed_date:
    :param regexes:
    :return:
    """
    cd = {}
    cdd = []
    court_matches = []

    assert (
        type(court_str) == six.text_type
    ), "court_str is not a text type, it's of type %s" % type(court_str)
    for regex, court_id, court_name, court_type in regexes:
        match = re.search(regex, court_str)
        if match:
            court_matches.append(court_id)
            if court_id is None:
                court_id = court_name
            cd[match.group()] = court_id
            cdd.append({"id": court_id, "text": match.group(), "court_name":court_name, "court_type":court_type})
            # print(cdd)

    results = list(set(court_matches))
    if len(results) > 1:
        court_matches = []
        remove_list = [x["text"] for x in cdd]
        subsetlist = []

        for test in remove_list:
            for item in [x for x in remove_list if x != test]:
                if test in item:
                    subsetlist.append(test)
        final_list = [x for x in remove_list if x not in subsetlist]

        for r in cdd:
            if r["text"] in final_list:
                court_key = r["id"]
                court_matches.append(court_key)

    court_matches = list(set(court_matches))


    if court_matches > 1:
        new_cd = [x for x in cdd if x['id'] in court_matches]
        bank = list(set([x['id'] for x in new_cd if x['court_type'] == "bankruptcy"]))
        non_bank = list(set([x['id'] for x in new_cd if x['court_type'] != "bankruptcy"]))

        if bankruptcy == True:
            if len(bank) == 1:
                return bank
            else:
                if len(non_bank) == 1:
                    return non_bank
        else:
            if len(non_bank) == 1:
                return non_bank

    return court_matches

def load_template():
    """

    :return:
    """
    with open('data/courts.json', "r") as f:
        court_data = json.loads(f.read())

    with open('data/variables.json', "r") as v:
        variables = json.loads(v.read())

    for path in iglob("data/places/*.txt"):
        with open(path, "r") as p:
            places = "(%s)" % "|".join(p.read().splitlines())
            variables[path.split("/")[-1].split(".txt")[0]] = places

    s = Template(json.dumps(court_data)).substitute(**variables)
    return s.replace("\\", "\\\\")

def clean_punct(court_str):
    clean_court_str = reg_punc.sub(' ', court_str)
    clean_court_str = combined_whitespace.sub(' ', clean_court_str).strip()
    ccs = clean_court_str.title().decode('unicode_escape')
    return ccs

reg_punc = re.compile("[%s]" % re.escape(punctuation))
combined_whitespace = re.compile(r"\s+")


def strip_punc(court_str):
    clean_court_str = reg_punc.sub(" ", court_str)
    clean_court_str = combined_whitespace.sub(" ", clean_court_str).strip()
    ccs = "%s" % clean_court_str.title()

    return ccs

def remove_accents(text):
    if re.search(accents, text):
        text = unicode(text, 'utf-8')
        text = unicodedata.normalize('NFD', text)
        text = text.encode('ascii', 'ignore')
        text = text.decode("utf-8")
    return text

def get_court_list(fp):
    print fp
    court_set = set()
    df = pandas.read_csv(fp, usecols=['court'])
    cl = df['court'].tolist()

    try:
        cl = [x for x in cl if type(x) == str]
    except:
        print x

    long_list = []
    for item in cl:
        clean_str = clean_punct(item)
        long_list.append(clean_str)

    c = collections.Counter(long_list)
    return c

def get_court_list_west(fp):
    # print fp
    court_set = set()
    df = pandas.read_csv(fp, usecols=['Court Line'])
    cl = df['Court Line'].tolist()

    try:
        cl = [x for x in cl if type(x) == str]
    except:
        print x

    long_list = set()
    for item in cl:
        clean_str = clean_punct(item)
        long_list.add(clean_str)

    # c = collections.Counter(long_list)
    c = list(long_list)
    return c
    # court_list = set(cl)
    #
    # for court_str in court_list:
    #     try:
    #         clean_str = clean_punct(court_str)
    #         court_set.add(clean_str)
    #     except Exception as e:
    #         print court_str, str(e)

    # return court_set


def get_court_list_x(fp):
    print fp
    court_set = set()
    # df = pandas.read_csv(fp, usecols=['court'])
    # cl = df['court'].tolist()
    df = pandas.read_csv(fp,
                         nrows=10000,
                         usecols=['zip_title', 'court', "lexis_ids_normalized"]
                         )
    cl = []
    for row in df.iterrows():
        # print(row[1]['court'])
        if type(row[1]['court']) == str:
            clx = " 0 ".join([x for x in row[1] if type(x) == str and "00000" not in x])
            # cl.append(row[1]['court'] + " " + row[1]['zip_title'])
            cl.append(clx)

    try:
        cl = [x for x in cl if type(x) == str]
    except:
        print x
    court_list = set(cl)

    for court_str in court_list:
        try:
            clean_str = clean_punct(court_str)
            court_set.add(clean_str)
        except Exception as e:
            print court_str, str(e)

    return court_set



class DataTest(TestCase):
    """ """




    def test_str(self):
        # """Can we extract the correct court id from string and date?"""

        bankruptcy = False
        text = u"State Of Wisconsin Circuit Court Of Waukesha County"


        court_str = clean_punct(text)
        if bankruptcy==True:
            bank = True
        else:
            bank = False
        print court_str

        matches = find_court(
            court_str=court_str,
            filed_date=None,
            bankruptcy=bank
        )

        print matches, "==", ['mntaxct']
        # self.assertEqual(matches, ['mnd'])



    def test_west(self):
        count = 0
        court_set = set()
        reporter = "bankruptcy"
        volume = "*"

        s = load_template()
        courts = json.loads(s)


        regexes = []
        for court in courts:
            for reg_str in court['regex']:
                reg_str = re.sub(r'\s{2,}', ' ', reg_str)
                regex = re.compile(reg_str, re.I)
                regexes.append((regex, court['id']))

        gpath = "/Users/Palin/Code/courtlistener/cl/assets/media/opinion_metadata/%s/%s_vol_%s.csv" % (reporter, reporter, volume)
        for file_path in iglob(gpath):
            current_reporter = file_path.split("opinion_metadata/")[1].split("/")[0]
            if reporter != current_reporter:
                reporter = current_reporter
                # print reporter

            if 1 == 1:
            # if "lexis" not in file_path and "bankruptcy" not in file_path:
                cd = {}
                df = pandas.read_csv(file_path,
                                     usecols=['Court Line'],
                                     )

                cl = df['Court Line'].tolist()
                cl = [x for x in cl if type(x) == str]
                courts = set(cl)

                for court_str in courts:
                    try:
                        clean_court_str = re.sub("[%s]" % re.escape(punctuation), ' ', court_str)
                        clean_court_str = re.sub(r'\s{2,}', ' ', clean_court_str)
                        clean_court_str = clean_court_str.title().strip()
                        court_set.add(clean_court_str)
                    except Exception as e:
                        print court_str, str(e)

        output = []
        for court_strings in court_set:

            matches = find_court_alt(court_str=court_strings,
                                     regexes=regexes)
            # if len(matches) > 0:
            for match in matches:
                if match is not None and match != "":
                    if match[-1] == "b":
                        matches.remove(match)

            if len(list(set(matches))) != 1:
                count = count + 1
                print count, matches, "\t\t\t", court_strings
                output.append(court_strings)

        # print "\n\n\n"
        # for x in sorted(output):
        #     print x
        #
        with open(os.path.join(db_root, "junk", "west_output.txt"), 'w') as f:
            for item in sorted(output):
                f.write("%s\n" % item)


    def test_lexis(self):
        # /Users/Palin/Code/courtlistener/cl/assets/media/opinion_metadata/lexis/20190510
        # _minimal_metadata_state.csv -- 85 left
        # _minimal_metadata_circuit.csv  -- 114 left
        # _minimal_metadata_district.csv -- 180 left
        # _minimal_metadata_fed_other.csv -- 2 left
        # _minimal_metadata_supreme.csv -- 1 left

        count = 0
        volume = "*state"

        output = []
        duplicates = []


        for file_path in iglob(local_path % volume):
            if "bankruptcy" in file_path:
                banktupcy = True
            else:
                banktupcy = False

            collect = get_court_list(fp=file_path)
            court_set = collect.keys()

            for court_string in court_set:
                matches = find_court(
                    court_str=court_string,
                    bankruptcy=banktupcy,
                    filed_date=None
                )

                if len(list(set(matches))) < 1:
                    count = count + 1
                    # print count, matches, "\t\t\t", court_strings
                    output.append(court_string)
                elif len(list(set(matches))) > 1:
                    duplicates.append(court_string)

        joined_list = sorted(output) + \
                      ["\n--- NOW DUPLICATES --- \n"] + \
                      sorted(duplicates) + [str(sum(collect.values()))]


        with open(os.path.join(db_root,
                               "stuff",
                               "lexis_output_%s.txt" % volume[1:]), 'w') as f:
            for item in joined_list:
                f.write("%s, %s\n" % (collect[item.encode("latin")], item.encode("latin")))
                # f.write("%s\n" % item.encode("latin"))


    def test_west_new(self):
        count = 0
        court_set = set()
        reporter = "*"
        volume = "*"

        courts = load_courts_db()
        output = []
        duplicates = []
        court_set = []
        regexes = gather_regexes(courts)
        gpath = "/Users/Palin/Code/courtlistener/cl/assets/media/opinion_metadata/%s/%s_vol_%s.csv" % (reporter, reporter, volume)
        for file_path in iglob(gpath):
            current_reporter = file_path.split("opinion_metadata/")[1].split("/")[0]
            if reporter != current_reporter:
                reporter = current_reporter
                print reporter

            if "lexis" not in file_path:
                if "bankruptcy" in file_path:
                    bankruptcy = True
                    regex = self.bank_regexes
                else:
                    bankruptcy = False
                    regex = self.regexes

                cs = get_court_list_west(fp=file_path)
                court_set = court_set + cs

                # court_set = collect.keys()
        court_set = list(set(court_set))
        for court_string in court_set:

            matches = find_court(
                court_str=court_string,
                regexes=regex,
                bankruptcy=bankruptcy,
                filed_date=None
            )

            if len(list(set(matches))) < 1:
                count = count + 1
                # print count, matches, "\t\t\t", court_strings
                output.append(court_string)
            elif len(list(set(matches))) > 1:
                duplicates.append(court_string)

        joined_list = sorted(output) + \
                      ["\n--- NOW DUPLICATES --- \n"] + \
                      sorted(duplicates)


        with open(os.path.join(db_root, "junk", "west_output.txt"), 'w') as f:
            for item in joined_list:
                f.write("%s\n" % (item.encode("latin")))
                # f.write("%s\n" % item.encode("latin"))


    def test_regex(self):
        court_str = "Trib  unal   Circuito,,, De Ápelációnes De Puerto Rico"
        reg_punc = re.compile('[%s]' % re.escape(punctuation))
        combined_whitespace = re.compile(r"\s+")
        clean_court_str = reg_punc.sub(' ', court_str)
        clean_court_str = combined_whitespace.sub(' ', clean_court_str)
        print clean_court_str



    def test_find_row(self):
        # fp = "_minimal_metadata_district.csv"
        # fp = "_minimal_metadata_fed_other_sample.csv"
        # fp = "_minimal_metadata_state.csv"
        # fp = "_minimal_metadata_bankruptcy.csv"
        # df = pandas.read_csv(fp, usecols=['court', "lexis_ids_normalized"])
        fp = "_minimal_metadata_circuit.csv" # -- 114 left

        df = pandas.read_csv(fp,
                             skiprows=0,
                             nrows=100
                             )
        # df2 = pandas.read_csv(fp, usecols=['lexis_ids_normalized'])

        for row in df.iterrows():
            print (row)
            # if "US Cases/NY Lower Court Cases" in row[1]['zip_title']:
            #     print row[1]['court']#, row[1]['zip_title']
                # print(row[2]['court'])

        # cols = pandas.read_csv(fp, nrows=1).columns.tolist()
        # l = sorted(list(set(df['zip_title'].tolist())))
        # for item in l:
        #     print item
        # chunksize = 10 ** 6
        # # for chunk in pd.read_csv(filename, chunksize=chunksize):
        # #     process(chunk)
        #
        # for df in pandas.read_csv(fp,
        #                      # skiprows=50,
        #                      # nrows=100,
        #                      skip_blank_lines=True,
        #                     chunksize=chunksize):
        # # print df
        #     for index, row in df.iterrows():
        #         # print(row[2], row[0], row[3], row[4])
        #
        #         if type(row[2]) is float:
        #             continue
        #         try:
        #             example = strip_punc(row[2]).title()
        #             # print(example)
        #             if "Public Utilities" in example:
        #                 print(row[2], row[0], row[3], row[4])
        #             # if example == "Before Public Utilities Commission":
        #         except:
        #             print(row[2], row[0], row[3], row[4])

        # print df["Surrogate" in df['court']]

        # count = 0
        # for item in df['court']:
        #     count = count + 1
        #     if item == "District Court, S.d. New York":
        #         print item
        #         break
        # cl1 = df['court'].tolist()
        # cl2 = df2['lexis_ids_normalized'].tolist()
        #
        #
        # i = 0
        # for item in cl1:
        #     if type(item) == str:
        #         if "Massachusetts" in item  and "Rhode Island" in item:
        #             print cl1[i], cl2[i]
        #     i = i+1

        # l = [x.title() for x in cl if type(x) == str]
        # j = [x for x in l if "Southern District" in x and "Eastern District" in x and "New York" in x]
        # for i in j:
        #     print i
        # for i, j in df.iterrows():
        #     if j['court'] == type(str):
        #         if "Southern District" in j['court'] and "Eastern District" in j['court'] and "New York" in j['court']:
        #             print i, j
            # print j['court']
        #     try:
        #         if "eastern" in j['court'].lower() and "southern" in j['court'].lower() and "new york" in j['court'].lower():
        #         # if j['court'] == "United States District Court For The Eastern District Of New York And Southern District Of New York":
        #             print(i, j)
        #     except:
        #         pass

                # print()
        # cl = df['court'].tolist()
        #
        # cl = [x for x in cl if type(x) == str]
        # court_list = set(cl)
        #
        # for court_str in court_list:
        #     try:
        #         clean_str = clean_punct(court_str)
        #         if clean_str == "Courts Of Appeal Of Oklahoma Division No 20":
        #             print court_str
        #         court_set.add(clean_str)
        #     except Exception as e:
        #         print court_str, str(e)

    # def test_lexis_other(self):
    #     # _minimal_metadata_state.csv -- 231 left
    #     # _minimal_metadata_circuit.csv  -- 114 left
    #     # _minimal_metadata_district.csv -- 222 left
    #     # _minimal_metadata_fed_other.csv -- 2 left
    #     # _minimal_metadata_supreme.csv -- 1 left
    #     count = 0
    #     reporter = "lexis"
    #     volume = "20190510_minimal_metadata_state"
    #
    #     courts = load_courts_db()
    #     output = []
    #     duplicates = []
    #
    #     regexes = gather_regexes(courts)
    #
    #     for file_path in iglob(local_path % volume):
    #         if "bankruptcy" in file_path:
    #             continue
    #
    #         court_set = get_court_list_x(fp=file_path)
    #         print("__next__")
    #         for court_string in court_set:
    #             matches = find_court(
    #                 court_str=court_string,
    #                 regexes=regexes,
    #                 bankruptcy=None,
    #                 filed_date=None
    #             )
    #
    #             if len(list(set(matches))) < 1:
    #                 count = count + 1
    #                 print count, matches, "\t\t\t", court_string
    #                 output.append(court_string)
    #             elif len(list(set(matches))) > 1:
    #                 duplicates.append(court_string)
    #
    #     joined_list = sorted(output) + \
    #                   ["\n--- NOW DUPLICATES --- \n"] + \
    #                   sorted(duplicates)
    #
    #     with open(os.path.join(db_root, "junk", "lexis_output_next.txt"), 'w') as f:
    #         for item in joined_list:
    #             f.write("%s\n" % item.encode("latin").replace(" 0 ", "\t"))


if __name__ == '__main__':
    unittest.main()
