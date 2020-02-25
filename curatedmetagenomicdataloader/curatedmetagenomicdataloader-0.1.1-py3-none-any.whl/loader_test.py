from curatedmetagenomicdataloader import loader
import pandas as pd
import os
import random

keys = ['body_site', 'title', 'path']
query = "SELECT {0} FROM annotations where annotation = 'metaphlan_bugs_list';".format(', '.join(keys))
query2 = "SELECT {0} FROM annotations where annotation = 'pathabundance_relab';".format(', '.join(keys))
diseases = loader.get_unique_phenotypes('disease')
filters_dict = {disease:"SELECT sampleID, title, body_site FROM phenotypes WHERE disease LIKE '%{0}%'".format(disease) for disease in diseases}

def test_get_row_ids():

    row_ids = loader.get_row_ids(query, filters_dict, keys)
    assert len(row_ids) == 49
    assert type(row_ids) is dict

def test_get_row_labels():

    labels_dict = loader.get_row_labels(query, filters_dict, keys)
    assert len(labels_dict) == 62

def test_get_file_labels():

    labels_dict = loader.get_file_labels(query, filters_dict, keys)
    assert len(labels_dict) == 38 # HMP is left out

def test_extract_row_ids():

    filepath = 'LomanNJ_2013/stool/metaphlan_bugs_list'
    row_ids = ['OBK1122', 'OBK1196', 'OBK1253', 'OBK2535', 'OBK2638', 'OBK2661', 'OBK2668', 'OBK2723', 'OBK2741', 'OBK2752', 'OBK2758', 'OBK2764',
        'OBK2772', 'OBK2828', 'OBK2840', 'OBK2848', 'OBK2849', 'OBK2878', 'OBK2880', 'OBK2896', 'OBK2971', 'OBK3014', 'OBK3132', 'OBK3134', 'OBK3135',
        'OBK3185', 'OBK3303', 'OBK3549', 'OBK3587', 'OBK3646', 'OBK3751', 'OBK3852', 'OBK3958', 'OBK4096', 'OBK4112', 'OBK4141', 'OBK4168', 'OBK4198',
        'OBK4328', 'OBK4508', 'OBK4961', 'OBK5066', 'OBK2535b',
        ]
    df = loader.extract_row_ids(filepath, row_ids)
    assert (df.index == row_ids).all()

def test_assign_file_name():

    file_name = loader.assign_file_name(query, filters_dict)
    # Test order invariance
    random.shuffle(diseases)
    filters_dict2 = {disease:"SELECT sampleID, title, body_site FROM phenotypes WHERE disease LIKE '%{0}%'".format(disease) for disease in diseases}
    file_name2 = loader.assign_file_name(query, filters_dict2)
    assert file_name == file_name2
    new_keys = ['body_site', 'title']
    new_query = "SELECT {0} FROM annotations where annotation = 'metaphlan_bugs_list';".format(', '.join(new_keys))
    file_name3 = loader.assign_file_name(new_query, filters_dict)
    assert file_name3 != file_name

def test_all_columns_functional():

    cols = loader.all_columns_functional(use_cache=False, update_cache=False)
    assert type(cols) is pd.Index
    assert len(cols) > 70000

def test_LoaderPipe():

    meta_columns = loader.all_columns_metaphlan()
    ladder = loader.LoaderPipe(interpolate_columns=meta_columns)
    ladder.load(query, filters_dict)
    batch = ladder[0:10]
    assert 'examples' in batch
    assert 'label' in batch
    functional_columns = loader.all_columns_functional()
    bladder = loader.LoaderPipe(interpolate_columns=functional_columns)
    bladder.load(query2, filters_dict)
    batch = bladder[0:10]
    for col in ['SampleID', 'label', 'example']:
        assert col in batch.columns

def test_load_columns():
    keys = ['body_site', 'title', 'path']
    query = "SELECT {0} FROM annotations where annotation = 'genefamilies_relab';".format(', '.join(keys))
    diseases = loader.get_unique_phenotypes('disease')
    filters_dict = {disease:"SELECT sampleID, title, body_site FROM phenotypes WHERE disease LIKE '%{0}%'".format(disease) for disease in diseases}
    cols = loader.all_columns_uniref()
    dataset = loader.LoaderPipe(interpolate_columns=cols)
